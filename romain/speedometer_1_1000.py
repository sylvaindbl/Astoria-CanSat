import matplotlib
import random
import math

print("Matplotlib Version : {}".format(matplotlib.__version__))

colors = ["#72c66e", "#f6ee54", "#f36d54"]

values = [1000, 100, 10, 1]

x_axis_vals = [0, 1.05, 2.09]

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5, 5))

ax = fig.add_subplot(projection="polar")

ax.bar(x=[0, 1.05, 2.09], width=1.05, height=0.5, bottom=2,
       linewidth=3, edgecolor="white",
       color=colors, align="edge")

for loc, val in zip([0, 1.05, 2.09, 3.14], values):
    plt.annotate(val, xy=(loc, 2.5), ha="right" if val <= 50 else "left")

plt.title("Speedometer Log(speed)", loc="center", pad=10, fontsize=10, fontweight="bold")

ax.set_axis_off()

while True:
    myrandom = random.randint(1, 1000)
 #   myrandom=round(myrandom,0)
    myposition = (3 - math.log(myrandom, 10)) / 3 * 3.14
    plt.annotate(myrandom, xytext=(0, 0), xy=(myposition, 2.0),
                 arrowprops=dict(arrowstyle="wedge, tail_width=0.5", color="black", shrinkA=0),
                 bbox=dict(boxstyle="circle", facecolor="black", linewidth=1.0, ),
                 fontsize=25, color="white", ha="center"
                 )

    plt.pause(1)  # Pause for 1 second
    plt.annotate(myrandom, xytext=(0, 0), xy=(myposition, 2.0),
                 arrowprops=dict(arrowstyle="wedge, tail_width=0.5", color="white", shrinkA=0),
                 bbox=dict(boxstyle="circle", facecolor="black", linewidth=1.0, ),
                 fontsize=25, color="white", ha="center"
                 )

