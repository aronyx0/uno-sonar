import serial
import serial.tools.list_ports
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib.style as style
import matplotlib.colors as mplcolors
import matplotlib.backends.backend_tkagg as mpl_backend
import tkinter as tk
from tkinter import ttk

import tester

testing = True
if not testing:
    monitor = serial.Serial("COM5")
buffer = ""
yawdist = {90: 100}
colormap = mplcolors.LinearSegmentedColormap.from_list("", ["firebrick","orange", "green","mediumblue"])

class ArduinoData:
    def __init__(self, testing: bool = False, comport: str = None) -> None:
        self.testing = testing
        self.comport = comport
        self.update()

    def __str__(self) -> str:
        return f"({self.yaw}, {self.distance}) @ COM{self.comport}"

    def update(self) -> None:
        if testing:
            datastr = tester.inputdata()
        else:
            datastr = monitor.readline().decode()
        datastr = eval(datastr)
        self.yaw = datastr[0]
        self.distance = datastr[1]

def graph_init(data: "ArduinoData") -> None:
    global fig
    fig = plt.figure(figsize=(8, 6))

def graph_init_p2() -> None:
    global fig, ax, theta_now, r_now, vline, graph, yawdist
    ax = plt.subplot(111, polar=True)
    ax.set_xlim(0, np.pi)
    ax.set_ylim(0, 300)

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

def start_graph() -> None:
    global data, root, fig, vline, r_now, theta_now, graph, animation
    data = ArduinoData()
    graph_init(data)
    canvas = mpl_backend.FigureCanvasTkAgg(fig, root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    graph_init_p2()
    theta_now = data.yaw
    r_now = data.distance
    vline = ax.axvline(theta_now, color="black")
    graph = ax.scatter([], [], color="green")
    style.use("fast")
    animation = anim.FuncAnimation(fig, animate, interval=10, cache_frame_data=False, blit=True)

def render_graph_window() -> None:
    global root
    root = tk.Tk()
    width = 768
    height = 576
    root.minsize(width, height)

    comport_menu = tk.Listbox(root)
    comports = serial.tools.list_ports.comports()
    for port in comports:
        comport_menu.insert("end", port)
    comport_menu.pack()
    print(comports)

    start_button = ttk.Button(root, text="Start", command=lambda: [start_graph(), start_button.pack_forget()])
    start_button.pack()

    root.protocol("WM_DELETE_WINDOW", lambda: [root.destroy(), exit()])
    root.mainloop()

if __name__ == "__main__":
    try:
        render_graph_window()
    except KeyboardInterrupt:
        root.destroy()
        exit()

    """try:
        data = ArduinoData()
        graph_init(data)
        #graph_animate()
        style.use("fast")
        animation = anim.FuncAnimation(fig, animate, interval=10, cache_frame_data=False, blit=True)
        plt.show()
        
    except KeyboardInterrupt:
        plt.close()
        exit()"""