import random
import ambientes
import parametros as p

# Clase Arena
class Arena():

    def __init__(self, nombre, riesgo, dificultad, jugador, tributos, ambientes):
        self.nombre = nombre
        self.riesgo = riesgo
        self.dificultad = dificultad
        self.jugador = jugador
        self.tributos = tributos
        self.ambientes = ambientes
        self.contador_ciclo = 0

    # Función que ejecuta el evento
    def ejecutar_evento(self):
        if self.contador_ciclo == 0:
            lugar = "Playa"
        elif self.contador_ciclo == 1:
            lugar = "Montaña"
        elif self.contador_ciclo == 2:
            lugar = "Bosque"
        self.contador_ciclo += 1
        if self.contador_ciclo == 3:
            self.contador_ciclo = 0
        # Comienza evento si cumple probabilidad
        if random.randint(1,10) > p.PROBABILIDAD_EVENTO: 
            lista_ambientes = []
            for lista in self.ambientes:
                for evento in lista:
                    if evento.nombre == lugar:
                        lista_ambientes.append(evento)
            ambiente = random.choice(lista_ambientes)
            dano = ambiente.calcular_dano()
            print(f'\nSe produjo el evento {ambiente.evento} en el/la {lugar}!!!'
                  f'\nTodos perdieron {dano} de vida :(\n')
            self.jugador.vida -= dano
            for tributo in self.tributos:
                tributo.vida -= dano
            return f"Ocurrió el evento en: {lugar}"
        print(f"\nNo paso nada ^_^"
              f"\nTodos chill en el/la {lugar} :D")
        return "No ocurrió ningún evento"

    # Función que genera los encuentros
    def encuentro(self):
        atacante = random.choice(self.tributos)
        mismo_atacante = True
        self.tributos.append(self.jugador)
        while mismo_atacante:
            victima = random.choice(self.tributos)
            if victima != atacante:
                texto = f'{atacante.atacar_tributos(victima)}\n'
                self.tributos.pop()
                return texto
