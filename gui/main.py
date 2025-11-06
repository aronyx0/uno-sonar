import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib.style as style
import matplotlib.colors as mplcolors
import tkinter as tk
from tkinter import ttk

import tester

testing = False
if not testing:
    monitor = serial.Serial("COM5")
buffer = ""
yawdist = {90: 100}
colormap = mplcolors.LinearSegmentedColormap.from_list("", ["firebrick","orange", "green","mediumblue"])

class ArduinoData:
    def __init__(self) -> None:
        self.update()

    def __str__(self) -> str:
        return f"({self.yaw}, {self.distance})"

    def update(self) -> None:
        if testing:
            datastr = tester.inputdata()
        else:
            datastr = monitor.readline().decode()
        datastr = eval(datastr)
        self.yaw = datastr[0]
        self.distance = datastr[1]

def graph_init(data: "ArduinoData") -> None:
    global fig, ax, theta_now, r_now, vline, graph, yawdist
    fig = plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, polar=True)
    ax.set_xlim(0, np.pi)
    ax.set_ylim(0, 300)

    theta_now = data.yaw
    r_now = data.distance
    vline = ax.axvline(theta_now, color="black")
    graph = ax.scatter([], [], color="green")

def animate(frame) -> tuple:
    global fig, data, yawdist, vline, graph, ax, colormap
    vline.remove()
    graph.remove()
    ax.set_xlim(0, np.pi)
    ax.set_ylim(0, 300)
    
    data.update()
    theta_now = data.yaw
    r_now = data.distance

    yawdist[theta_now] = r_now

    vline = ax.axvline(np.deg2rad(theta_now), color="black")
    graph = ax.scatter([np.deg2rad(item) for item in list(yawdist.keys())],
                       list(yawdist.values()),
                       s=6,
                       marker="x",
                       c=list(yawdist.values()),
                       cmap=colormap)
    return graph, vline

def render_window() -> None:
    root = tk.Tk()

if __name__ == "__main__":
    try:
        data = ArduinoData()
        graph_init(data)
        #graph_animate()
        style.use("fast")
        animation = anim.FuncAnimation(fig, animate, interval=10, cache_frame_data=False, blit=True)
        plt.show()
        
    except KeyboardInterrupt:
        plt.close()
        exit()