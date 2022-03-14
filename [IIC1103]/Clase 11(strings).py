#string->cadena de caracteres(texto) "entre comillas"
#se pueden sumar y multiplicar
print('Esto es un texto')
print("Esto tambien es un texto")
print('''Comimos super "poco" en el Mcdonald's''')

#comparación de strings 
print("Hola"=="hola")
print("hola"=="hola")
print("bota"<"bote")

#todo tiene un orden mayusculas->minusculas}
print(len("holamellamonicolasolate"))
print(len("hola que tal"))

#posicion caracteres
s="murcielago"
print(s[0]) #m
print(s[7]) #a
print(s[-1]) #o

#slice o substring: s[i:j] antes de la j
n="Nicolas Olate Orellana"
print(n[0:7]) #Nicolas
print(n[8:13]) #Olate
print(n[:7]) #Nicolas
print(n[14:]) #Orellana
print(n[:]) #Nicolas Olate Orellana
print(n[:len(n)-1]) #Nicolas Olate Orellan
print(n[0]) #N
a="Barca es un equipo"
print("F"+a[1:3]+"$"+a[4:])

#slicing o substrings->ayuda a intercalar s[i:j:k]
p="anitalavalatina"
print(p[0:len(p):2]) #aiaaaaia
print(p[::-1]) #anitalavalatina-> dar vuelta el numero
print(p[0:len(p):3]) #atali
print("siesta"[0:len("siesta"):2])