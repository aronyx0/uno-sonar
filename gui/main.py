import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib.style as style
import time
import tester

testing = True
if not testing:
    monitor = serial.Serial("COM5")
buffer = ""
yawdist = {90: 100}

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
            datastr = str(eval(last_serial_line()))
        datastr = eval(datastr)
        self.yaw = datastr[0]
        self.distance = datastr[1]

def graph_init(data: "ArduinoData") -> None:
    global fig, ax, theta, theta_now, r, r_now, vline, graph
    fig = plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, polar=True)
    ax.set_xlim(0, np.pi)
    ax.set_ylim(0, 300)

    theta_now = data.yaw
    r_now = data.distance
    vline = ax.axvline(theta_now, color="black")
    graph = ax.bar([], [], np.deg2rad(1), color="green")

def graph_animate():
    global fig, animation
    def update(frame) -> tuple:
        global theta_now, vline, graph, data, yawdist
        data.update()
        vline.remove()

        theta_now = np.deg2rad(data.yaw)
        r_now = data.distance
        yawdist[theta_now] = r_now
        theta = list(yawdist.keys())
        r = list(yawdist.values())

        vline = plt.axvline(theta_now, color="black")
        print(graph)
        return vline, graph

    style.use("fast")
    animation = anim.FuncAnimation(fig, update, interval=20, cache_frame_data=False)

if __name__ == "__main__":
    try:
        data = ArduinoData()
        graph_init(data)
        graph_animate()
        plt.show()
    except KeyboardInterrupt:
        plt.close()
        exit()