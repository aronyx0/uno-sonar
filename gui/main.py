import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import time
import tester

testing = False
monitor = serial.Serial("COM3")
buffer = ""

def last_serial_line():
    global buffer, monitor
    buffer += str(monitor.read(monitor.in_waiting))
    if "\n" in buffer:
        lines = buffer.split("\n")
        buffer = lines[-1]
        return lines[-2]
    else:
        return buffer

class ArduinoData:
    def __init__(self) -> None:
        self.update()

    def __str__(self) -> str:
        return f"({self.yaw}, {self.distance})"

    def update(self) -> None:
        if testing:
            datastr = tester.inputdata()
        else:
            time.sleep(1)
            datastr = str(eval(last_serial_line()))
        datastr = eval(datastr)
        self.yaw = datastr[0]
        self.distance = datastr[1]

def graph_init(data: "ArduinoData") -> None:
    global fig, ax, theta, theta_now, r, r_now, vline, graph
    fig = plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, polar=True)
    ax.set_xlim(0, np.pi)
    ax.set_ylim(0, 200)
    
    theta = list(range(0, 181))
    r = list(range(0, 181))
    theta_now = data.yaw
    r_now = data.distance
    vline = plt.axvline(theta_now, color="black")
    graph = plt.bar(np.deg2rad(theta), r, np.deg2rad(1), color="green")

def graph_animate():
    global fig, animation
    def update(frame) -> tuple:
        global theta_now, r, vline, graph, data
        data.update()
        vline.remove()
        graph.remove()

        theta_now = np.deg2rad(data.yaw)
        r_now = data.distance
        r[data.yaw] = r_now

        vline = plt.axvline(theta_now, color="black")
        graph = plt.bar(np.deg2rad(theta), r, np.deg2rad(1), color="green")
        return vline, graph

    animation = anim.FuncAnimation(fig, update, interval=20, cache_frame_data=False)

if __name__ == "__main__":
    data = ArduinoData()
    graph_init(data)
    graph_animate()
    plt.show()