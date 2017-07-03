from sense_hat import SenseHat

sense = SenseHat()

sense.set_pixel(0,0, [255, 255, 0])
speed = 0.5
x, y = 0, 0


while True:
    for event in sense.stick.get_events():
        sense.set_pixel (x, y,[255, 255, 0])
        speed = 0.5
        if event.action == "pressed" and event.direction == "up":
            y -= 1
            sense.clear()
        if event.action == "pressed" and event.direction == "down":
            y += 1
            sense.clear()
        if event.action == "pressed" and event.direction == "right":
            x += 1
            sense.clear()
        if event.action == "pressed" and event.direction == "left":
            x -= 1
            sense.clear()
            
            
