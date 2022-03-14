#para ver ciclos se comando comando while-> volver a lo anterior si la respuesta es erronea.
#while-> un cierto numero de veces, si es true se hace 
#funciona como el if (con operacion logica) pero se repite hasta que deje de ser verdadera

#while True:
  #  print("Hola") se repite infinitas veces
#Break : corta la operación lógica 

while False:
    print("Hola ctm")
#no se ejecuta nada...es falsa.

#Ejemplo 1:
i= 0
while i < 3:
    print(i+1)
    i=i+1
print("\n")
#Ejemplo 2:
variable = 1
while variable<=20:
    print(variable)
    variable=variable+1 #es lo mismo a variable+=1
print("termino del conteo \n")

#Ejemplo 3: ver esto
inp= input("Escribe 1 para que termine el programa:\n")
while inp != "1":
    print("ERROR!!!")
    inp = input("Escribe 1 para que termine el programa:\n")
print("Felicitaciones, tu número es 1")

#ejemplo 4: break corta todo
while True:
    print("test")
    break


 #Ejercicio 5
#Escribe un programa donde un usuario ingrese un número n.
#El número n debe ser mayor que 1.
#El programa debe imprimir todos los números entre 1 y n (incluído).
#Cuando se imprima un número par se debe imprimir esto en consola (“Par”) y cuando sea impar también (“Impar”).
n = int(input("Ingresa un número mayor que 1.\n"))
while n <= 1:
  n = int(input("ERROR, EL NÚMERO NO ES MAYOR QUE 1. Ingresa un número mayor que 1.\n"))
i = 1
while i<=n:
  if i%2 == 0:
    print(i,"es par.")
  else:
    print(i,"es impar.")
  i+=1
