#Clase 1:
# -- escribe en la salida estandar (en general consola)
#-- los parentesis denotan que es una funcion
# -- es un procedimiento que uno llama y se ejecuta 
# -- lo que va entre parentesis son los parametros (del print)
#  -- le dimos un texto, un string, que va entre comillas 
print("este print va a la salida estándar")
print('este va en comillas simples')
print(1, 2, 3, 4, 5, "seis")

print("---Aqui veremos tipos")
# Veamos valores en Python
print(1, type(1))        # int, entero
print(1.0, type(1.0))    # float, flotante
print(True, type(True))  # bool, booleano
print("txt", type("txt"))  # str, string o texto

#ejemplo operador suma 
print(4+7)
print(1001+817)

#ejemplo operador resta 
print(4-7)

#ejemplo operador multiplicación 
print(5*8)
print(25*0) 

#ejemplo operador división 
print(12/4)
print(4/12)

#ejemplo operador potencia 
print(2**5)

#ejemplo operador división entera 
print(5//4)

#ejemplo operador módulo (RESTO)
print(7%5)

#ejemplo declaración de una variable 
a=1
print(a)

#ejemplo declaración de una variable como resultado de una operación 
a=20*860
print(a)

b=26%2
print(b)

#ejemplo nombres de variables 
cantidad_de_personas=1 
print(cantidad_de_personas) 
 
pasos=9-3 
print(pasos) 
 
esteEsElNombre_de_una_variable=7
print(esteEsElNombre_de_una_variable)

#ejemplo operación con variables 
manzanas=30
niños=6
cantidad_de_manzanas_por_niño=manzanas/niños 
print(cantidad_de_manzanas_por_niño)

#ejemplo variable de tipo int 
variable_a=1 
print(variable_a)

#ejemplo variable de tipo float
variable_b=3.9
print(variable_b)

#ejemplo variable de tipo string 
variable_c="este es un texto de ejemplo" 
print(variable_c)

#transformar texto a número entero 
texto1="710" 
print(texto1) 

variable_tipo_entera=int(texto1) 
print(variable_tipo_entera+1)

#transformar texto a número decimal
texto2="45.6891" 
print(texto2)

variable_tipo_float=float(texto2) 
print(variable_tipo_float+1)

#ejemplo print 
texto1="ejemplo1" 
texto2="ejemplo2" 
variable_numerica1=50 
variable_numerica2=40.56 

print("Como ya hemos visto, se puede imprimir solo texto. Pero también se pueden concatenar valores de variables con el operador ,") 
 
print("Por ejemplo:",texto1) 
print("O también:",variable_numerica1) 
print("También se pueden concatenar varios valores juntos, como estoy haciendo ahora",texto1,texto2,"aunque sean de distinto tipo",variable_numerica1,variable_numerica2)

#ejemplo input
texto_ingresado_por_el_usuario=input("ingresa un texto")
 
print("el texto ingresado es:") 
 
print(texto_ingresado_por_el_usuario)

#ejemplo 1: Cambiar dólares a pesos
precio_dolar=float(input("Ingrese el precio del dólar hoy:"))
cantidad_dolares=float(input("Ingrese la cantidad de dólares que desea cambiar:"))

cantidad_pesos=precio_dolar*cantidad_dolares
print("Tus",cantidad_dolares," a un precio de",precio_dolar,"equivalen a",cantidad_pesos,"pesos")

#ejemplo 2: Cambiar de grados Celsius a Fahrenheit 
grados_celsius=float(input("Ingrese la temperatura en grados Celsius que desea convertir a grados Fahrenheit."))
grados_fahrenheit=grados_celsius*(9/5)+32
print("Una temperatura de",grados_celsius,"°C es equivalente a",grados_fahrenheit,"°F") 

#ejemplo 3: Distancia entre dos puntos
x1 = 0
x2 = 3
y1 = 0
y2 = 4

distancia = ((y2-y1)**2+(x2-x1)**2)**(1/2)
print(distancia)