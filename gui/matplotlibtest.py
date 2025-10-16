import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)
ax.set_xlim(0, np.pi)
ax.set_ylim(0, 1)

yaw = [list(np.linspace(0, np.pi, 180)), list(np.linspace(np.pi, 0, 179))]
distance = np.linspace(0, 1, 180)
currentyaw = 0
anticlockwise = True

def update(frame):
    global currentyaw, vline()
    vline.remove()
    currentyaw += 180/np.pi
    vline = plt.axvline(currentyaw, color="black")

plt.bar(yaw, distance, 1, label="1")
vline = plt.axvline(currentyaw, color="black")
anim = animation.FuncAnimation(fig, update, interval=0)

plt.show()