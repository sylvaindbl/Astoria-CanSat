import tkinter as tk
import redis
import time

class ThermometreVisuel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Thermomètre Visuel")
        self.geometry("500x350")  # Taille du cadre augmentée
        
        self.current_temperature = 0
        self.canvas = tk.Canvas(self, width=200, height=242, bg="green")  # Taille du canvas ajustée
        self.canvas.pack(pady=20)
        
        self.label = tk.Label(self, bg="green", fg="white", text=f"Température actuelle: {self.current_temperature} °C", font=("Android 101", 24))
        self.label.pack()
        self.configure(bg="green")
        
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.update_temperature()
    
    def update_temperature(self):
        # Retrieve temperature value from Redis
        temperature_str = self.redis_client.get('temperature')
        if temperature_str:
            self.current_temperature = float(temperature_str.decode())
        else:
            # Use a default value if Redis has no temperature stored
            self.current_temperature = 0
        
        degrees = 40
        numbergrad = 8

        # Effacer le contenu précédent
        self.canvas.delete("temp_bar", "graduations")
        
        # Dessiner les graduations
        for i in range(0, degrees+1, int(degrees / numbergrad)):
            y = 200 - (i / degrees) * 150
            self.canvas.create_line(60, y, 80, y, fill="white", tags="graduations")
            self.canvas.create_text(55, y, anchor="e", text=str(i), fill="white", tags="graduations", font=("Android 101", 12))
        
        # Dessiner la barre de température avec dégradé de couleur et arrondis sur les coins
        temp_height = (self.current_temperature / degrees) * 150
        color = self.interpolate_color("#0000FF", "#FF0000", self.current_temperature / degrees)  # Bleu à rouge
        
        # Dessiner la barre de température avec des coins arrondis
        self.canvas.create_rectangle(100, 200, 150, 200 - temp_height, fill=color, outline=color, width=3, tags="temp_bar")

        # Mettre à jour l'étiquette avec la nouvelle température
        self.label.config(text=f" {self.current_temperature} °C")
        
        # Répéter la mise à jour toutes les secondes
        self.after(1000, self.update_temperature)
    
    def interpolate_color(self, color1, color2, fraction):
        r1, g1, b1 = self.hex_to_rgb(color1)
        r2, g2, b2 = self.hex_to_rgb(color2)
        r = round(r1 + (r2 - r1) * fraction)
        g = round(g1 + (g2 - g1) * fraction)
        b = round(b1 + (b2 - b1) * fraction)
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
    
    def hex_to_rgb(self, color):
        color = color.lstrip('#')
        return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

if __name__ == "__main__":
    app = ThermometreVisuel()
    app.mainloop()
