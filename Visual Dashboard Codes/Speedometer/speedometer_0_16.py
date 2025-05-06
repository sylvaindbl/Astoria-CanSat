import matplotlib
import random
import math

# Access pi constant
pi_value = math.pi

print("Matplotlib Version : {}".format(matplotlib.__version__))

colors = [ "#f36d54", "#f6ee54", "#72c66e", "#f6ee54", "#f36d54"]

values = [16, 12, 11, 8, 4, 0]

x_axis_vals = [0, 0.78, 0.98, 1.57, 2.36]

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,5))

ax = fig.add_subplot(projection="polar")

ax.bar(x=[0, 0.78, 0.98, 1.57, 2.36], width=0.785, height=0.5, bottom=2,
       linewidth=3, edgecolor="white",
       color=colors, align="edge")



for loc, val in zip([0, 0.78, 0.98, 1.57, 2.36, pi_value], values):
    plt.annotate(val, xy=(loc, 2.5), ha="right" if val<=6 else "left");
plt.title("Performance Gauge Chart", loc="center", pad=10, fontsize=10, fontweight="bold")

ax.set_axis_off()


while True:
    myrandom = random.randint(0, 16*1000)/1000
    myrandom=round(myrandom,1)
#   myrandom = 100
    if myrandom <= 16:
        myposition = (16-myrandom)/16*pi_value
        plt.annotate(myrandom , xytext=(0,0), xy=( myposition , 2.0),
            arrowprops=dict(arrowstyle="wedge, tail_width=0.5", color="black", shrinkA=0),
            bbox=dict(boxstyle="circle", facecolor="black", linewidth=1.0, ),
             fontsize=25, color="white", ha="center"
            )
        plt.pause(1)
        plt.annotate(myrandom , xytext=(0,0), xy=( myposition , 2.0),
            arrowprops=dict(arrowstyle="wedge, tail_width=0.5", color="white", shrinkA=0),
            bbox=dict(boxstyle="circle", facecolor="black", linewidth=1.0, ),
             fontsize=25, color="white", ha="center"
            )
    else:
        plt.annotate(myrandom, xytext=(0, 0), xy=(1.666, 2.0),
                     bbox=dict(boxstyle="circle", facecolor="black", linewidth=1.0, ),
                     fontsize=25, color="white", ha="center"
                     )
        plt.pause(1)
