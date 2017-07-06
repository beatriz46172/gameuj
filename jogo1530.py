from sense_hat import SenseHat
from random import randint
from time import sleep
from time import time
from datetime import datetime, timedelta

sense = SenseHat()

#CORES
v = (255, 0, 0) #vermelho
p = (0, 0, 0) #preto
c = (100, 100, 100) #cinzento
s = (255,255,255) #branco  

a, b = (7, 7)

image2 = [
    s,p,s,p,p,p,p,s,
    s,p,s,p,p,p,p,s,
    s,p,s,p,p,s,p,s,
    s,s,s,p,p,s,s,s,
    p,p,p,p,p,p,p,p,
    p,v,v,v,v,v,v,p,
    p,p,v,v,v,v,p,p,
    p,p,p,v,v,p,p,p
    ]

sense.set_pixels(image2)

def game_over(a,r,y,b,t,m,w,x,k):
    global time1, time2
    if (a == r and y == b) or (t==a and y == b) or (m ==a and y == b) or (x ==a and w == b) or (x== a and b==k): 
        time2= datetime.now()
        elapsed =time2 - time1
        e = elapsed
        print (str(e))
        sense.show_message("Game Over", scroll_speed=0.03, text_colour=[250,0,0])
        sense.show_message(str(e),scroll_speed=0.06)
        

        image = [
v,v,c,c,c,c,v,v,
v,c,c,c,c,c,c,v,
c,p,c,c,c,c,p,c,
c,p,p,c,c,p,p,c,
v,c,c,p,p,c,c,v,
v,c,c,c,c,c,c,v,
v,c,v,c,c,v,c,v,
v,c,v,c,c,v,c,v
]

        sense.set_pixels(image)
        quit()

def  move_middle(event):
    if event.action == "pressed" and event.direction == "middle":
       sense.set_pixel(0,0, [0,0,0])
     
def move_up(event):
    global b
    if event.action == "pressed" and b > 0:
        b -= 1
    sense.set_pixel(a, b, [0,0,0])

def move_down(event):
    global b
    if event.action == "pressed" and b < 7:
        b += 1
    sense.set_pixel(a, b, [0,0,0])

def move_right(event):
    global a
    if event.action == "pressed" and a < 7:
        a += 1
    sense.set_pixel(a, b, [0,0,0])

def move_left(event):
    global a
    if event.action == "pressed" and a > 0:
        a -= 1
    sense.set_pixel(a, b, [0,0,0])

sense.stick.direction_up = move_up
sense.stick.direction_down = move_down
sense.stick.direction_right = move_right
sense.stick.direction_left = move_left
sense.stick.direction_middle = move_middle

def draw_player():
    global a, b
    sense.set_pixel(a, b, [255, 255, 0])
    
def draw_enemy(x, y):
    global r, t, m, w, k
    sense.set_pixel(r, y, [255, 0, 0])
    sense.set_pixel(t, y, [255, 0, 0])
    sense.set_pixel(m,y, [255, 0, 0])
    sense.set_pixel(x,w, [255, 0, 0])
    sense.set_pixel(x, k, [255,0,0])
    game_over(a,r,y,b,t,m,w,x,k)
    
r = randint(0,7)
t = randint(0,5)
m = randint(0,6)
w = randint(0,7)
k = randint(1,5)
y = 0
x = 0

def menu():
    global r, t, m, w, k
    x = sense.get_accelerometer_raw()['x']
    y = sense.get_accelerometer_raw()['y']
    x = round(2*x, 0)
    y = round(2*y, 0)

    if y == 1:
        sense.show_message("Highscore")
    if selection==input(click):
        global time1, time2
        time1 = datetime.now()
        while True:
            sense.clear(0, 0, 0)
            draw_player()
            draw_enemy(x, y)
            sleep(0.25)
            y= y+1
            if y> 7:
                r = randint (0,7)
                t=randint(0,5)
                m=randint(0,6)
                print(r)
                y=0
            x = x+1
            if x> 7:
                w=randint (0,7)
                k=randint(1,5)
                x=0

click = sense.show_message("Menu")
selection = input(click)

while True:
    sense.clear()
    sense.set_pixels(image2)
    menu()

def gyroscope():
    x = sense.get_accelerometer_raw()['x']
    y = sense.get_accelerometer_raw()['y']
    x = round(4*x, 0)
    y = round(4*y, 0)
    
    if y == -1 and b > 0:
        global b
        b -= 1
        sense.set_pixel(a, b, (0, 0, 0))
    elif y == 1 and b < 7:
        global b
        b += 1
        sense.set_pixel(a, b, (0, 0, 0))
    elif x == -1 and a > 0:
        global a
        a -= 1
        sense.set_pixel(a, b, (0, 0, 0))
    elif x == 1 and a < 7:
        global a
        a += 1
        sense.set_pixel(a, b, (0, 0, 0))




