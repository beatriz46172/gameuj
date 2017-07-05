from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

a = 7
b = 7
sense.set_pixel(a, b, (255, 255, 0))

def gyroscope():
    x = sense.get_accelerometer_raw()['x']
    y = sense.get_accelerometer_raw()['y']
    x = round(x, 0)
    y = round(y, 0)
    
    if y == -1 and b > 0:
        global b
        b -= 1
        sense.set_pixel(a, b, (255, 255, 0))
    elif y == 1 and b < 7:
        global b
        b += 1
        sense.set_pixel(a, b, (255, 255, 0))
    elif x == -1 and a > 0:
        global a
        a -= 1
        sense.set_pixel(a, b, (255, 255, 0))
    elif x == 1 and a < 7:
        global a
        a += 1
        sense.set_pixel(a, b, (255, 255, 0))
        
while True:
    sense.clear(0, 0, 0)
    sense.set_pixel(a, b, (255, 255, 0))
    gyroscope()
    sleep(0.05)

