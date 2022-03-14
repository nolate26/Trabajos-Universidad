#FUNCIONES


#calcular funcion abs
x =float(input())
if x>=0:
    print("El abs es:", x)
else:
    print(-x)
# o
x=float(input())
print(abs(x))

#Función: funciona igual que función matemática
#persona especializada, ejemplo: input(), str(), print() bool() int() float, funciones built in

#round-> redondea de (el numero, cuantos decimales)

#como defino mis propias funciones??????
#-> def nombre(parámetros):
    #codigo funcion....
    #return valor_retoro

def calcular_area(radio):
    pi=3.141592
    area= pi*radio**2
    return area
circulo_2=calcular_area(2)
print("circulo de radio 2:", circulo_2)
circulo_5=calcular_area(5)
print("Circulo de radio 5:", circulo_5)


#ambito global, estan en todos lados
#dentro de una funcion son de otro mundo, no puedo usar sus variables. 
#solo funcion funciona hasta la primera respuesta, primer return


# EJEMPLO:con bool deteremine si es par
def es_par(n):
    if n%2==0:
        return True
    else:
        return False

#Código principal
print(es_par(6))


def de_radianes_a_grados(rad):
    grados=rad/3.14 * 180
    return grados
print(de_radianes_a_grados(3.14))

#Modulos: gente ya elaboró las funciones, funciones hay que cargarlas cuando uno quiere 
#se usa el import->libreria
#ej math, random

#Las funciones que se usarán en el curso
import math
print(math.sqrt(4))

import random
print(random.randint(2,9))

