#Operador in: operador booleano que dice si un string pertenece a otro
a= "i" in "Nicolas Olate"
print(a)
b="a" in "Nicolas Olate"
print(b)

#for var in string -> ir de caracter a caracter
#es lo mismo que for i in range (len(Nicolas))
for v in "Nicolas":
    print(v)
    
rut_sucio=input("RUT: ")
rut_limpio =""
for c in rut_sucio:
    if c in "1234567890kK":
        rut_limpio+=c
rut_formateado=rut_limpio[0:2]+"."+rut_limpio[2:5]+"."+rut_limpio[5:8]+"-"+rut_limpio[-1]
print(rut_formateado)

#caracteres especiales-> (\)
#1- (\n)
print("Hola\nsoy el chico\nde las poesias")
#\t-> tab
#\"->escribir doble comilla
#\'->escribir comilla 
#\\->\escribir backsalsh

#METODOS: similar a funcion -> recibe cosas y retorna valor
#var.metodo(<param,>)
#1) upper,lower (mayuscuka,minusculas)
s="texto minuscula"
a=s.upper()
print(a) 
b=a.lower()
print(b)

#2)var.islower,var.isupper
print(a.isupper()) #True
print(a.islower()) #false

#3) var.isalpha() , var.isdigit()
a="12345678"
print(a.isalpha()) #False
print(a.isdigit()) #True

#4) strip(<chars>) borra espacios y \n desde izquierda a palabra y de derecha a palabra
print("       ho   l       a".strip()) #ho   l     a
print("Hola o que tal soy yo".strip("Hyo ")) #la o que tal s

#EJERCICIO APNEAS
