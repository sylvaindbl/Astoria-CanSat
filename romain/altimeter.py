import matplotlib.pyplot as plt
from matplotlib import image as mpimg
from matplotlib.patches import Rectangle
import random

w = 30  # largeur du rectangle

# Fonction pour ajouter une image à une position spécifique
import matplotlib.pyplot as plt
from matplotlib import image as mpimg
from matplotlib.patches import Rectangle
import random

w = 30  # largeur du rectangle

# Fonction pour ajouter une image à une position spécifique
def add_image_with_position(img_path, position, zorder=0):
    img = mpimg.imread(img_path)
    plt.imshow(img, extent=(position[0], position[0] + img.shape[1], position[1], position[1] + img.shape[0]), zorder=zorder)
    return img.shape

# Chargement de l'image de la jauge
img_path_background = r'D:\Users\romain\Documents\Cansat\images\Altimeterhauteurbarplusblackall.png'
background_shape = add_image_with_position(img_path_background, (0, 0), zorder=0)

# Chargement de l'image Eiffel Tower color
img_path_eiffel_tower = r'D:\Users\romain\Documents\Cansat\images\Altimetereiffelcolor.png'
eiffel_tower_position = (284.5, 0)  # Définissez la position de la tour Eiffel
add_image_with_position(img_path_eiffel_tower, eiffel_tower_position, zorder=1)

# Chargement de l'image Burj Khalifa color
img_path_burj_khalifa = r'D:\Users\romain\Documents\Cansat\images\Altimeterkhalifacolor.png'
burj_khalifa_position = (0, 0)  # Définissez la position de la tour Burj Khalifa
add_image_with_position(img_path_burj_khalifa, burj_khalifa_position, zorder=1)

# Réglez la limite des axes pour s'adapter aux images
plt.xlim(0, 750)
plt.ylim(0, 750)

# Désactivez les axes et affichez uniquement les images
plt.axis('off')

# Sauvegardez la disposition des images dans un fichier sans afficher le graphique
plt.savefig('layout.png', bbox_inches='tight', pad_inches=0)

# Nombre de graduations entre 0 et 1200
num_graduations = 1200

# Graduations à afficher
graduations_a_afficher = ['0', '400', '800', '1200']

# Positionnement des graduations
graduation_distance = 600 / num_graduations  # Distance verticale totale est de 600
graduations_positions = {'0': (350, 0)}  # Inversion de la position de la graduation 0

for i in range(1, num_graduations + 1):
    graduation_value = i * 1200 // num_graduations
    graduations_positions[str(graduation_value)] = (350, i * graduation_distance)  # Inversion de l'ordre


# Ajout des graduations sur le graphique
for graduation in graduations_a_afficher:
    position = graduations_positions[graduation]
    plt.text(position[0], position[1], f'{graduation}m', fontsize=8, ha='center', va='center', color='black')

# Génération d'une valeur aléatoire initiale
random_value = random.randint(0, 1200)

# Calcul de la position du rectangle
rectangle_x_position = 245  # Position x du rectangle
rectangle_y_position = graduations_positions['1200'][1]  # Base du rectangle au sommet de l'image

# Hauteur du rectangle pour pointer la bonne graduation
rectangle_height = graduation_distance * abs(random_value - 1200)

# Ajout du rectangle initial
rectangle = Rectangle((rectangle_x_position, rectangle_y_position), w, rectangle_height, color='black', alpha=1, zorder=1)
plt.gca().add_patch(rectangle)

# Affichage de la valeur aléatoire à une position fixe
random_text = plt.text(150, 500, f'{random_value}m', fontsize=15, ha='left', va='top', color='black')

# Mise à jour de la valeur aléatoire chaque seconde
while True:
    random_value = random.randint(0, 1200)
    rectangle_height = graduation_distance * abs(random_value - 1200)
    rectangle.set_height(rectangle_height)
    random_text.set_text(f'{random_value}m')
    plt.pause(1)


# Chargement de l'image de la jauge
img_path_background = r'D:\Users\romain\Documents\Cansat\images\Altimeterhauteurbarplusblackall.png'
background_shape = add_image_with_position(img_path_background, (0, 0), zorder=0)

# Chargement de l'image Eiffel Tower color
img_path_eiffel_tower = r'D:\Users\romain\Documents\Cansat\images\Altimeterhauteureiffeltowercolor.png'
eiffel_tower_position = (200, 200)  # Définissez la position de la tour Eiffel
add_image_with_position(img_path_eiffel_tower, eiffel_tower_position, zorder=1)

# Chargement de l'image Burj Khalifa color
img_path_burj_khalifa = r'D:\Users\romain\Documents\Cansat\images\Altimeterhauteurburjkhalifacolor.png'
burj_khalifa_position = (250, 250)  # Définissez la position de la tour Burj Khalifa
add_image_with_position(img_path_burj_khalifa, burj_khalifa_position, zorder=1)

# Réglez la limite des axes pour s'adapter aux images
plt.xlim(0, 800)
plt.ylim(0, 800)

# Désactivez les axes et affichez uniquement les images
plt.axis('off')

# Sauvegardez la disposition des images dans un fichier sans afficher le graphique
plt.savefig('layout.png', bbox_inches='tight', pad_inches=0)

# Nombre de graduations entre 0 et 1200
num_graduations = 1200

# Graduations à afficher
graduations_a_afficher = ['0', '400', '800', '1200']

# Positionnement des graduations
graduation_distance = 600 / num_graduations  # Distance verticale totale est de 600
graduations_positions = {'0': (350, 0)}  # Inversion de la position de la graduation 0

for i in range(1, num_graduations + 1):
    graduation_value = i * 1200 // num_graduations
    graduations_positions[str(graduation_value)] = (350, i * graduation_distance)  # Inversion de l'ordre


# Ajout des graduations sur le graphique
for graduation in graduations_a_afficher:
    position = graduations_positions[graduation]
    plt.text(position[0], position[1], f'{graduation}m', fontsize=8, ha='center', va='center', color='black')

# Génération d'une valeur aléatoire initiale
random_value = random.randint(0, 1200)

# Calcul de la position du rectangle
rectangle_x_position = 245  # Position x du rectangle
rectangle_y_position = graduations_positions['1200'][1]  # Base du rectangle au sommet de l'image

# Hauteur du rectangle pour pointer la bonne graduation
rectangle_height = graduation_distance * abs(random_value - 1200)

# Ajout du rectangle initial
rectangle = Rectangle((rectangle_x_position, rectangle_y_position), w, rectangle_height, color='black', alpha=1, zorder=1)
plt.gca().add_patch(rectangle)

# Affichage de la valeur aléatoire à une position fixe
random_text = plt.text(150, 500, f'{random_value}m', fontsize=15, ha='left', va='top', color='black')

# Mise à jour de la valeur aléatoire chaque seconde
while True:
    random_value = random.randint(0, 1200)
    rectangle_height = graduation_distance * abs(random_value - 1200)
    rectangle.set_height(rectangle_height)
    random_text.set_text(f'{random_value}m')
    plt.pause(1)