#EJEMPLO 1
num=1
while num<=10:
  print(num, num**2)
  num+=1
print("fin del algoritmo")

#EJEMPLO 2
res=1
num=1
while num<=5:
    res=res*num
    num+=1
    print(res)

#ir printeando ayuda para ver como vamos 
#el num es un contador 

#EJEMPLO 3: muestre los n primeros multiplos de 3
n=int(input("cantidad de multiplos de 3 a mostrar: "))
numero=1
contador_multiplos=0
while contador_multiplos< n:
    if numero % 3==0:
        print(numero)
        contador_multiplos +=1
    numero+=1

#Ejemplo: multiplos de 3 o 7
n=int(input("cantidad de multiplos de 3 y 7 mostrar: "))
numero=1
contador_multiplos=0
while contador_multiplos< n:
    if numero % 3==0 and numero%7==0:
        print(numero)
        contador_multiplos +=1
    numero+=1

#EJEMPLO: MUESTRE LAS POTENCIAS DE 2 INFERIORES A 500
print("\nPotencias inferiores a 500: ")
num=0
while 2**num<500:
    print(2**num)
    num+=1
print("f del programa")

#EJEMPLO REAL 
