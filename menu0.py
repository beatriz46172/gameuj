from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

v = (255, 0, 0) #vermelho
p = (0, 0, 0) #preto
c = (100, 100, 100) #cinzento
i = (255, 0, 0)
c = (100, 100, 100)
s = (255, 255, 255)

image = [
    s,p,s,p,p,p,p,s,
    s,p,s,p,p,p,p,s,
    s,p,s,p,p,s,p,s,
    s,s,s,p,p,s,s,s,
    p,p,p,p,p,p,p,p,
    p,p,v,p,p,v,p,p,
    p,v,v,p,p,v,v,p,
    p,p,v,p,p,v,p,p
    ]

def  move_middle(event):
    if event.action == "pressed" and event.direction == "middle":
       sense.set_pixel(0,0, (255, 0, 0))

def menu():
    x = sense.get_accelerometer_raw()['x']
    y = sense.get_accelerometer_raw()['y']
    x = round(2*x, 0)
    y = round(2*y, 0)

    if y == 1:
        sense.show_message("Highscore")

while True:
    sense.clear()
    sense.set_pixels(image)
    menu()
