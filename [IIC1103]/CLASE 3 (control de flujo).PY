#ejemplo 1 if
if True:
  print("resultado de la operación cuando es True")
else:
  print("resultado de la operación cuando es False")

#ejemplo 2 if
numero = int(input("Ingrese un número que sea mayor que 5\n"))

if numero>5:
  print("El número ingresado es mayor que 5.")
else:
  print("¡ERROR! El número que ingresaste no es mayor que 5.")

#ejemplo 3 if
import random
numero_dado=random.randint(1,6)
print("El número que arrojó el dado fue:",numero_dado,"\n")

if numero_dado%2==0:
  print("Este es un número par. \n")
else:
  print("Este es un número impar. \n")

#ejemplo 3 if v2
import random
numero_dado=random.randint(1,6)
print("El número que arrojó el dado fue:",numero_dado,"\n")

if numero_dado%2==0:
  print("Este es un número par. \n")

#ejemplo if anidados
import random
numero_aleatorio = random.randint(1,3)
nombre_persona = input("Ingresa tu nombre para poder asignarte a un grupo.")

if numero_aleatorio == 1:
  print(nombre_persona,"fuiste asignado/a al grupo ALERCE\n")
else:
  if numero_aleatorio == 2:
    print(nombre_persona,"fuiste asignado/a al grupo BOLDO\n")
  else:
    print(nombre_persona,"fuiste asignado/a al grupo CEREZO\n")

#ejemplo 1 if-elif-else (siempre se elige la primera elegida en orden)
import random
numero_aleatorio = random.randint(1,3)
nombre_persona = input("Ingresa tu nombre para poder asignarte a un grupo.")

if numero_aleatorio == 1:
    print(nombre_persona, "fuiste asignado/a al grupo ALERCE\n")
elif numero_aleatorio == 2:
    print(nombre_persona, "fuiste asignado/a al grupo BOLDO\n")
else:
    print(nombre_persona, "fuiste asignado/a al grupo CEREZO\n")

#ejemplo 2 if-elif-else
import random
numero_aleatorio = random.randint(1,5)
nombre_persona = input("Ingresa tu nombre para poder asignarte a un grupo.")

if numero_aleatorio == 1:
    print(nombre_persona + " fuiste asignado/a al grupo ALERCE\n")
elif numero_aleatorio == 2:
    print(nombre_persona + " fuiste asignado/a al grupo BOLDO\n")
elif numero_aleatorio == 3:
    print(nombre_persona + " fuiste asignado/a al grupo CEREZO\n")
elif numero_aleatorio == 4:
    print(nombre_persona + " fuiste asignado/a al grupo DAMASCO\n")
else:
    print(nombre_persona + " fuiste asignado/a al grupo EUCALIPTUS\n")


#ejercicio: cálculo promedio final modificado
i1=4.4
i2=3.6
ex=4
t1=1.0
t2=5
t3=7.0
np=1

ne = ((0.15*i1+0.15*i2+0.3*ex)/.6)
ne_cumple = ne >= 4.0
print("Tu nota de evaluación (NE) es",ne,"¿Apruebas el requisito?")

nt = ((0.1*t1+0.1*t2+0.1*t3)/0.3)
nt_cumple = nt >= 4.0
print("Tu nota de tareas (NT) es",nt,"¿Apruebas el requisito?",nt_cumple)

pf = 0.6*ne+0.3*nt+0.1*np
pf_cumple = pf >= 4.0
print("Tu promedio final (PF) es",pf,"¿Apruebas el requisito?",pf_cumple)

pasar_el_ramo = ne_cumple and nt_cumple and pf_cumple

if pasar_el_ramo:
  print("Pasaste")
else:
  print("No pasaste")

if 1.0<=pf<4.0:
  print("Reprobado")
elif (4.0<=pf<5.0) and ne_cumple and nt_cumple:
  print("Aprobado")
elif 5.0<=pf<6.0 and ne_cumple and nt_cumple:
  print("Con un voto de distinción")
elif 6.0<=pf<=7.0 and ne_cumple and nt_cumple:
  print("Con distinción máxima")

#ejercicio ruleta simple
import random

tipo_apuesta = int(input("¿Qué tipo de apuesta desea hacer?\n\t1) Pleno\n\t2) Par o Impar\n\t3) Docena\n"))

cant_apuesta = int(input("Ingrese la cantidad en dinero que desea apostar\n"))
cant_final = 0

if tipo_apuesta == 1:
  numero = int(input("Ingrese un número entre 0 y 36\n"))
  num_ruleta = random.randint(0,36)
  print("El número que salió en la ruleta es:",num_ruleta)
  if numero == num_ruleta:
    cant_final = cant_apuesta*36
    print("Ganaste:", (cant_final-cant_apuesta))
  else:
    print("Perdiste")
elif tipo_apuesta == 2:
  tipo = input("Ingresa PAR o IMPAR\n")
  num_ruleta = random.randint(0,36)
  print("El número que salió en la ruleta es:",num_ruleta)
  if (tipo == "PAR" and num_ruleta%2==0) or (tipo == "IMPAR" and num_ruleta%2==1):
    cant_final = cant_apuesta*2
    print("Ganaste:", (cant_final-cant_apuesta))
  else:
    print("Perdiste")
else:
  tipo = int(input("Ingresa 1, 2 ó 3 (para la primera, segunda o tercera docena respectivamente)\n"))
  num_ruleta = random.randint(0,36)
  print("El número que salió en la ruleta es:",num_ruleta)

  if (tipo == 1 and 1<=num_ruleta<=12) or (tipo == 2 and 13<=num_ruleta<=24) or (tipo == 3 and 25<=num_ruleta<=36):
    cant_final = cant_apuesta*3
    print("Ganaste:", (cant_final-cant_apuesta))
  else:
    print("Perdiste")

