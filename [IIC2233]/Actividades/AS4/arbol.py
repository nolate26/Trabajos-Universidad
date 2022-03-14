class NodoFama:

    def __init__(self, usuario, padre=None):
        # No modificar
        self.usuario = usuario
        self.padre = padre
        self.hijo_izquierdo = None
        self.hijo_derecho = None


class ArbolBinario:

    def __init__(self):
        # No modificar
        self.raiz = None

    def crear_arbol(self, nodos_fama):
        # No modificar
        for nodo in nodos_fama:
            self.insertar_nodo(nodo, self.raiz)

    def insertar_nodo(self, nuevo_nodo, padre=None):
        if self.raiz == None:
            self.raiz = nuevo_nodo
            return
        if nuevo_nodo.usuario.fama <= padre.usuario.fama:
            if padre.hijo_izquierdo:
                self.insertar_nodo(nuevo_nodo, padre.hijo_izquierdo)
            else:
                padre.hijo_izquierdo = nuevo_nodo
                nuevo_nodo.padre = padre
        elif nuevo_nodo.usuario.fama > padre.usuario.fama:
            if padre.hijo_derecho:
                self.insertar_nodo(nuevo_nodo, padre.hijo_derecho)
            else:
                padre.hijo_derecho = nuevo_nodo
                nuevo_nodo.padre = padre


    def buscar_nodo(self, fama, padre=None):
        if padre == None:
            padre = self.raiz
        if padre.usuario.fama == fama:
            return padre
        else:
            if padre.usuario.fama > fama:  
                if padre.hijo_izquierdo == None:
                    return None
                else:
                    self.buscar_nodo(fama, padre.hijo_izquierdo)
            else:
                if padre.hijo_derecho == None:
                    return None
                else:
                    self.buscar_nodo(fama, padre.hijo_derecho)

    def print_arbol(self, nodo=None, nivel_indentacion=0):
        # No modificar
        indentacion = "|   " * nivel_indentacion
        if nodo is None:
            print("** DCCelebrity Arbol Binario**")
            self.print_arbol(self.raiz)
        else:
            print(f"{indentacion}{nodo.usuario.nombre}: "
                  f"{nodo.usuario.correo}")
            if nodo.hijo_izquierdo:
                self.print_arbol(nodo.hijo_izquierdo,
                                 nivel_indentacion + 1)
            if nodo.hijo_derecho:
                self.print_arbol(nodo.hijo_derecho,
                                 nivel_indentacion + 1)
