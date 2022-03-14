from tributos import Tributo
from ambientes import Ambiente, Bosque, Montana, Playa
from objetos import Objeto, Arma, Consumible, Especial
from parametros import paths

#creación de la lista de tributos
def lista_tributos():
    lista_tributos = []
    with open(paths("tributos"), 'rt', encoding = 'utf8') as archivo_tributos: 
        for linea in archivo_tributos.readlines()[1:]:
            linea = linea.strip().split(",")
            tributo = Tributo(linea[0], linea[1], int(linea[2]), int(linea[3]), int(linea[4]), 
                                  int(linea[5]), int(linea[6]), int(linea[7]), int(linea[8]))
            lista_tributos.append(tributo)
    return lista_tributos

# Creación lista de ambientes según el tipo de ambiente
def ambientes():
    lista_ambientes = [[],[],[]]
    with open(paths("ambientes"), 'rt', encoding = 'utf8') as archivo_ambientes: 
        for linea in archivo_ambientes.readlines()[1:]:
            linea = linea.strip().split(",")
            if linea[0] == 'playa':
                for indice in range(1, 4):
                    linea[indice] = linea[indice].split(";")
                    ambiente = Playa("Playa", linea[indice][0], int(linea[indice][1]))
                    lista_ambientes[0].append(ambiente)
            elif linea[0] == 'montaña':
                for indice in range(1, 4):
                    linea[indice] = linea[indice].split(";")
                    ambiente = Montana("Montaña", linea[indice][0], int(linea[indice][1]))
                    lista_ambientes[1].append(ambiente)
            elif linea[0] == "bosque":
                for indice in range(1, 4):
                    linea[indice] = linea[indice].split(";")
                    ambiente = Bosque("Bosque", linea[indice][0], int(linea[indice][1]))
                    lista_ambientes[2].append(ambiente)
    return lista_ambientes

# Lista de todos los objetos
def objetos():
    lista_objetos = []
    with open(paths("objetos"), 'rt', encoding = 'utf8') as archivo_objetos: 
        for linea in archivo_objetos.readlines()[1:]:
            linea = linea.strip().split(",")
            if linea[1] == "consumible":
                objeto = Consumible(linea[0], linea[1], int(linea[2]))
            elif linea[1] == "arma":
                objeto = Arma(linea[0], linea[1], int(linea[2]))
            elif linea[1] == "especial":
                objeto = Especial(linea[0], linea[1], int(linea[2]))
            lista_objetos.append(objeto)
    return lista_objetos

# Retprna lista de arenas
def arenas():
    lista_arenas = []
    with open(paths("arenas"), 'rt', encoding = 'utf8') as archivo_arenas: 
        for linea in archivo_arenas.readlines()[1:]:
            linea = linea.strip().split(",")
            lista_arenas.append(linea)
    return lista_arenas
