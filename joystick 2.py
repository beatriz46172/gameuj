from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
x, y = 0, 0

def move_up(event):
    global y
    if event.action == "pressed" and y > 0:
        y -= 1
    sense.clear()

def move_down(event):
    global y
    if event.action == "pressed" and y < 7:
        y += 1
    sense.clear()

def move_right(event):
    global x
    if event.action == "pressed" and x < 7:
        x += 1
    sense.clear()

def move_left(event):
    global x
    if event.action == "pressed" and x > 0:
        x -= 1
    sense.clear()
        
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down
sense.stick.direction_right = move_right
sense.stick.direction_left = move_left


while True:
    sense.clear(0, 0, 0)
    sense.set_pixel(x, y, 255, 255, 0)
    sleep(0.25)

                
