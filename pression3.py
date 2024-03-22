import tkinter as tk
import random
import math

class Manometer(tk.Canvas):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(width=200, height=300, bg="#008000")
        self.pressure = 0

    def set_pressure(self, pressure):
        self.pressure = pressure
        self.draw_meter()

    def draw_meter(self):
        self.delete("all")

        # Draw the meter outline
        self.create_oval(50, 50, 150, 150, outline="black", width=2)
        
        # Draw tick marks
        for angle in range(-90, 91, 10):
            x1 = 100 + 80 * math.cos(math.radians(angle))
            y1 = 100 + 80 * math.sin(math.radians(angle))
            x2 = 100 + 90 * math.cos(math.radians(angle))
            y2 = 100 + 90 * math.sin(math.radians(angle))
            self.create_line(x1, y1, x2, y2, fill="black", width=2)

        # Draw the pressure indicator
        angle = -90 + (self.pressure / 100 * 180)
        x1 = 100 + 80 * math.cos(math.radians(angle))
        y1 = 100 + 80 * math.sin(math.radians(angle))
        self.create_line(100, 100, x1, y1, fill="red", width=2)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Manometer")
        self.geometry("300x450")
        
        self.manometer = Manometer(self)
        self.manometer.place(x=50, y=50)  # Placer le manomètre

        self.pressure_label = tk.Label(self, text="Pressure: 0", font=("Helvetica", 12))
        self.pressure_label.place(x=100, y=20)  # Placer le label de pression plus haut

        self.update_pressure()

    def update_pressure(self):
        pressure = random.randint(0, 100)
        self.manometer.set_pressure(pressure)
        self.pressure_label.config(text=f"Pressure: {pressure}")
        self.after(1000, self.update_pressure)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
