from sense_hat import SenseHat

sense = SenseHat()

v = (165, 42, 42) #vermelho diferente
r = (151, 105, 79) #lingua
b = (250, 250, 250) #branco
a = (255, 255, 0) #amarelo
p = (0, 0, 0)   #preto


image = [
a,a,a,a,a,a,a,a,
a,b,p,a,a,b,p,a,
a,b,b,a,a,b,b,a,
a,a,a,a,a,a,a,a,
a,v,v,v,v,v,v,a,
a,v,v,v,r,r,v,a,
a,a,v,v,r,r,a,a,
a,a,a,a,a,a,a,a
]

sense.set_pixels(image)
