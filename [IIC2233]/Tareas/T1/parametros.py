import os

#Paths contenidos a importar
def paths(nombre):
    path_tributos = os.path.join('tributos.csv')
    path_ambientes = os.path.join('ambientes.csv')
    path_objetos = os.path.join('objetos.csv')
    path_arenas = os.path.join('arenas.csv')
    if nombre == "tributos":
        return path_tributos
    elif nombre == "ambientes":
        return path_ambientes
    elif nombre == "objetos":
         return path_objetos
    elif nombre == "arenas":
         return path_arenas

#código extraido de la ayudantía 3
#función para manejar el input
def manejar_input(opcion_elegida, cantidad_de_opciones):
    try:
        int_opcion_elegida = int(opcion_elegida)
    except ValueError:
        raise ValueError(f"\nEl valor ingresado no es un número entero\n")
    else:
        if int_opcion_elegida > cantidad_de_opciones or int_opcion_elegida < 1:
            raise IndexError(f"\nEl valor ingresado no está entre el 1 y el {cantidad_de_opciones}")
    return True

#SIMULACIÓN DE HORA
#acción heroica 
ENERGIA_ACCION_HEROICA = 15
POPULARIDAD_ACCION_HEROICA = 4

#atacar a tributo
ENERGIA_ATACAR = 20
POPULARIDAD_ATACAR = 5

#pedir objeto a patrocinadores
POPULARIDAD_PEDIR = 4

#hacerse bolita
ENERGIA_BOLITA = 20


#AMBIENTES
#Playa
VELOCIDAD_VIENTOS_PLAYA = 60
HUMEDAD_PLAYA = 30

#montaña
NUBOSIDAD_MONTANA = 70
PRECIPITACIONES_MONTANA = 35

#bosque
PRECIPITACIONES_BOSQUE = 65
VELOCIDAD_VIENTOS_BOSQUE = 30

AUMENTAR_ENERGIA = 20
PONDERADOR_AUMENTAR_FUERZA = 0.8
AUMENTAR_AGILIDAD = 10
AUMENTAR_INGENIO = 8
COSTO_OBJETO = 4

#ARENA
PROBABILIDAD_EVENTO = 5

