from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()


r = (255, 0, 0) #vermelho
p = (0, 0, 0) #preto
c = (100, 100, 100                                                                  )
     
#caveira
     
image = [
r,r,c,c,c,c,r,r,
r,c,c,c,c,c,c,r,
c,p,c,c,c,c,p,c,
c,p,p,c,c,p,p,c,
r,c,c,p,p,c,c,r,
r,c,c,c,c,c,c,r,
r,c,r,c,c,r,c,r,
r,c,r,c,c,r,c,r
]


sense.set_pixels(image)
