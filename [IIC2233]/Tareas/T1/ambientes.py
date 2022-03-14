from abc import ABC, abstractmethod
import parametros as p
import tributos

# Clase abstracta de ambiente
class Ambiente(ABC):

    def __init__(self, nombre, evento, dano):
        self.nombre = nombre
        self.evento = evento
        self.dano = dano

    def calcular_dano(self):
        dano = int((0.4 * self.humedad + 0.2 * self.vientos + 0.1 * self.precipitaciones 
                + 0.3 * self.nubosidad + self.dano) // 5)
        return max(5, dano)

class Playa(Ambiente):

    def __init__(self, nombre, evento, dano):
        super().__init__(nombre, evento, dano)
        self.vientos = p.VELOCIDAD_VIENTOS_PLAYA
        self.humedad = p.HUMEDAD_PLAYA
        self.precipitaciones = 0
        self.nubosidad = 0

class Montana(Ambiente):

    def __init__(self, nombre, evento, dano):
        super().__init__(nombre, evento, dano)
        self.nubosidad = p.NUBOSIDAD_MONTANA
        self.precipitaciones = p.PRECIPITACIONES_MONTANA
        self.vientos = 0
        self.humedad = 0 

class Bosque(Ambiente):

    def __init__(self, nombre, evento, dano):
        super().__init__(nombre, evento, dano)
        self.precipitaciones = p.PRECIPITACIONES_BOSQUE
        self.vientos = p.VELOCIDAD_VIENTOS_BOSQUE
        self.humedad = 0
        self.nubosidad = 0 


