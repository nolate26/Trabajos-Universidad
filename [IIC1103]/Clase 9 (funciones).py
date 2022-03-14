#La función se ejecuta hasta al primer return
#puedo ocupar mis propias funciones (sin números)

# import Clase 8 (funciones)
# print(Clase 8 (funciones).calcular_area(2))

#EJERCICIO USAIN BOLT

#Genere determinar tiempo de reacción.
# al inicio -> tiempo aleatorio entre 1-3s (preparados)
#"listos"-> 1-3 s
#"ya " de 1-5 s y muestre cuanto tardo

import random
import time

tiempo_preparado = random.randint(1,3)
time.sleep(tiempo_preparado)
print("Preparados")

tiempo_listos = random.randint(1,3)
time.sleep(tiempo_listos)
print("Listos")

tiempo_ya= random.randint(1,5)
time.sleep(tiempo_ya)
print("YA!")
inicio = time.time()

input()
final = time.time()    
tiempo_transcurrido = final-inicio
print("Te demoraste", tiempo_transcurrido, "segundos")


#EJEMPLO: función primos relativos 
def primos_relativos(n1,n2):
    if n1<n2:
        minimo = n1
    else:
        minimo = n2
    for i in range (2,minimo+1):
        if n1%i == 0 and n2%i==0:
            return False
    return True

print(primos_relativos(6,9))
print(primos_relativos(9,14))