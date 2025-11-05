import time
import random

def inputdata():
    ms = int(time.time() * 1000)
    yaw = (ms % 6000) * 360 // 6000
    if yaw > 180: yaw = 360 - yaw

    distance = round((yaw * 300 / 180) * (random.randint(8, 10)/10))

    return f"({yaw},{distance})"

if __name__ == "__main__":
    while True:
        print(inputdata())

