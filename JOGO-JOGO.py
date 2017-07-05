from sense_hat import SenseHat
from random import randint
from time import sleep
import time

sense = SenseHat()

#CORES
v = (255, 0, 0) #vermelho
p = (0, 0, 0) #preto
c = (100, 100, 100) #cinzento
s = (255,255,255) #branco  

a, b = (7, 7)

click = sense.show_message("Start", scroll_speed=0.03)
image=[

p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
p,s,p,s,p,s,s,s,
p,s,p,s,p,p,p,s,
p,s,p,s,p,p,p,s,
p,s,p,s,p,s,p,s,
p,s,s,s,p,s,s,s,
p,p,p,p,p,p,p,p
]

sense.set_pixels(image)

selection = input(click)

def game_over(a,r,b,y,t):
    if a == r and y == b or t==a and y == b:
        sense.show_message("Game Over", scroll_speed=0.03)

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
       sense.set_pixel(0,0) 
     
    
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

def draw_player():
    sense.set_pixel(a, b, [255, 255, 0])
    
def draw_enemy():
    t = r +1<7
    sense.set_pixel(r, y, [255, 0, 0])
    sense.set_pixel(t, y, [255, 0, 0])
    game_over(a,r,b,y,t)
        
    sense.set_pixel(m, y, [250,0,0])
    game_over(a,r,b,y,t)
 

    sense.set_pixel(x, m2, [250,0,0])
    game_over(a,r,b,y,t)


r=randint(0,7)
m=randint(2,6)
m2=randint(0,7)
y=0
x=0


while True:
   sense.clear(0, 0, 0)
   draw_player()
   draw_enemy()
   sleep(0.25)
   y = y+1
   if y>= 8:
       r=randint (0,7)
       y=0
   x = x+1
   if x>= 8:
       m2=randint (0,7)
       x=0

