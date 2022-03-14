from abc import ABC, abstractmethod
import parametros as p
import tributos

# Clase abstracta de un objeto
class Objeto(ABC):

    def __init__(self, nombre, tipo, peso):
        self.nombre = nombre
        self.tipo = tipo
        self.peso = peso

    @abstractmethod
    def entregar_beneficio(self, tributo, riesgo):
        pass

class Consumible(Objeto):
    
    def entregar_beneficio(self, tributo, riesgo):
        tributo.energia += p.AUMENTAR_ENERGIA
        print(f"{self.nombre} aumentó la energía de {tributo.nombre}!!!"
              f"\nNueva energía: {tributo.energia}")

class Arma(Objeto):

    def entregar_beneficio(self, tributo, riesgo):
        tributo.fuerza += tributo.fuerza * (p.PONDERADOR_AUMENTAR_FUERZA * riesgo + 1)
        print(f"{self.nombre} aumentó la fuerza de {tributo.nombre}!!!"
              f"\nNueva fuerza: {tributo.fuerza}")

class Especial(Objeto):

    def entregar_beneficio(self, tributo, riesgo):
        tributo.energia += p.AUMENTAR_ENERGIA
        tributo.fuerza += tributo.fuerza * (p.PONDERADOR_AUMENTAR_FUERZA * riesgo + 1)
        tributo.agilidad += p.AUMENTAR_AGILIDAD
        tributo.ingenio += p.AUMENTAR_INGENIO 
        print(f"WOW! {self.nombre} aumentó en muchas cualidades a {tributo.nombre}"
              f"\nNueva energía: {tributo.energia}"
              f"\nNueva fuerza: {tributo.fuerza}"
              f"\nNueva agilidad: {tributo.agilidad}"
              f"\nNuevo ingenio {tributo.ingenio}")