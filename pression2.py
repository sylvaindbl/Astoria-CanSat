import pygame
import os
import random
import time

# Initialisation de pygame
pygame.init()

# Définir la taille de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Ballon")

# Charger l'image du ballon
ballon_image = pygame.image.load("C:\\Users\\Home\\Documents\\redis\\balloon.jpg")

# Obtenir la taille initiale de l'image
ballon_rect = ballon_image.get_rect()

# Couleur verte
VERT = (0, 128, 0)

# Charger une police de caractères
font = pygame.font.Font(None, 36)

# Boucle de jeu
continuer = True
horloge = pygame.time.Clock()

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    pression = random.randint(1, 75)
    taille = (ballon_rect.width * pression/50, ballon_rect.height * pression/50)
    ballon = pygame.transform.scale(ballon_image, taille)

    fenetre.fill(VERT)

    fenetre.blit(ballon, (largeur // 2 - taille[0] // 2, hauteur // 2 - taille[1] // 2))

    # Créer une surface de texte avec la valeur de pression
    texte = font.render(f"Pression : {pression}", True, (255, 255, 255))
    # Afficher le texte sous le graphique
    fenetre.blit(texte, (10, hauteur - 50))

    pygame.display.flip()

    time.sleep(0.5)

pygame.quit()
