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

graph = ax.bar(yaw, distance, 1)
vline = ax.axvline(currentyaw, color="black")
with open("gui/out.txt", "w") as file:
    file.write(str([str(item) for item in list(iter(graph))]))
with open("gui/out.txt", "r") as file:
    print(len(eval(file.read())))

plt.show()