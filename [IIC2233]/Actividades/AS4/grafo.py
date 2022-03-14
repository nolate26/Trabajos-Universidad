from collections import deque


class NodoGrafo:
    def __init__(self, usuario):
        # No modificar
        self.usuario = usuario
        self.amistades = None

    def formar_amistad(self, nueva_amistad):
        if self in nueva_amistad.amistades or nueva_amistad in self.amistades:
            print("Ya existe relación previa")
        else:
            self.amistades.append(nueva_amistad)
            nueva_amistad.amistades.append(self)
            print("Creada la relación")

    def eliminar_amistad(self, ex_amistad):
        if ex_amistad in self.amistades:
            self.amistades.remove(ex_amistad)
        if self in ex_amistad.amistades:
            ex_amistad.amistades.remove(self)

def recomendar_amistades(nodo_inicial, profundidad):
    """
    Recibe un NodoGrafo inicial y una profundidad de busqueda, retorna una
    lista de nodos NodoGrafo recomendados como amistad a esa profundidad.
    """
    visitados = []
    recomendados = []
    for _ in range(profundidad):
        for nodo in nodo_inicial.amistades:
            queue = deque([nodo])    
            vertice = queue.popleft()
            if vertice in visitados:
                continue
            visitados.append(vertice)


    for v in visitados:
        if v not in nodo_inicial.amistades:
            recomendados.append(v)
    return recomendados






    # Debes modificarlo


def busqueda_famosos(nodo_inicial, visitados=None, distancia_min=80):
    """
    [BONUS]
    Recibe un NodoGrafo y busca en la red social al famoso mas
    cercano, retorna la distancia y el nodo del grafo que contiene
    a el usuario famoso cercano al que se encuentra.
    """
    # Completar para el bonus
