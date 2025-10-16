import serial
import tester

testing = True
monitor = serial.Serial("COM3")

class ArduinoData:
    def __init__(self, yaw, distance):
        self.yaw = yaw
        self.distance = distance

if __name__ == "__main__":
    while True:
        if testing: datastr = tester.inputdata()
        else: datastr = monitor.read()

        datastr = datastr.split(",")
        arduino = ArduinoData(datastr[0], datastr[1])