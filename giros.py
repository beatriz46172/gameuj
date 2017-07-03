

from sense_hat import SenseHat

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


orientation = sense.get_orientation_degrees()
pitch = orientation['pitch']
roll = orientation['roll']
