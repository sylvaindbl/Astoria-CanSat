import matplotlib.pyplot as plt
from matplotlib import image as mpimg
from matplotlib.patches import Rectangle
import random

plt.gcf().set_facecolor('black')

max_value = 7000

# Fonction pour ajouter une image à une position spécifique
def add_image_with_position(img_path, position, scale=1.0, zorder=0):
    img = mpimg.imread(img_path)
    img_width = img.shape[1] * scale
    img_height = img.shape[0] * scale
    # Calculez les nouvelles coordonnées de l'extent pour garder le centre de l'image fixe
    new_extent = (position[0] - img_width / 2, position[0] + img_width / 2, position[1] - img_height / 2,
                  position[1] + img_height / 2)
    image_object = plt.imshow(img, extent=new_extent, zorder=zorder)
    return image_object


# Chargement de l'image de la light_bulb_grey
img_path_background = r'media/light_bulb_grey.png'
background_shape = add_image_with_position(img_path_background, (301, 285), zorder=0)

# Chargement de l'image sun_transparent color
img_path_sun_transparent = r'media/sun_transparent.png'
sun_transparent_position = (300, 400)  # Définissez la position de la tour Eiffel
sun_transparent_image = add_image_with_position(img_path_sun_transparent, sun_transparent_position, scale=1.0, zorder=1)

# Chargement de light_buble_transparent color
img_path_light_bulb_grey = r'media/light_bulb_white_black.png'
burj_khalifa_position = (301, 285)  # Définissez la position de la tour Burj Khalifa
light_bulb_image = add_image_with_position(img_path_light_bulb_grey, burj_khalifa_position, zorder=2)

# Réglez la limite des axes pour s'adapter aux images
plt.xlim(-100, 700)
plt.ylim(0, 800)

# Désactivez les axes et affichez uniquement les images
plt.axis('off')

# Sauvegardez la disposition des images dans un fichier sans afficher le graphique
plt.savefig('layout.png', bbox_inches='tight', pad_inches=0)

# Text annotation for light value
light_text = plt.text(330, 400, '', ha='center', va='center', fontsize=24, color='white', fontfamily='Bebas Neue')


# Function to format light intensity value
def format_light_value(value):
    if value >= 1000:
        return '{:.1f} klux'.format(value / 1000)
    elif value >= 1:
        return '{:.1f} lux'.format(value)
    elif value >= 0.001:
        return '{:.1f} mlx'.format(value * 1000)
    elif value >= 0.000001:
        return '{:.1f} µlux'.format(value * 1000000)


# Mise à jour de la valeur aléatoire chaque seconde
while True:
    random_value = random.randint(0, max_value)
    x = random_value / max_value
    light_text.set_text(format_light_value(random_value))

    # Supprimer l'image sun_transparent et light_bulb précédente si elles existent
    if sun_transparent_image:
        sun_transparent_image.remove()
    if light_bulb_image:
        light_bulb_image.remove()

    # Ajouter la nouvelle image et mettre à jour les références
    sun_transparent_image = add_image_with_position(img_path_sun_transparent, sun_transparent_position, scale=x,
                                                    zorder=1)
    light_bulb_image = add_image_with_position(img_path_light_bulb_grey, burj_khalifa_position, zorder=2)

    plt.pause(1)
