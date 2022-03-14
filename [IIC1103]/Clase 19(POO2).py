#copia por referencia : pasa lo mismo con las listas, queda la variable por referencia,
#ambas variables están en la misma ubicación en la memoria, si hago variables distintas no hayb problema

#metodo __str__() a un objeto
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
    def __str__(self):
        s="("+str(self.x)+","+str(self.y)+")"
        return s
a=Punto2D(0,5)
print(a) #<__main__.Punto2D object at 0x00FEE700> ubicación objeto(con __str__ -> (0,5))
#cuidado usae mismos parámetros y atributos-> da lo mismo 
#no es necesario tener igual parametros, atributos 




class Aeropuerto:
    def __init__(self, nombre):
        self.nombre_aeropuerto = nombre
        self.vuelos = []  # podemos almacenar vuelos en una lista

class Vuelo:
    def __init__(self, destino):
        self.destino = destino

# opción 1: los vuelos son un objeto
aeropuerto = Aeropuerto("Chile") # creamos el objeto Aeropuerto
instancia_vuelo = Vuelo("Jamaica") # instancia de la clase Vuelo

aeropuerto.vuelos.append(instancia_vuelo)  # añadimos instancia_vuelo al objeto aeropuerto

# opción 2: los vuelos son un string
string_vuelo = "Vuelo con dirección a Jamaica"

aeropuerto.vuelos.append(string_vuelo)  # añadimos string_vuelo al objeto aeropuerto




