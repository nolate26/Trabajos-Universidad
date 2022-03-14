#Ejemplo BINGO
import random

class Tombola:
    def __init__(self):
        self.numeros=[]
        for i in range(1,76):
            self.numeros.append(i)

    def sacar_bolita(self):
        bolitas_restantes=len(self.numeros)
        indice=random.randint(0,bolitas_restantes-1)
        bolita=self.numeros.pop(indice)
        return bolita

class Jugador:
    def __init__(self,nom,cant_cart):
        self.nombre=nom
        self.cartones=[]
        for i in range(cant_cart):
            carton=Carton()
            self.cartones.append(carton)

    def marcar_carton(self,num):
        for c in self.cartones:#c es un objeto tipo Carton
            c.marcar(num)

    def bingo(self):
        for c in self.cartones:
            if c.completo():
                return True
        return False
    



class Carton:
    def __init__(self):
        self.columnaB= Columna(5,1,15)
        self.columnaI=Columna(5,16,30)
        self.columnaN=Columna(4,31,45)
        self.columnaG=Columna(5,46,60)
        self.columnaO=Columna(5,61,75)
    
    def marcar(self,num):
        self.columnaB.marcar(num)
        self.columnaI.marcar(num)
        self.columnaN.marcar(num)
        self.columnaG.marcar(num)
        self.columnaO.marcar(num)
    
    def completo(self):
        colb=self.columnaB.completa()
        coli=self.columnaI.completa()
        coln=self.columnaN.completa()
        colg=self.columnaG.completa()
        colo=self.columnaO.completa()
        if colb and coli and coln and colg and colo:
            return True
        else:
            return False

class Columna:
    def __init__(self,cant_num,inicio,fin):
        self.numeros=[]
        while len(self.numeros)< cant_num:
            num=random.randint(inicio,fin)
            if num not in self.numeros:
                self.numeros.append(num)
        self.marcados=[]
    
    def marcar(self,num):
        if num in self.numeros:
            self.marcados.append(num)

    def completa(self):
        if len(self.numeros)==len(self.marcados):
            return True
        else:
            return False 



#CP
tombola=Tombola()
print(tombola.sacar_bolita()) #numeros aleatorios

hugo=Jugador("Hugo",2)
paco=Jugador("Paco",3)
luis=Jugador("Lucho",2)

while not hugo.bingo() and not paco.bingo() and not luis.bingo():
    numero=tombola.sacar_bolita()
    print(numero)
    hugo.marcar_carton(numero)
    paco.marcar_carton(numero)
    luis.marcar_carton(numero)

if hugo.bingo():
    print("Hugo gano el bingo")
if paco.bingo():
    print("Paco ganó el bingo")
if luis.bingo():
    print("Lucho gano el bingo")
