import tkinter as tk
import random

class AccelerationVisualizer(tk.Canvas):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(width=400, height=500, bg="green")
        self.draw_circle()
        self.draw_acceleration_value()
        self.update_acceleration()

    def draw_circle(self):
        self.create_oval(20, 20, 380, 380, outline="", width=3)  # Augmentation de la taille du cercle
        self.fill_arc_yellow = self.create_arc(20, 20, 380, 380, start=90, extent=0, outline="", fill="yellow")
        self.fill_arc_orange = self.create_arc(20, 20, 380, 380, start=90, extent=0, outline="", fill="orange")
        self.fill_arc_red = self.create_arc(20, 20, 380, 380, start=90, extent=0, outline="", fill="red")

    def draw_acceleration_value(self):
        x_center = 200
        y_center = 200
        radius = 150
        self.value_background = self.create_oval(x_center - radius, y_center - radius, x_center + radius, y_center + radius, outline="", fill="green")
        self.value_text = self.create_text(x_center, y_center, text="", fill="white", font=("android 101", 24))

    def update_acceleration(self):
        acceleration = random.uniform(0, 30)  # Générer une accélération aléatoire entre 0 et 30 m/s^2
        fill_extent = acceleration / 30 * 360
        
        if acceleration < 9.81:
            self.itemconfigure(self.fill_arc_yellow, extent=fill_extent)
            self.itemconfigure(self.fill_arc_orange, extent=0)
            self.itemconfigure(self.fill_arc_red, extent=0)
        elif acceleration < 19.62:
            self.itemconfigure(self.fill_arc_yellow, extent=359)
            self.itemconfigure(self.fill_arc_orange, extent=fill_extent)
            self.itemconfigure(self.fill_arc_red, extent=0)
        else:
            self.itemconfigure(self.fill_arc_orange, extent=359)
            self.itemconfigure(self.fill_arc_red, extent=fill_extent)
            self.itemconfigure(self.fill_arc_yellow, extent=0)
        
        self.itemconfigure(self.value_text, text="{:.2f} m/s^2".format(acceleration))
        self.after(1000, self.update_acceleration)  # Mettre à jour l'accélération toutes les secondes

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Acceleration Visualizer")
    acceleration_visualizer = AccelerationVisualizer(root)
    acceleration_visualizer.pack()
    root.mainloop()

