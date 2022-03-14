#for in range, otra forma de iterara-> cuando sé cuantas veces quiero iterar.
#no es necesario crear variables ni incrementar el iterador.
#range(n)-> desde 0 a n-1
#range (a,b) -> desde "a" a b-1
#forma más comoda del while 

for i in range(1,101):
    print(i, i**2)

#Ejemplo: múltiplos de 7 entre 1-1000
print("multiplos de 7:")
contador_múltiplos=0
for i in range(1,1001):
    if i%7==0:
        print(i)
        contador_múltiplos+=1
print("Total:", contador_múltiplos)

#programa que pida a cada persona ingresar cantidad definifa de peliculas 
cant_personas= int(input())
for i in range(cant_personas):
    print("te toca persona", i)

    for j in range (3):
        peli=input()
        print("perfecto, vere", peli)

    print("Gracias")

#programa muestre tabla multiplicar del 1-10
for i in range (1,10):
     print("Tabla del", i)
     for j in range(1,11):
         print(i,"*", j , "=", i*j)