import matplotlib.pyplot as plt
from matplotlib import image as mpimg
from matplotlib.patches import Rectangle
import random

plt.gcf().set_facecolor('black')

rectangle_width = 420

def add_image_with_positions(img_path, img_positions, x=0, y=0, zorder=0):
    img = mpimg.imread(img_path)
    plt.imshow(img, extent=[x, x + img.shape[1], y, y + img.shape[0]], zorder=zorder)
    plt.axis('off')
    for label, position in img_positions.items():
        plt.text(position[0], position[1], label, fontsize=10, ha='center', va='center', color='white')
    return img.shape

# Chargement de l'image du contour
img_path_background = r'media/humiditywaterdropcontourfinblack.png'
background_shape = add_image_with_positions(img_path_background, {}, x=-15, y=0, zorder=2)

# Chargement de l'image du jauge
img_path_foreground = r'media/humidityjauge.png'
foreground_shape = add_image_with_positions(img_path_foreground, {}, x=-2, y=13.5, zorder=0)

# Réglez la limite des axes pour s'adapter aux images
plt.xlim(-100, 700)
plt.ylim(0, 800)

# Désactivez les axes et affichez uniquement les images
plt.axis('off')

# Sauvegardez la disposition des images dans un fichier sans afficher le graphique
plt.savefig('layout.png', bbox_inches='tight', pad_inches=0)

# Nombre de graduations entre 0 et 100
num_graduations = 100

# Graduations à afficher
graduations_a_afficher = ['0', '20', '40', '60', '80', '100']

# Positionnement des graduations
graduations_positions = {'0%': (500, 10), '100%': (500, 575)}

# Calcul de la distance verticale entre chaque graduation
graduation_distance = (graduations_positions['0%'][1] - graduations_positions['100%'][1]) / num_graduations

# Ajout des autres graduations à afficher
for graduation in graduations_a_afficher:
    if graduation != '100':
        position_y = graduations_positions['0%'][1] - int(graduation) * graduation_distance
        graduations_positions[f'{graduation}'] = (graduations_positions['0%'][0], position_y)
    else:
        graduations_positions['100'] = (graduations_positions['100%'][0], graduations_positions['100%'][1])

# Ajout des graduations sur le graphique
for graduation in graduations_a_afficher:
    position = graduations_positions[graduation]
    plt.text(position[0], position[1], f'{graduation}%', fontsize=15, ha='center', va='center', color='black')



# Génération d'une valeur aléatoire initiale
random_value = random.randint(0, 100)

# Calcul de la position du rectangle
rectangle_x_position = -50  # Position x du rectangle
rectangle_y_position = graduations_positions['100%'][1]  # Base du rectangle au sommet de l'image

# Hauteur du rectangle pour pointer la bonne graduation
rectangle_height = graduation_distance * abs(random_value - 100)

# Ajout du rectangle initial
rectangle = Rectangle((rectangle_x_position, rectangle_y_position), rectangle_width, rectangle_height, color='black', alpha=1, zorder=0)
plt.gca().add_patch(rectangle)

# Affichage de la valeur aléatoire à une position fixe
random_text = plt.text(40, 190, f'{random_value}%', fontsize=30, ha='left', va='top', color='white')

# Mise à jour de la valeur aléatoire chaque seconde
while True:
    random_value = 56.0
    rectangle_height = graduation_distance * abs(random_value - 100)
    rectangle.set_height(rectangle_height)
    random_text.set_text(f'{random_value}%')
    plt.pause(1)