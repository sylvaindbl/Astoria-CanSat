import turtle
import random
import time

# Fonction pour dessiner une goutte d'eau
def draw_droplet(x, y, percent_full):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Dessin de la goutte d'eau
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.circle(50, 180)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.circle(50, 180)
    turtle.end_fill()

    # Dessin du remplissage de la goutte d'eau
    turtle.penup()
    turtle.goto(x - 50, y)
    turtle.pendown()
    turtle.fillcolor("lightblue")
    turtle.begin_fill()
    turtle.setheading(-90)
    turtle.forward(100 * (percent_full / 100))
    turtle.right(90)
    turtle.circle(50, 180)
    turtle.right(90)
    turtle.forward(100 * (percent_full / 100))
    turtle.end_fill()

# Initialisation de l'écran
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.title("Visualisation de l'Humidité")

# Désactiver les animations pour un dessin plus rapide
turtle.speed(0)
turtle.hideturtle()

while True:
    # Génération d'une valeur d'humidité aléatoire
    humidite = random.randint(0, 100)

    # Effacer le dessin précédent
    turtle.clear()

    # Dessiner la goutte d'eau avec l'humidité actuelle
    draw_droplet(0, 0, humidite)

    # Afficher l'humidité
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.write(f"Humidité: {humidite}%", align="center", font=("Arial", 16, "normal"))

    # Mettre en pause pour une seconde
    time.sleep(1)

# Garder la fenêtre ouverte
turtle.done()
