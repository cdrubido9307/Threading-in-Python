import time
import threading
import math

def circle_area(r):
    time.sleep(10)
    print(math.pi * r**2)
    return math.pi * r**2

if __name__ == '__main__':
    print('Main thread started')
    radius = float(input('Enter the radius: '))
    thread = threading.Thread(target=circle_area, args=[radius])
    print('Main waiting for thread to finish the area calculation')
    thread.start()
    thread.join()
    print('Main ended')