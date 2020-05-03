import pygame
import random
import math
# LA POSISCION X;  x= V0 * Cos(angulo) * tiempo
# LA POSISCION Y;  y= h+V0 * Sen(angulo) * tiempo - g*t^2

FONDO = (0, 0, 0)
COLOR =(26,150,120)
color1 = (255,255,255)
cantidad_particulas = 50


class Rectangulo():
    def __init__(self):
        self.V0 = 45
        self.V1 = 15
        self.g=9.81
        self.angulo = math.radians(random.randrange(0,360))
        self.tiempo = 0
        self.xi = 0
        self.yi = 0
        #self.angulo1 = math.radians(45)
        self.x = 0
        self.y = 0
        self.width = random.randrange(3,10)
        self.heigth = self.width
        #self.move_x = posicion_x
        #self.move_y = posicion_y
        self.color = (a,b,c)
        self.vida = random.randrange(1,3)

        self.m=(-self.yi+y)/(self.xi-x)
        self.angulo1=(math.atan(self.m))

    def mover(self):
        self.x = self.xi+((self.V0 * (math.cos(self.angulo1))) + (self.V1*(math.cos(self.angulo)))) * self.tiempo
        self.y = self.yi-(((self.V1*(math.sin(self.angulo)))*self.tiempo)-((self.g*self.tiempo**2) / 2))

    def draw(self,pantalla):
        pygame.draw.rect(pantalla,self.color,[self.x,self.y,self.width,self.heigth])


def proy(self,pantalla):
        pygame.draw.rect(pantalla,color1[10,690,5,5])


def creaParticulas(x, y):
    particulasLista = []
    for i in range(cantidad_particulas):
        rectangulo = Rectangulo()
        rectangulo.x = x
        rectangulo.y = y
        rectangulo.xi = x
        rectangulo.yi = y

        particulasLista.append(rectangulo)
    return particulasLista





pygame.init()
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("SIMULACION MAMALONA")
FPS = 60
lista_particulas = []

reloj = pygame.time.Clock()

while True:
        a = random.randrange(0,255)
        b = random.randrange(0,255)
        c = random.randrange(0,255)
        for evento in pygame.event.get():
           if evento.type == pygame.QUIT:
               pygame.quit()
           elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
               x,y = evento.pos
               lista_particulas.append(creaParticulas(x, y))

             
            
        pantalla.fill(FONDO)

        i = 0
        for sub_lista in lista_particulas:
            j = 0
            for particula in sub_lista:
                particula.draw(pantalla)
                particula.mover()
                if  particula.vida < 0:
                    lista_particulas[i].pop(j)
                    
                particula.vida -= (1.0/60.0)
                particula.tiempo += (1.0/60.0)

                j += 1
            
            i += 1
        pygame.display.flip()
        reloj.tick(60)


