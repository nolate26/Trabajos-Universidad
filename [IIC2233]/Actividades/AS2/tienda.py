from threading import Thread, Lock
from time import sleep
from random import randint


class Tienda(Thread):

    def __init__(self, nombre):
        # NO MODIFICAR
        super().__init__()
        self.nombre = nombre
        self.cola_pedidos = []
        self.abierta = True
        # COMPLETAR DESDE AQUI
        self.lock_ingresar = Lock()
        self.lock_pedido = Lock()

    def ingresar_pedido(self, pedido, shopper):
        with self.lock_ingresar:
            tupla = (pedido, shopper)
            self.cola_pedidos.append(tupla)
            pedido.evento_pedido_listo.set()

    def preparar_pedido(self, pedido):
        tiempo = randint(1,10)
        print(f"Se demorará {tiempo} segundos el pedido")
        sleep(tiempo)
        print("El pedido está listo")

    def run(self):
        if len(self.cola_pedidos) != 0:
            with self.lock_pedido:
                pedido = self.cola_pedidos.pop(0)
                self.preparar_pedido(pedido)
                pedido.evento_pedido_listo.wait()
            pedido.evento_llego_repartidor.wait()
            print("El pedido ha sido retirado")
        else:
            print(f"La tienda {self.nombre} se tomará un break")
            tiempo = randint(1,5)
            sleep(tiempo)
            print(f"La tienda {self.nombre} ha vuelto a trabajar")


            

