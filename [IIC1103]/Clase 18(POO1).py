#funcion type-> me dice el tipo de dato
#definir nuevos tipos de datos: perro, auto, etc
#operacion sobre:
#  objetos: conjunto de datos y comportamientos
#  y metodos: lo que puede hacer 

#una clase = type

#ej: perro-> clase
# el tipo de perro: instancias (golden,quiltro,boyero etc)
#atributos-> nombre, raza, edad:bools
#metodos-> puede ladrar, comer, morder :cambia los bools (cosas aplicadas)-> se aplican a objetos: tipo de perro

#¿como definir?
#->class NombreClase:
#class Perros:

#naipes:(int y string)atributos
#mi_carta=carta(2,"corazones")

#para crear los objetos de ese molde
#class NombreClase:
#      def __init__()

#calcular distancia 2 puntos
class Punto2D:
    def __init__(self,coord_x,coord_y):
        self.x=coord_x
        self.y=coord_y
        self.norma=(coord_x**2+coord_y**2)**(1/2)
        #agreguemos metodos al punto:
    def mover_x(self,size):
        self.x+=size
        self.norma=(self.x**2+self.y**2)**(1/2)
    def mover_y(self,size):
        self.y+=size
        self.norma=(self.x**2+self.y**2)**(1/2)
        #metodo ditancia
    def distancia(self, otro):
        dist=((self.x-otro.x)**2+(self.y-otro.y)**2)**(1/2)
        return dist


a=Punto2D(0,-5)
k=Punto2D(5,5)
print("Distancia entre A y K:",a.distancia(k))
#->class Nombre
print("El punto A se encuentra en",a.x,"y",a.y) #0 y -5
a.mover_x(3)#lo movimos
print("El punto A se encuentra en",a.x,"y",a.y) #3 y -5
k.mover_x(90)#movemos a k en x
k.mover_y(12)
print("El punto K se encuentra en",k.x,"y",k.y) #95 y 17
print("El punto A tiene norma",a.norma,"y el punto K tiene",k.norma)






