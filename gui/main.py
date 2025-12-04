import serial
import serial.tools.list_ports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib.style as style
import matplotlib.colors as mplcolors
import matplotlib.backends.backend_tkagg as mpl_backend
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pathlib
import os

import tester

yawdist = {0: 0}
colormap = mplcolors.LinearSegmentedColormap.from_list("", ["firebrick","orange", "green","mediumblue"])

class ArduinoData:
    def __init__(self, testing: bool = False, comport: str = "COM1") -> None:
        self.testing = testing
        self.comport = comport
        self.update()

    def __str__(self) -> str:
        return f"({self.yaw}, {self.distance}) @ COM{self.comport}"

    def update(self) -> None:
        if self.testing:
            datastr = tester.inputdata()
        else:
            monitor = serial.Serial(self.comport, 115200, timeout=5)
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

    data.update()
    if data.distance >= 300:
        return graph, vline

    theta_now = data.yaw
    r_now = data.distance

    try:
        if 'vline' in globals() and vline is not None and vline in ax.lines:
            vline.remove()
    except Exception:
        pass
    try:
        if 'graph' in globals() and graph is not None and graph in ax.collections:
            graph.remove()
    except Exception:
        pass
    ax.set_xlim(0, np.pi)
    ax.set_ylim(0, 300)
    
    

    yawdist[theta_now] = r_now

    vline = ax.axvline(np.deg2rad(theta_now), color="black")
    graph = ax.scatter([np.deg2rad(item) for item in list(yawdist.keys())],
                       list(yawdist.values()),
                       s=6,
                       marker="x",
                       c=list(yawdist.values()),
                       cmap=colormap)
    return graph, vline

def start_graph(data: "ArduinoData") -> None:
    global root, fig, vline, r_now, theta_now, graph, animation
    graph_init(data)
    canvas = mpl_backend.FigureCanvasTkAgg(fig, root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    graph_init_p2()
    theta_now = data.yaw
    r_now = data.distance
    vline = ax.axvline(np.deg2rad(theta_now), color="black")
    graph = ax.scatter([], [], color="green")
    style.use("fast")

def render_graph_window() -> None:
    global root
    root = tk.Tk()
    width = 768
    height = 576
    root.minsize(width, height)

    comport_menu_button = ttk.Menubutton(root, text="Choose a COM port")
    comport_menu = tk.Menu(comport_menu_button, tearoff=False)
    comports = serial.tools.list_ports.comports()
    chosen_port = tk.StringVar(root)
    chosen_port.set("Testing")

    def update_label(*args):
        comport_menu_button.config(text=chosen_port.get())

    chosen_port.trace_add("write", update_label)
    for port in comports:
        comport_menu.add_radiobutton(label=port.description, value=port.device, variable=chosen_port)
    comport_menu.add_radiobutton(label="Testing mode", value="Testing", variable=chosen_port)
    comport_menu_button["menu"] = comport_menu
    comport_menu_button.pack()
        
    """label = ttk.Label(root, text="None chosen")
    test_button = ttk.Button(root, text="test", command=lambda: update_label(chosen_port, comport_menu_button))
    test_button.pack()
    label.pack()"""

    def forget_ui(*args: tk.Widget) -> None:
        for arg in args:
            arg.pack_forget()       

    def start_button_func(comport: str) -> None:
        global data, animation
        if comport == "Testing":
            data = ArduinoData(True)
        else:
            data = ArduinoData(False, comport)
        start_graph(data)
        update_label()
        animation = anim.FuncAnimation(fig, animate, interval=20, cache_frame_data=False, blit=True)

    start_button = ttk.Button(root, text="Start", command=lambda: [start_button_func(chosen_port.get()), forget_ui(comport_menu, comport_menu_button, start_button)])
    start_button.pack()

    root.title("Arduino Uno Sonar")
    current_dir = pathlib.Path(__file__).parent.resolve() # current directory
    img_path = os.path.join(current_dir, "icon.ico")
    root.iconbitmap(img_path)
    root.protocol("WM_DELETE_WINDOW", lambda: [root.destroy(), exit()])
    root.report_callback_exception = lambda exc, val, tb: messagebox.showerror("An error occured", str(val))
    root.mainloop()

if __name__ == "__main__":
    try:
        render_graph_window()
    except KeyboardInterrupt:
        root.destroy()
        exit()
    except Exception as e:
        messagebox.showerror("An error occured", str(e))