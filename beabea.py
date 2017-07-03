from sense_hat import SenseHat
from time import sleep

sense= SenseHat()

r = [0, 0, 0]
s = [200, 0, 200]
t = [150, 0, 250]

image= [
r,r,r,s,s,r,r,r,
t,t,t,t,t,t,t,t,
s,s,t,t,r,s,s,t,
s,s,s,s,s,s,s,s,
t,t,t,t,t,t,t,t,
r,r,s,s,t,t,s,s,
s,s,t,t,r,r,s,t,
r,r,r,r,r,r,r,r
]


angles = [0, 90, 45, 100, 270, 360]

for r in angles:
    sense.set_rotation(r)
    
sense.set_pixels(image)


