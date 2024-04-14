import matplotlib.pyplot as plt
from matplotlib import image as mpimg
from matplotlib.patches import Rectangle
import random

# 0	    1170	-1	390	780	    -45	735
# 400	1170	0	390	1170	-45	1125
# 800	1170	1	390	1560	-45	1515
# 1200	1170	2	390	1950	-45	1905	1170


plt.gcf().set_facecolor('black')
w = 52  # largeur du rectangle
x = 45
# Fonction pour ajouter une image à une position spécifique

# Génération d'une valeur aléatoire initiale
random_value = random.randint(0, 1200)


def add_image_with_position(img_path: object, position: object, zorder: object = 0) -> object:
    img = mpimg.imread(img_path)
    image_object = plt.imshow(img, extent=(position[0], position[0] + img.shape[1], position[1], position[1] + img.shape[0]), zorder=zorder)
    return image_object


# Chargement de l'image de la jauge
img_path_background = r'media\altimeter_all.png'
add_image_with_position(img_path_background, (0, 0), zorder=1)

# Chargement de l'image atomium color
img_path_atomium_color = r'media\atomiumcolor.png'
atomium_color_position = (0, 0)  # Définissez la position de la tour Eiffel
atomium_color = add_image_with_position(img_path_atomium_color, atomium_color_position, zorder=0)

# Chargement de l'image Eiffel Tower color
img_path_eiffel_tower = r'media\eiffeltowercolorgut.png'
eiffel_tower_position = (0, 0)  # Définissez la position de la tour Eiffel
eiffel_tower = add_image_with_position(img_path_eiffel_tower, eiffel_tower_position, zorder=0)

# Chargement de l'image Burj Khalifa color
img_path_burj_khalifa = r'media\burjkhalifacolorgut.png'
burj_khalifa_position = (0, 0)  # Définissez la position de la tour Burj Khalifa
burj_khalifa = add_image_with_position(img_path_burj_khalifa, burj_khalifa_position, zorder=0)

# Chargement de l'image cansat black color
img_path_can_black_icon = r'media\can_black_icon.png'
can_black_icon_position = (200, 300 )  # Définissez la position
can_black_icon = add_image_with_position(img_path_can_black_icon, can_black_icon_position, zorder=3)

# Réglez la limite des axes pour s'adapter aux images
plt.xlim(-1, 1250)
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

# Calcul de la position du rectangle
rectangle_x_position = 502  # Position x du rectangle
rectangle_y_position = graduations_positions['1200'][1]  # Base du rectangle au sommet de l'image

# Hauteur du rectangle pour pointer la bonne graduation
rectangle_height = graduation_distance * abs(random_value - 1200)


# Ajout du rectangle initial
rectangle = Rectangle((rectangle_x_position, rectangle_y_position), w, rectangle_height, color='black', alpha=1, zorder=1)
plt.gca().add_patch(rectangle)

# Affichage de la valeur aléatoire à une position fixe
random_text = plt.text(-200, 1250, f'{random_value}m', fontsize=15, ha='left', va='top', color='white')

# Mise à jour de la valeur aléatoire chaque seconde
while True:
    if can_black_icon :
        can_black_icon.remove()
    if atomium_color :
        atomium_color.remove()
    if eiffel_tower :
        eiffel_tower.remove()
    if burj_khalifa :
        burj_khalifa.remove()
    random_value = random.randint(0, 1200)
    if random_value < 102:
        a = 0
        e = 0
        b = 0
    else:
        if random_value < 330:
            a = 1
            e = 0
            b = 0
        else:
            if random_value < 830:
                a = 1
                e = 1
                b = 0
            else:
                a = 1
                e = 1
                b = 1
    atomium_color = add_image_with_position(img_path_atomium_color, atomium_color_position, zorder=a)
    eiffel_tower = add_image_with_position(img_path_eiffel_tower, eiffel_tower_position, zorder=e)
    burj_khalifa = add_image_with_position(img_path_burj_khalifa, burj_khalifa_position, zorder=b)
    rectangle_height = graduation_distance * abs(random_value - 1200)
    rectangle_height = (-(1200-random_value) / 1200 * 1170)
    rectangle.set_height(rectangle_height)

    can_black_icon_position = (100, 1810 + rectangle_height)  # Définissez la position
    can_black_icon = add_image_with_position(img_path_can_black_icon, can_black_icon_position, zorder=3)

    random_text.set_text(f'{random_value}m')
    plt.pause(1)