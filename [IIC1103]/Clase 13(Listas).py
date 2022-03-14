#Lista: coleccion ordenada de valores 
superm=["fideos", "areoz", "queso"]

#Aspectos básicos
#1-lista vacia
p=[]
#2-ista int: floats varios tipos bools etc
fib=[1,1,2,3,5,8]
#3-lista float
r=[1.3,3.4,5.7]
#4-lista bools
p=[True,False,False]
#5- lista varios
j=["nico",4,6.8876,True]

#Operaciones Listas
a=[1,2,3,4,5,6]
b=[7,8,9]
print(a+b) #suma
print(a*2)  #multiplicar
c=[1,2,3,4,5,6]
print(a==c) #(=)->true
print(b>a) #(<)true

#Funcion len()
print(len(a)) # 6

#Posiciones 
c=[1,2,3,4,5,6]
print(c[3]) #4 -> elemento
print(c[1:3]) # [2,3]->retorna lista
print(3 in c) # True

#lista in var:
d=["Nico", "Olate" , "Orellana", 1 , True]
print("nico" in d ) #False
print("Olat" in d) #False

#for i in var():
for i in d:
    print(i) 

#Nico
#Olate
#Orellana
#1
#True

#str!=a listas: Listas puedo remplazar elementos
equipos=["español", "sevilla","Barca"]
equipos[2]="Farza"
print(equipos) #[español,sevilla,farza]

#Agregar elementos a Listas: MODIFICAR:

#var.append()-> agrefa al final
a=[1,2,3,4,5,6,7]
a.append(10)
print(a) #[1, 2, 3, 4, 5, 6, 7, 10]
a.append("Nixo")
print(a) #[1, 2, 3, 4, 5, 6, 7, 10, 'Nixo']

#####var.pop()-> retorna y elimina ultimo de lista
a=[1,2,3,4,5,6,7]
print(a.pop())  #7
print(a)   #[1, 2, 3, 4, 5, 6]
a=[1,2,3,4,5,6,7]
print(a.pop(4)) # 5   en esa posicion 
print(a) #[1, 2, 3, 4, 6, 7]



