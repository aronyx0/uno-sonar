import serial

com = serial.Serial("COM3")

while True:
    print(str(eval(com.readline())))