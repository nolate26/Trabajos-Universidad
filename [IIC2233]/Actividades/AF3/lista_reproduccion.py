"""
En este archivo se encuentra la clase ListaReproduccion, la Iterable que
contiene los videos ordenados
"""


from functools import reduce
from io import SEEK_CUR

from pelicula import Pelicula


class ListaReproduccion:

    def __init__(self, conjunto_videos, usuario, nombre):
        self.conjunto_videos = conjunto_videos
        self.usuario = usuario
        self.nombre = nombre

    def __iter__(self):
        return IterarLista(self.conjunto_videos.copy())


    def __str__(self):
        return f"Lista de Reproducción de {self.usuario}: {self.nombre}"


class IterarLista:

    def __init__(self, conjunto_videos):
        self.conjunto_videos = conjunto_videos

    def __iter__(self):
        return self

    def __next__(self):
        if self.conjunto_videos is None:
            # Levantamos una excepción del tipo StopIteration
            # con el mensaje "Llegamos al final".
            raise StopIteration("Se acabaron los videos")
        else:           
            tupla = reduce(lambda x, y: x if x[-1] > y[-1] else y, self.conjunto_videos)
            pelicula =  tupla[0]
            self.conjunto_videos.remove(tupla)
            return pelicula
        
