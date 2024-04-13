import matplotlib.pyplot as plt
from matplotlib import image as mpimg
from matplotlib.patches import Rectangle
import random

def add_image_with_positions(img_path, img_positions, zorder=0):
    img = mpimg.imread(img_path)
    plt.imshow(img, zorder=zorder)
    plt.axis('off')
    for label, position in img_positions.items():
        plt.text(position[0], position[1], label, fontsize=10, ha='center', va='center', color='white')
    return img.shape

# Chargement de l'image du contour
img_path_background = r'media/amazingcontourpluswhite.png'
background_shape = add_image_with_positions(img_path_background, {}, zorder=2)

# Chargement de l'image du jauge
img_path_foreground = r'media/amazingjauge.png'
foreground_shape = add_image_with_positions(img_path_foreground, {}, zorder=0)

# Nombre de graduations entre 0 et 25
num_graduations = 25

# Positionnement des graduations
graduations_positions = {'0°C': (210, 432), '25°C': (200, 0)}

# Calcul de la distance verticale entre chaque graduation
graduation_distance = (graduations_positions['0°C'][1] - graduations_positions['25°C'][1]) / num_graduations

# Ajout des autres graduations
for i in range(1, num_graduations):
    graduation_value = i
    graduation_y = graduations_positions['0°C'][1] - i * graduation_distance
    graduations_positions[f'{graduation_value}°C'] = (210, graduation_y)

# Ajout des graduations sur le graphique
for graduation, position in graduations_positions.items():
    if graduation in ['0°C', '5°C', '10°C', '15°C', '20°C', '25°C']:
        plt.text(position[0], position[1], graduation, fontsize=15, ha='center', va='center', color='black')

# Génération d'une valeur aléatoire initiale
random_value = random.randint(0, 25)

# Calcul de la position du rectangle
rectangle_x_position = -25  # Position x du rectangle
rectangle_y_position = graduations_positions['25°C'][1]  # Base du rectangle au sommet de l'image

# Hauteur du rectangle pour pointer la bonne graduation
rectangle_height = graduation_distance * abs(random_value - 25)

# Ajout du rectangle initial
rectangle = Rectangle((rectangle_x_position, rectangle_y_position), 300, rectangle_height, color='black', alpha=1, zorder=1)
plt.gca().add_patch(rectangle)

# Affichage de la valeur aléatoire à une position fixe
random_text = plt.text(36.5, 480, f'{random_value}°C', fontsize=25, ha='left', va='top', color='white')

# Mise à jour de la valeur aléatoire chaque seconde
while True:
    random_value = random.randint(0, 25)
    rectangle_height = graduation_distance * abs(random_value - 25)
    rectangle.set_height(rectangle_height)
    random_text.set_text(f'{random_value}°C')
    plt.pause(1)
