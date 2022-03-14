#ejercicio clase anterior
grados_fahrenheit=float(input("Ingrese la temperatura en grados Fahrenheit que desea convertir a grados Celsius:"))
grados_celsius = (5/9)*(grados_fahrenheit-32)
print("Una temperatura de",grados_fahrenheit,"°F es equivalente a",grados_celsius,"°C")

#ejemplo paquete random, PAQUETES AGREGADO PARA OBTENER NÚMERO ALEATORIO (ENTRE 1-6)
import random
dado=random.randint(1,6)
numero_mult=int(input("¿Por qué número quieres multiplicar el resultado del dado?"))
print(dado*numero_mult)

#ejemplo operador lógico igualdad 
a=1 
b=2 
c=1 
print(a==a) 
print(a==b) 
print(b==a) 
print(a==c)

#ejemplo operador lógico desigualdad (=!)
a=1 
b=2 
c=1 
print(a!=a) 
print(a!=b) 
print(b!=a) 
print(a!=c) 

#ejemplo operador lógico textos
a="texto1"
b="texto2" 
c="texto1"
print(a==a)
print(a!=b)
print(b!=a)
print(a==c)

#ejemplo operador lógico < 
print(4<7)
print(7<7)
print(11<7)

#ejemplo operador lógico > 
print(4>7) 
print(7>7) 
print(11>7)

#ejemplo operador lógico >= 
print(4>=7) 
print(7>=7) 
print(11>=7)

#ejemplo operador lógico <= 
print(4<=7) 
print(7<=7) 
print(11<=7)

#varias operaciones lógicas
valor_a = 1
valor_b = 2

res = valor_a == valor_a
print(res)
res = valor_b != valor_b
print(res)
res = valor_a < valor_b
print(res)
res = valor_a > valor_b
print(res)
res = valor_a <= valor_a
print(res)
res = valor_a >= valor_b
print(res)

#ejemplo operador lógico not
print(3>=2)
print(not 3>=2)

print(1!=1)
print(not 1!=1)

#mini-ejercicio 1
print(-3 >= 9)
print(not -3 <= 9)
print(not -3 != -3)

#ejemplo operador binario or
a=True
b=False

print("a or b")
print("True or False")
print(a or b)

print("a or a")
print("True or True")
print(a or a)

print("b or b")
print("False or False")
print(b or b)

#ejemplo operador binario or 
numero = int(input("Ingrese el número que desea comprobar que no pertenezca al intervalo (3,10)\n")) 
menor_que_3 = numero <= 3 
mayor_que_10 = numero >= 10 
print(menor_que_3 or mayor_que_10) 

#ejemplo operador binario and 
a=True 
b=False 

print("a and b") 
print("True and False") 
print(a and b) 

print("a and a") 
print("True and True") 
print(a and a)  

print("b and b") 
print("False and False") 
print(b and b) 

#mini-ejercicio 2
a = -14

resultado = (((a < 0) and (a == a)) or (a > 14))

#ejemplo 2 operador binario and 
numero = int(input("Ingrese el número que desea comprobar si pertenece al intervalo [3,10)\n")) 
mayor_que_3 = numero >= 3 
menor_que_10 = numero < 10 
print(menor_que_10 and mayor_que_3) 

#ejemplo: cálculo promedio final
i1=4.4
i2=3.6
ex=4
t1=1.0
t2=5
t3=7.0
np=1

ne = ((0.15*i1+0.15*i2+0.3*ex)/.6)
ne_cumple = ne >= 4.0
print("Tu nota de evaluación (NE) es",ne,"¿Apruebas?",ne_cumple)

nt = ((0.1*t1+0.1*t2+0.1*t3)/0.3)
nt_cumple = nt >= 4.0
print("Tu nota de tareas (nt) es",nt,"¿Apruebas?",nt_cumple)

pf = 0.6*ne+0.3*nt+0.1*np
pf_cumple = pf >= 4.0
print("Tu promedio final (pf) es",pf,"¿Apruebas?",pf_cumple)

pasar_el_ramo = ne_cumple and nt_cumple and pf_cumple
print("¿Pasaste?",pasar_el_ramo)
