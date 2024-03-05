import tkinter as tk
import random
import time

# Définir les valeurs minimale et maximale de la luminosité en lux
lux_min = 0
lux_max = 88000

# Fonction pour générer une couleur en fonction de la luminosité
def couleur_luminosite(luminosite):
    # Interpoler entre noir (0, 0, 0) et jaune (255, 255, 0) en fonction de la luminosité
    rouge = min(int(luminosite / lux_max * 255), 255)
    vert = min(int(luminosite / lux_max * 255), 255)
    bleu = 0
    
    # Convertir les valeurs RGB en une chaîne de couleur hexadécimale
    couleur_hex = '#{:02x}{:02x}{:02x}'.format(rouge, vert, bleu)
    return couleur_hex

# Fonction pour mettre à jour l'affichage de la luminosité
def mettre_a_jour_luminosite():
    # Générer une luminosité aléatoire dans la plage spécifiée
    luminosite = random.randint(lux_min, lux_max)
    ratio = 2.5
    
    # Mettre à jour l'affichage de la luminosité
    label_luminosite.config(text=str(luminosite) + " lux", bg=couleur_luminosite(luminosite))
    
    # Mettre à jour le rayon du cercle en fonction de la luminosité
    rayon = luminosite / 880
    canvas.delete("rayon_cercle")
    canvas.create_oval(50*ratio - rayon, 50*ratio - rayon, 50*ratio + rayon, 50*ratio + rayon, fill=couleur_luminosite(luminosite), outline='', tags="rayon_cercle")
    
    # Planifier la prochaine mise à jour après une seconde
    fenetre.after(1000, mettre_a_jour_luminosite)

# Créer une fenêtre tkinter
fenetre = tk.Tk()
fenetre.title("Représentation de la luminosité en lux")
fenetre.configure(bg='green')

# Créer un canevas pour dessiner le cercle
ratio = 2.5
    
canvas = tk.Canvas(fenetre, width=100*ratio, height=100*2.5, bg='green', highlightthickness=0)
canvas.pack()

# Créer un label pour afficher la luminosité
label_luminosite = tk.Label(canvas, text="0 lux", font=("android 101", 12), bg="black", fg="white", bd=2)
label_luminosite.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Mettre à jour initialement la luminosité
mettre_a_jour_luminosite()

# Lancer la boucle principale
fenetre.mainloop()
