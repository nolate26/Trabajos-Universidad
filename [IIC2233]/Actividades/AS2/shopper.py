
from threading import Thread, Event
from time import sleep
from random import randint


class Shopper(Thread):

    evento_disponible = Event()

    def __init__(self, nombre, velocidad):
        # No Modificar
        super().__init__()
        self.posicion = 0
        self.distancia_tienda = 0
        self.distancia_destino = 0
        self.pedido_actual = None
        self.termino_jornada = False
        # COMPLETAR DESDE AQUI
        self.nombre = nombre
        self.velocidad = velocidad
        self.__ocupado = False
        self.daemon = True


    @property
    def ocupado(self):
        # No Modificar
        if self.pedido_actual:
            return True
        return False

    def asignar_pedido(self, pedido):
        # No Modificar
        print(f"Asignando pedido {pedido.id_} a {self.nombre}...")
        self.distancia_tienda = randint(1, 10)
        self.distancia_destino = self.distancia_tienda +\
            pedido.distancia_destino
        self.pedido_actual = pedido
        self.posicion = 0
        print(f"El pedido {pedido.id_} fue asignado a {self.nombre}")

    def avanzar(self):
        # Completar
        self.posicion += 1
        tiempo = 1/ self.velocidad
        sleep(tiempo)
        print(f"El Shopper {self.nombre} avanzó hasta la posición {self.posicion}")


    def run(self):
        if self.termino_jornada == False or self.ocupado == False:
            if self.pedido_actual != None:
                self.avanzar()
            if self.posicion == self.distancia_tienda:
                print(f"El repartidor {self.nombre} llegó a la tienda")
                self.pedido_actual.evento_llego_repartidor.set()
                self.pedido_actual.evento_pedido_listo.wait()
            if self.posicion == self.distancia_destino:
                print(f"El Shopper {self.nombre} ha llegado al destino")
                self.pedido_actual.entregado = True
                self.evento_disponible.set()
                self.posicion = 0
                self.pedido_actual = None
            


if __name__ == "__main__":
    pass
