import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)
ax.set_xlim(0, np.pi)
ax.set_ylim(0, 1)

yaw = np.linspace(0, np.pi, 180)
distance = np.linspace(0, 1, 180) 
currentyaw = 0
anticlockwise = True

def update(frame):
    global currentyaw, vline
    vline.remove()
    currentyaw += np.deg2rad(2)
    vline = plt.axvline(currentyaw, color="black")
    return vline,

plt.bar(yaw, distance, 1)
vline = plt.axvline(currentyaw, color="black")
anim = animation.FuncAnimation(fig, update, interval=50)

plt.show()