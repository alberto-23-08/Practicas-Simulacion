import random
import math
import time
import pygame
from pygame.locals import *
import sys

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


incremento = 0
def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PELUQUERIA")

    # cargamos el fondo y una imagen (se crea objetos "Surface")
    fondo = pygame.image.load("peluqueria.png").convert()
    cliente = pygame.image.load("cliente.png")
    a = pygame.image.load("estacion.png")
    # Indicamos la posicion de las "Surface" sobre la ventana (Y,X)
    # se muestran lo cambios en pantalla
    pygame.display.flip()
    # el bucle principal del juego
    x = 100
    y = 400
  
    
    velocidad = 30
    velocidad2 = 15
    derecha = True
    arriba= True    
    inre = 1
    Salida = True
    
    x1=  100
    y1 = 150
    while True:
        # Posibles entradas del teclado y mouse
        
        pygame.time.delay(100)
        screen.blit(fondo,(0, 0))
         
        screen.blit(a,(100,150)) 
        screen.blit(a,(300,150))
        screen.blit(cliente,(x,y))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        if t_llegadaa > 0:
            if derecha == True:
                if x < x1:
                    x += velocidad
                else :
                    derecha = False
            else :
                  derecha = False

            if arriba== True:
                if y > y1:
                    y -= velocidad2
                else :
                    arriba= False
            else :
                arriba = False
        else:  
               Salida = True
       
            #####cominesa la salida
        if Salida == True:
            if x == x1:
                x += velocidad
            else :
                Salida = False
        else :
              Salida = False

        
         
        pygame.display.update()

def tiempoEnQueSeDesocupaLaEstacion(estacion):
    return estacion[1]
t_min = int(input("tiempo de corte minimo "))
t_max = int (input("tiempo de corte maximo "))
t_entre = int(input("Ingrese el tiempo entre llegada de los clientes: "))
n_veces = int(input("Ingrese numero de simulaciones : " ))
n_peluqueros = int(input("Ingrese numero de peluqueros : " ))

r_corte = []
cortes = []
esperas = []
salidas = []
salidass = []
listaClientes = []
r_llegada = []
t_llegada = []
t_llegada_acumulado = 0
llegadas = []
t_llegadaa = []
llegadass = []
num1 = 0
num2 = 0 
corteTotal = 0
listaCliente = 0
t_llegadaa = 0
salidaa = 0

for i in range(0,n_veces):
   num1=  (random.random())
   r_llegada.append(num1)
print("r_llegada",r_llegada)

for i in range(0,n_veces):
   num2=  (random.random())
   r_corte.append(num2)
print("r_corte ",r_corte,"\n") 

peluqueros = []
for i in range(0,n_peluqueros):
   peluqueros.append([i+1,0 ])
  
 

t_llegada_acumuladoo = 0
t_corte = 0
num3 = 0
t_esperaTotal = 0

print("los peluqueros",peluqueros,"\n")
servicios = []
servicioss = []
print(" Cliente   t_llegada            t_espera              t_corte             t_salida         Estacion\n")
for i in range(0,n_veces):

    ############### TIEMPO DE LLEGADAS CON DECIMALES
    t_llegada = - t_entre*(math.log(r_llegada[i]))
    t_llegada_acumulado += t_llegada
    llegadas.append(t_llegada_acumulado)
    ################# TEMPO DE LLEGADAS EN ENTEROS 
    t_llegadaa = int (float(t_llegada))
    t_llegada_acumuladoo += t_llegadaa
    llegadass.append(t_llegada_acumuladoo)
    ##########TIEMPO DE CORTE
    t_corte = (t_min + ((t_max-t_min)*(r_corte[i])))
    cortes.append(t_corte)

    t_salida = t_llegada_acumulado + t_corte
    peluqueros.sort(key=tiempoEnQueSeDesocupaLaEstacion)

    # el tiempo de espera se calcula tomando el tiempo en el que se desocupa la estacion
    # mas proxima menos el tiempo de llegada actual
    t_espera = peluqueros[0][1] - t_llegada

    # si el tiempo en el que se desocupo la estacion es menor que el de llegada
    # la espera es 0
    if t_espera < 0:
        t_espera = 0

    t_salida += t_espera
    peluqueros[0][1] = t_salida

    servicios.append([i+1, t_llegada_acumulado, t_salida, peluqueros[0][0], t_espera])
    

    print("|    #%s           %.2f              %.2f              %.2f               %.2f           %s  |" %(i+1,t_llegada_acumulado,t_espera,t_corte,t_salida,peluqueros[0][0]))
    
    #print ("Cliente #%s Llegada: %s Espera: %s Servicio: %s Salida: %s Estacion: %s" %(i+1, t_llegada, t_espera, t_corte, t_salida, peluqueros[0][0]))
    servicioss.append(peluqueros[0][0])

    t_esperaTotal += t_espera
    salidaa = int (float(t_salida))
    salidass.append(salidaa)
    t_salidaUltimoCliente = t_salida
    corteTotal += t_corte
        


print("\n salida ultimocliente : %.0f"%t_salidaUltimoCliente)
print("esperatotal: %.2f" %t_esperaTotal)
print("tiempo de corte total : %.2f" %corteTotal)

fila_Longitud = t_salidaUltimoCliente / t_esperaTotal
print("longitud de la fila es %.2f" %fila_Longitud)

t_promedioEspera = t_esperaTotal / n_veces
print("tiempo promedio de espera  es de %.2f" %t_promedioEspera)

usoInstalacion = corteTotal / t_salidaUltimoCliente
instalacion = usoInstalacion* 100
print("Las instalaciones se usaron en un %.2f %%" %instalacion)



#tiempo = int(input("\n\ncuantos segundos quiere que dure la simulacion"))


tiempo = int (float(t_salidaUltimoCliente))
print (tiempo+1)
tiempo += 1

clientes = []
inicio = time.time()
print("las llegadas son: ",llegadass)
print("las salidas son :",salidass)
print("los peluqueros son :",servicioss)
#if tiempo >= t_salidaUltimoCliente :
#    print("si se puede simular") 
#    pe = 0
#    ce = 1
#    cs = 1
#    for i in range(0,tiempo):
#      print("minuto : %d" %i) 
#      time.sleep(1)
    
#      try:
#        if i in llegadass: 
#            print("Llegada del cliente ",ce,"en la estacion",servicioss[pe])
#            ce += 1
#            pe += 1
#        if i in salidass:
#            print("Salida del cliente ",cs)
#            cs += 1
       
#      except ValueError:
#        pass




if __name__ == "__main__":
    main()