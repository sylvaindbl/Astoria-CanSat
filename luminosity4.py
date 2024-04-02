import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Generate light data (circular)
theta = np.linspace(0, 2*np.pi, 100)
r = np.ones_like(theta)
light_intensity = np.sin(theta)  # Example light data, replace with your own
min_intensity = 0.01  # Minimum light intensity (188 ulux)
max_intensity = 10000 # Maximum light intensity (88000 lux)


fig, ax = plt.subplots(figsize=(6, 6))
plt.gca().set_aspect('equal', adjustable='box')
fig.patch.set_facecolor('green')

# Plot the background circle
circle_background = plt.Circle((0.5, 0.5), 0.4, color='darkgrey', alpha=1)
ax.add_artist(circle_background)

# Plot the light circle
light_circle = plt.Circle((0.5, 0.5), 0.4, color='yellow', alpha=1)
ax.add_artist(light_circle)

# Set axis limits to ensure circular shape
ax.set_xlim(0.1, 0.9)
ax.set_ylim(0.1, 0.9)

# Hide axes for a cleaner look
ax.axis('off')

# Text annotation for light value
light_text = ax.text(0.5, 0.5, '', ha='center', va='center', fontsize=42, color='black', fontfamily='Bebas Neue')

# Function to format light intensity value
def format_light_value(value):
    if value >= 1000:
        return '{:.1f} klux'.format(value / 1000)
    elif value >= 1:
        return '{:.1f} lux'.format(value)
    elif value >= 0.001:
        return '{:.1f} mlx'.format(value * 1000)
    elif value >=0.000001:
        return '{:.1f} µlux'.format(value * 1000000)

# Update the size of the light circle based on light intensity
def update_light(i):
    light_value = np.random.uniform(min_intensity, max_intensity)  # Randomly generate light value within range
    light_text.set_text(format_light_value(light_value))
    # Adjust circle radius based on random light intensity, ensuring it doesn't exceed the maximum value
    circle_radius = min(0.4 * (light_value - min_intensity) / (max_intensity - min_intensity), 0.4)
    light_circle.set_radius(circle_radius)
    return light_circle, light_text

# Animate the plot with an interval of 1 second (1000 milliseconds)
ani = animation.FuncAnimation(fig, update_light, frames=len(theta), interval=1000, blit=True)

# Show the plot
plt.show()
