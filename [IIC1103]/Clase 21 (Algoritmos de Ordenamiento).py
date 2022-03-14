#ORDENAR 
#Metodo sort():
#Funciona sobre listas en orden ascendente(numeros)
#L.sort()

#se puede ordenar de manera descendente?
#-> L.sort(reverse=True) o L.sort()->L[::-1]}

L=[1,34,62,-2,74,5]
L.sort()
print(L)
L.sort(reverse=True)
print(L)

#Si quiero mantener la lista, guardarla en otra lista l=l_original[:]

#Que pasa si no existiera el sort:
#1- selection sort:
#selecciona el menor de lo que queda por ordenar y lo intercambia con la casilla correspondiente
#L=[3,5,70,-1,3,7,1]->L=[-1,5,70,3,3,7,1]->L=[-1,1,70,3,3,7,5]
#Y asi sucesivamente

def selection_sort(L):
    for pos in range(0,len(L)):
        indice_menor_valor=pos
        for i in range(pos,len(L)):
            if L[i]<L[indice_menor_valor]:
                indice_menor_valor=i
        aux=L[indice_menor_valor]
        L[indice_menor_valor]=L[pos]
        L[pos]=aux

    return L

L=[7,2,9,11,51,-95]
print(L)
print(selection_sort(L))

#Oredenamos en lista de listas
def selection_sort1(L):
    for pos in range(0,len(L)):
        indice_menor_valor=pos
        for i in range(pos,len(L)):
            if L[i][1]<L[indice_menor_valor][1]:
                indice_menor_valor=i
        aux=L[indice_menor_valor]
        L[indice_menor_valor]=L[pos]
        L[pos]=aux

    return L
L=[['juana',15],['jose',20],['patricio',11],['francisco',9],['andrea',17]]
print(selection_sort1(L))

#Función Sorted-> sorted(lista):retorne lista de menor a mayor
#funciona tambien con strings
L=[1,34,62,-2,74,5]
p=sorted(L)
print(L)
print(p)
#tambien 
p=sorted(L,reverse=True)
print(p)

p=["casa","auto","sillon","silla"]
q=sorted(p)
print(p)
print(q)

#parametro "key" en el sorted: queda representada la lista con un valor

def por_edad(elemento):
    valor=elemento[1]
    return valor 

L=[['juana',15],['jose',20],['patricio',11],['francisco',9],['andrea',17]]
Q=sorted(L,key=por_edad) #puedo agregar el reverse
print(L)
print(Q)
#key tambien aplicable para el sort()
L.sort(key=por_edad)
print(L)

#ejemplo: ordenar naipes por pintas (C,P,D,T) y luego numeros

def ordenador(elemento):
    valor=0
    if elemento[1]=="C":
        valor=100
    elif elemento[1]=="P":
        valor=200
    elif elemento[1]=="D":
        valor=300
    elif elemento[1]=="T":
        valor=400
    valor+=elemento[0]
    return valor

def ordenar_cartas(cartas):
    cartas.sort(key=ordenador)
    return cartas


cartas =[[8,"P"],[9,"D"],[1,"T"],[1,"C"],[5,"C"],[2,"P"],[7,"D"],[8,"C"]]
print(cartas)
print(ordenar_cartas(cartas))

#SI QUIERO ORDENAR POR MAS DE UN CRITERIO-> RETURN (CRITERIO1,CRITERIO2)