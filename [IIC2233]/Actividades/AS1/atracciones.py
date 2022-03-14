from abc import ABC, abstractmethod
from personas import Persona
import parametros as p


# Recuerda definir esta clase como abstracta!
class Atraccion(ABC):

    def __init__(self, nombre, capacidad):
        # No modificar
        self.nombre = nombre
        self.capacidad_maxima = capacidad
        self.fila = []

    def ingresar_persona(self, persona):
        # No modificar
        print(f"** {persona.nombre} ha entrado a la fila de {self.nombre}")
        self.fila.append(persona)
        persona.esperando = True

    def nueva_ronda(self):
        # No modificar
        personas_ingresadas = 0
        lista_personas = []
        while personas_ingresadas < self.capacidad_maxima and self.fila:
            lista_personas.append(self.fila.pop(0))

        self.iniciar_juego(lista_personas)

        for persona in lista_personas:
            persona.actuar()

    def iniciar_juego(self, personas):
        # No modificar
        for persona in personas:
            print(f"*** {persona.nombre} jugó esta ronda")
            persona.esperando = False
            self.efecto_atraccion(persona)
        print()

    @abstractmethod
    def efecto_atraccion(self, persona):
        # No modificar
        pass

    def __str__(self):
        return f"Atraccion {self.nombre}"


# Recuerda completar la herencia!
class AtraccionFamiliar(Atraccion):

    def __init__(self, nombre, capacidad):
        super().__init__(nombre, capacidad)
        self.efecto_salud = p.SALUD_FAMILIA
        self.efecto_felicidad = p.FELICIDAD_FAMILIA
        pass

    def efecto_atraccion(self, persona):
        persona.felicidad += self.efecto_felicidad
        persona.salud -= self.efecto_salud
        pass


# Recuerda completar la herencia!
class AtraccionAdrenalinica(Atraccion):

    def __init__(self, nombre, capacidad, salud_necesaria):
        super().__init__(nombre, capacidad)
        self.salud_necesaria = salud_necesaria
        self.efecto_salud = p.SALUD_ADRENALINA
        self.efecto_felicidad = p.FELICIDAD_ADRENALINA
        pass

    def efecto_atraccion(self, persona):
        if persona.salud <= self.salud_necesaria:
            print("La persona la bajaron del juego")
            persona.salud += (self.efecto_salud/2)
            persona.felicidad -= (self.efecto_felicidad/2)
        else:
            persona.salud -= (self.efecto_salud)
            persona.felicidad += (self.efecto_felicidad)
            
        pass


# Recuerda completar la herencia!
class AtraccionAcuatica(AtraccionFamiliar):
    def __init__(self, nombre, capacidad):
        super().__init__(nombre, capacidad)
        self.efecto_felicidad = p.FELICIDAD_ACUATICA
        pass

    def ingresar_persona(self, persona):
        if persona.tiene_pase == True:
            super().ingresar_persona(persona)
        #no se deja entrar (else)
        pass


# Recuerda completar la herencia!
class MontanaAcuatica(AtraccionAcuatica, AtraccionAdrenalinica):

    def __init__(self, nombre, capacidad, salud_necesaria, dificultad):
        AtraccionAdrenalinica.__init__(self, nombre, capacidad, salud_necesaria)
        self.dificultad = dificultad
        pass

    def iniciar_juego(self, personas):#al final
        for p in personas:
            self.ingresar_persona(p)
            f"la persona {p.nombre} ha jugado esta atracción"
            p.esperando = False
            if p.salud <= self.salud_necesaria * self.dificultad:
                p.tiene_pase = False
            

        pass
