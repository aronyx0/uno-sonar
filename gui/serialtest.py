import serial

com = serial.Serial("COM5")

while True:
    print(str(eval(com.readline())))