


from sense_hat import SenseHat

sense = SenseHat()

a = (255, 255, 0) #amarelo
b = (250, 250, 250) #branco
r = (151, 105, 79) #lingua
g = (0, 255, 0)  #green
p = (0, 0, 0)   #preto
v = (165, 42, 42) #vermelho

image = [
g,a,a,a,a,a,a,g,
a,b,p,a,a,b,p,a,
a,b,b,a,a,b,b,a,
a,a,a,a,a,a,a,a,
a,v,v,v,v,v,v,a,
a,v,v,v,r,r,v,a,
a,a,v,v,r,r,a,a,
g,a,a,a,a,a,a,g
]

sense.set_pixels(image)
