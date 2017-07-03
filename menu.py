from sense_hat import SenseHat
click = sense.show_message("Please click")
selection = input(click)
for event in sense.stick.get_events():
    if event.action == "pressed" and event.direction == "middle":
       sense.set_pixel(0,0)  
    
