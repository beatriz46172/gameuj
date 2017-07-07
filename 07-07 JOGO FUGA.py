from sense_hat import SenseHat
from random import randint
from time import sleep
from time import time
from datetime import datetime, timedelta

sense = SenseHat()
e = timedelta(seconds=30)
elapsed = timedelta(seconds=0)
sense.set_rotation(180)

#CORES
v = (255, 0, 0) #vermelho
p = (0, 0, 0) #preto
c = (100, 100, 100) #cinzento
s = (255,255,255) #branco
u = (255, 255, 0) #amarelo
j = (151, 105, 79) #lingua

a, b = (3, 4)

imagecaveira = [
    v,v,c,c,c,c,v,v,
    v,c,c,c,c,c,c,v,
    c,p,c,c,c,c,p,c,
    c,p,p,c,c,p,p,c,
    v,c,c,p,p,c,c,v,
    v,c,c,c,c,c,c,v,
    v,c,v,c,c,v,c,v,
    v,c,v,c,c,v,c,v
    ]

image2 = [
    s,p,s,p,p,p,p,s,
    s,p,s,p,p,p,p,s,
    s,p,s,p,p,p,p,s,
    s,s,s,p,p,s,s,s,
    p,p,p,p,p,p,p,p,
    p,v,v,v,v,v,v,p,
    p,p,v,v,v,v,p,p,
    p,p,p,v,v,p,p,p
    ]

sense.set_pixels(image2)

def gyroscope():
    x = sense.get_accelerometer_raw()['x']
    y = sense.get_accelerometer_raw()['y']
    x = round(x, 0)
    y = round(y, 0)
    if y == 1 and b > 0:
        global b
        b -= 1
        sense.set_pixel(a, b, (0, 0, 0))
    elif y == -1 and b < 7:
        global b
        b += 1
        sense.set_pixel(a, b, (0, 0, 0))
    elif x ==-1 and a < 7:
        global a
        a += 1
        sense.set_pixel(a, b, (0, 0, 0))
    elif x == 1 and a > 0:
        global a
        a -= 1
        sense.set_pixel(a, b, (0, 0, 0))

def game_over_win(a,r,y,b,t,m,w,x,k):
    global time1, time2, elapsed, e
    time2= datetime.now()
    elapsed=time2 - time1
    print (str(elapsed.total_seconds()))
    if (a == r and y == b) or (t==a and y == b) or (m ==a and y == b) or (x ==a and w == b) or (x== a and b==k):
        sense.show_message("Game Over", scroll_speed=0.03, text_colour=[250,0,0])
        sense.show_message(str(int(elapsed.total_seconds())), scroll_speed=0.06)
        sense.set_pixels(imagecaveira)
        quit() 
            
def  move_middle(event):
    if event.action == "pressed" and event.direction == "middle":
       sense.set_pixel(0,0, [0,0,0])
       return True
    return False
     
def move_up(event):
    global b
    if event.action == "pressed" and b < 7:
        b += 1
    sense.set_pixel(a, b, [0,0,0])

def move_down(event):
    global b
    if event.action == "pressed" and b > 0:
        b -= 1
    sense.set_pixel(a, b, [0,0,0])

def move_right(event):
    global a
    if event.action == "pressed" and a > 0:
        a -= 1
    sense.set_pixel(a, b, [0,0,0])

def move_left(event):
    global a
    if event.action == "pressed" and a < 7:
        a += 1
    sense.set_pixel(a, b, [0,0,0])

#sense.stick.direction_middle = move_middle

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
    game_over_win(a,r,y,b,t,m,w,x,k)
    
r = randint(0,4)
t = randint(0,7)
m = randint(4,7)
w = randint(0,7)
k = randint(2,6)
y = 0
x = 0

def level_2(x,y):
    while elapsed>e:
        global elapsed, r, t, m, w, k
        sense.clear(0,0,0)
        gyroscope()
        draw_player()
        draw_enemy(x,y)
        sleep(0.25)
        y = y+1
        if y > 7:
            r = randint(0,4)
            t = randint(0,7)
            m = randint(4,7)
            y = 0
        x = x+1
        if x > 7:
            w = randint(0,7)
            k = randint(2,6)
            x = 0
        
def menu():
    sense.stick.get_events()
    while True:
        y1 = sense.get_accelerometer_raw()['y']
        y1 = round(y1, 0)
        if y1 == -1:
            sense.show_message("Fuga aos quadrados")
            sense.set_pixels(image2)
        for event in sense.stick.get_events():
            print(move_middle(event))
            if move_middle(event):
                sense.stick.direction_up = move_up
                sense.stick.direction_down = move_down
                sense.stick.direction_right = move_right
                sense.stick.direction_left = move_left
                global time1, time2
                x=0
                y=0
                global r, t, m, w, k
                time1 = datetime.now()
                while elapsed < e:
                    sense.clear(0, 0, 0)
                    draw_player()
                    draw_enemy(x, y)
                    sleep(0.25)
                    y = y+1
                    if y > 7:
                        r = randint(0,7)
                        t = randint(0,7)
                        m = randint(0,7)
                        y = 0
                    x = x+1
                    if x > 7:
                        w = randint(0,7)
                        k = randint(0,7)
                        x = 0
                    if elapsed > e:
                        sense.show_message("Next level", scroll_speed=0.05)
                        image3  = [
                        u,u,u,u,u,u,u,u,
                        u,s,p,u,u,s,p,u,
                        u,s,s,u,u,s,s,u,
                        u,u,u,u,u,u,u,u,
                        u,v,v,v,v,v,v,u,
                        u,v,v,v,j,j,v,u,
                        u,u,v,v,j,j,u,u,
                        u,u,u,u,u,u,u,u
                        ]
                        sense.set_pixels(image3)
                        sleep(1)
                        level_2(x,y)

click = sense.show_message("Menu", scroll_speed=0.05)
selection = input(click)

while True:
    sense.clear()
    sense.set_pixels(image2)
    menu()
