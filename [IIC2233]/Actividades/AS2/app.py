from random import randint
from time import sleep
from pedido import Pedido
from shopper import Shopper
from threading import Thread


class DCComidApp(Thread):

    def __init__(self, shoppers, tiendas, pedidos):
        # NO MODIFICAR
        super().__init__()
        self.shoppers = shoppers
        self.pedidos = pedidos
        self.tiendas = tiendas #dict (nombre->Tienda)

    def obtener_shopper(self):
        while True:
            for shopper in self.shoppers:
                if shopper.ocupado == False:
                    return shopper
            print("Todos los Shoppers están ocupados :(")
            Shopper.evento_disponible.wait()
            print("Se desocupó un Shopper!")

    def run(self):
        l_pedido = self.pedidos.pop(0)
        tienda_oficial = self.tiendas[l_pedido[1]]
        pedido = Pedido(l_pedido[0],l_pedido[1],l_pedido[2])
        shopper = self.obtener_shopper()
        shopper.asignar_pedido(pedido)
        tienda_oficial.ingresar_pedido(pedido, shopper)
        tiempo = randint(1, 5)
        sleep(tiempo)


if __name__ == '__main__':
    pass
