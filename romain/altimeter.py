import matplotlib.pyplot as plt
from matplotlib import image as mpimg
from matplotlib.patches import Rectangle
import random

plt.gcf().set_facecolor('black')
w = 52  # largeur du rectangle
x = 45
# Fonction pour ajouter une image à une position spécifique
def add_image_with_position(img_path, position, zorder=0):
    img = mpimg.imread(img_path)
    plt.imshow(img, extent=(position[0], position[0] + img.shape[1], position[1], position[1] + img.shape[0]), zorder=zorder)
    return img.shape

# Chargement de l'image de la jauge
img_path_background = r'media\altimeter_all.png'
background_shape = add_image_with_position(img_path_background, (0, 0), zorder=0)

# Chargement de l'image atomium color
img_path_eiffel_tower = r'media\atomiumcolor.png'
eiffel_tower_position = (0, 0)  # Définissez la position de la tour Eiffel
add_image_with_position(img_path_eiffel_tower, eiffel_tower_position, zorder=3)

# Chargement de l'image Eiffel Tower color
img_path_eiffel_tower = r'media\eiffeltowercolorgut.png'
eiffel_tower_position = (0, 0)  # Définissez la position de la tour Eiffel
add_image_with_position(img_path_eiffel_tower, eiffel_tower_position, zorder=2)

# Chargement de l'image Burj Khalifa color
img_path_burj_khalifa = r'media\burjkhalifacolorgut.png'
burj_khalifa_position = (0, 0)  # Définissez la position de la tour Burj Khalifa
add_image_with_position(img_path_burj_khalifa, burj_khalifa_position, zorder=1)

# Réglez la limite des axes pour s'adapter aux images
plt.xlim(200, 1250)
plt.ylim(450, 2000)

# Désactivez les axes et affichez uniquement les images
plt.axis('off')

# Sauvegardez la disposition des images dans un fichier sans afficher le graphique
plt.savefig('layout.png', bbox_inches='tight', pad_inches=0)

# Nombre de graduations entre 0 et 1200
num_graduations = 1200

# Graduations à afficher
graduations_a_afficher = ['0', '400', '800', '1200']

# Position de la graduation 1200
graduation_1200_position = (400, 1170)

# Distance entre chaque graduation
graduation_distance = (graduation_1200_position[1] ) / 3

# Positionnement des autres graduations
graduations_positions = {
    '0': (graduation_1200_position[0], graduation_1200_position[1]    - graduation_distance     - x),
    '400': (graduation_1200_position[0], graduation_1200_position[1]                            - x),
    '800': (graduation_1200_position[0], graduation_1200_position[1]  + graduation_distance     - x),
    '1200': (graduation_1200_position[0], graduation_1200_position[1] + 2 * graduation_distance - x)
}

# Ajout des graduations sur le graphique
for graduation in graduations_a_afficher:
    position = graduations_positions[graduation]
    plt.text(position[0], position[1], f'{graduation}m', fontsize=8, ha='center', va='center', color='white')

# Génération d'une valeur aléatoire initiale
random_value = random.randint(0, 1200)

# Calcul de la position du rectangle
rectangle_x_position = 502  # Position x du rectangle
rectangle_y_position = graduations_positions['1200'][1]  # Base du rectangle au sommet de l'image

# Hauteur du rectangle pour pointer la bonne graduation
rectangle_height = graduation_distance * abs(random_value - 1200)


# Ajout du rectangle initial
rectangle = Rectangle((rectangle_x_position, rectangle_y_position), w, rectangle_height, color='black', alpha=1, zorder=1)
plt.gca().add_patch(rectangle)

# Affichage de la valeur aléatoire à une position fixe
random_text = plt.text(150, 900, f'{random_value}m', fontsize=15, ha='left', va='top', color='white')

# Mise à jour de la valeur aléatoire chaque seconde
while True:
    random_value = random.randint(0, 1200)
    rectangle_height = graduation_distance * abs(random_value - 1200)
    rectangle_height = (-(1200-random_value) / 1200 * 1170)
    rectangle.set_height(rectangle_height)
    random_text.set_text(f'{random_value}m')
    plt.pause(1)