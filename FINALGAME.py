from sense_hat import SenseHat
from random import randint
from time import sleep
from time import time
from datetime import datetime, timedelta

def gyroscope():
    global a,b
    x = sense.get_accelerometer_raw()['x']
    y = sense.get_accelerometer_raw()['y']
    x = round(x, 0)
    y = round(y, 0)
    if y == 1 and b > 0:
        b -= 1
        sense.set_pixel(a, b, (0, 0, 0))
    elif y == -1 and b < 7:
        b += 1
        sense.set_pixel(a, b, (0, 0, 0))
    elif x ==-1 and a < 7:
        a += 1
        sense.set_pixel(a, b, (0, 0, 0))
    elif x == 1 and a > 0:
        a -= 1
        sense.set_pixel(a, b, (0, 0, 0))

def game_over_win(a,r,y,b,t,m,w,x,k):
    global time1, time2, elapsed, e, h
    time2= datetime.now()
    elapsed=time2 - time1
    print (str(elapsed.total_seconds()))
    if (a == r and y == b) or (t==a and y == b) or (m ==a and y == b) or (x ==a and w == b) or (x== a and b==k) :   
        sense.set_rotation(180)
        sense.show_message("Game Over", scroll_speed=0.03, text_colour=[255,0,0])
        sense.show_message(str(int(elapsed.total_seconds())), scroll_speed=0.06)
        if int(elapsed.total_seconds()) > h:
            sense.show_message("New Highscore", scroll_speed=0.06)
            h = int(elapsed.total_seconds())
            sense.set_pixels(imagecaveira)
            sleep(1)            
            return 1
        else:
            sense.set_pixels(imagecaveira)
            sleep(1)
            return 1
    return 0
     
def move_up(event):
    global b
    print("evento= ", event)
    print("B up= ", b)
    if event.action == "pressed" and b < 7:
        b += 1
    print(b)
    sense.set_pixel(a, b, [0,0,0])

def move_down(event):
    global b
    print("evento= ", event)
    print("B down = ", b)
    if event.action == "pressed" and b > 0:
        b -= 1
    print(b)
    
    sense.set_pixel(a, b, [0,0,0])

def move_right(event):
    global a
    print("evento= ", event)
    print("A right= ", a)
    if event.action == "pressed" and a > 0:
        a -= 1
    print(a)
    sense.set_pixel(a, b, [0,0,0])

def move_left(event):
    global a
    print("evento= ", event)
    print("A left = ", a)
    if event.action == "pressed" and a < 7:
        a += 1
    print(a)
    sense.set_pixel(a, b, [0,0,0])



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
    test2 = game_over_win(a,r,y,b,t,m,w,x,k)
    return test2

def level_2(x,y):
    global r,t,m,w,k
    while True:
        sense.clear(0, 0, 0)
        gyroscope()
        draw_player()
        test = draw_enemy(x, y)
        if test == 1:
            break;
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

def new_game():
    global sense, a, b, r, t, m, w, k, y, x
    print("new_game ")
    
    #Sense hat reset
    sense.stick.direction_up = None
    sense.stick.direction_down = None
    sense.stick.direction_right = None
    sense.stick.direction_left = None
    sense.stick.direction_middle = None
    
    sense = SenseHat()
    sense.set_rotation(180)
    sense.clear()

    #Sense hat reset func
    sense.set_pixels(imagemenu)
    r = randint(0,4)
    t = randint(0,7)
    m = randint(4,7)
    w = randint(0,7)
    k = randint(2,6)
    y = 0
    x = 0
    a, b = (3, 4)
    sense.stick.get_events()
    
        
def menu():
    global sense, time1, time2, r, t, m, w, k, a, b, elapsed
    sense = SenseHat()
    sense.stick.get_events()
    while True:
        print (" new game1",a," ",b)
        y1 = sense.get_accelerometer_raw()['y']
        y1 = round(y1, 0)

        if y1 == -1:
            sense.show_message("Highscore '%s'"% (h))
            sense.set_pixels(imagemenu)
        for event in sense.stick.get_events():
            if event.action == "pressed" and event.direction == "middle":
                elapsed = timedelta(seconds=0)
                sense.set_rotation(180)
                sense.stick.direction_up = move_up
                sense.stick.direction_down = move_down
                sense.stick.direction_right = move_right
                sense.stick.direction_left = move_left
                x=0
                y=0
                time1 = datetime.now()
                print(elapsed, " elapsed and e ", e)
                while elapsed < e:
                    sense.clear(0, 0, 0)
                    draw_player()
                    test = draw_enemy(x, y)
                    if test == 1:
                        new_game()
                        break
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
                        sense.set_pixels(imagesmile)
                        sleep(1)
                        level_2(x,y)
                        new_game()
                        break

sense = SenseHat()
e = timedelta(seconds=2)
elapsed = timedelta(seconds=0)
sense.set_rotation(180)

#CORES
v = (255, 0, 0) #vermelho
p = (0, 0, 0) #preto
c = (100, 100, 100) #cinzento
s = (255,255,255) #branco
u = (255, 255, 0) #amarelo
j = (151, 105, 79) #lingua

h = 0
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
imagesmile  = [
    u,u,u,u,u,u,u,u,
    u,s,p,u,u,s,p,u,
    u,s,s,u,u,s,s,u,
    u,u,u,u,u,u,u,u,
    u,v,v,v,v,v,v,u,
    u,v,v,v,j,j,v,u,
    u,u,v,v,j,j,u,u,
    u,u,u,u,u,u,u,u
    ]

imagemenu = [
    s,p,s,p,p,p,p,s,
    s,p,s,p,p,p,p,s,
    s,p,s,p,p,p,p,s,
    s,s,s,p,p,s,s,s,
    p,p,p,p,p,p,p,p,
    p,v,v,v,v,v,v,p,
    p,p,v,v,v,v,p,p,
    p,p,p,v,v,p,p,p
    ]

r = randint(0,4)
t = randint(0,7)
m = randint(4,7)
w = randint(0,7)
k = randint(2,6)
y = 0
x = 0

while True:
    click = sense.show_message("Menu", scroll_speed=0.05)
    selection = input(click)
    sense.clear()
    sense.set_pixels(imagemenu)
    menu()
    
