estado_tablero=input()
lista_tablero=estado_tablero.split(";")
num=len(lista_tablero)
for i in range(num):
    sublista=lista_tablero[i].split(",")
    lista_tablero[i]=sublista


for i in range(num):
    jugador=lista_tablero[i][0]
    if jugador=="O":
        lista_tablero[int(lista_tablero[i][1])][int(lista_tablero[i][2])]="O" 
    elif jugador=="X":
        lista_tablero[int(lista_tablero[i][1])][int(lista_tablero[i][2])]="X" 
    else:
        lista_tablero[int(lista_tablero[i][1])][int(lista_tablero[i][2])]="-" 

tablero=lista_tablero[0:3]
frase=""
ganador=""
for i in range(3):
    frase=""
    for j in range(3):
        frase+=tablero[i][j]
        frase+=" "
    frase=frase[:len(frase)-1]
    if frase=="O O O":
        ganador="O"
    if frase=="X X X":
        ganador="X"
    print(frase)


for i in range(3):
    contador_O=0
    contador_X=0
    for j in range(3):
        if tablero[j][i]=="O":
            contador_O+=1
        if tablero[j][i]=="X":
            contador_X+=1
    if contador_O==3:
        ganador="O"
    if contador_X==3:
        ganador="X"

contador_O1=0
contador_X1=0
contador_O2=0
contador_X2=0
indice=0
indice1=2
for i in range(3):
    if tablero[indice][i]=="O":
        contador_O1+=1
    if tablero[indice][i]=="X":
        contador_X1+=1
    if tablero[i][indice1]=="O":
        contador_O2+=1
    if tablero[i][indice1]=="X":
        contador_X2+=1
    indice+=1
    indice1-=1
if contador_O1==3:
    ganador="O"
if contador_X1==3:
    ganador="X"
if contador_O2==3:
    ganador="O"
if contador_X2==3:
    ganador="X"

if ganador=="":
    for i in range(3):
        for j in range(3):
            if tablero[i][j]=="-":
                ganador="No ha terminado"
            else:
                ganador="Empate"
    print(ganador)
else:
    print("Ganador:",ganador)