import time

def inputdata():
    ms = int(time.time() * 1000)
    yaw = (ms % 6000) * 360 // 6000
    if yaw > 180: yaw = 360 - yaw

    distance = yaw * 300 // 180

    return f"({yaw},{distance})"

if __name__ == "__main__":
    while True:
        print(inputdata())

