from mascota import Mascota
from random import randint, choice, random
from comida import Comida
import parametros as p

class Hotel:

    def __init__(self):
        self.__energia = 100
        self.__dias = 0
        self.max_energia = p.MAXIMO_ENERGIA_HOTEL
        self.mascotas = list()
        self.funcionando = True
        self.comidas = [
        Comida('Carne con legumbres', 18, 0.3),
        Comida('Pescado con Castañas', 22, 0.2),
        Comida('Pollo y Arroz', 20, 0.1)
        ]

    # COMPLETAR
    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self, extremo):
        if extremo >= self.max_energia:
            self.__energia = self.max_energia
        elif extremo < 0:
            self.__energia = 0
        else:
            self.__energia = extremo


    @property
    def dias(self):
        return self.__dias

    @dias.setter
    def dias(self, extremo):
        if self.__dias < 0:
            self.__dias = 0
        else:
            self.__dias = extremo

    def hotel_en_buen_estado(self):
        """
        Esta función verifica las condiciones de término
        del programa. Si se pierden más de dos mascotas
        en un mismo día o el Hotel se queda con menos de
        tres mascotas, el programa termina.
        """
        mascotas_perdidas = 0
        for mascota in self.mascotas:
            if mascota.satisfaccion < p.MASCOTA_SATISFACCION_MINIMO:
                self.despedir_mascota(mascota)
                mascotas_perdidas += 1
        if mascotas_perdidas > 2 or len(self.mascotas) < 3:
            return False
        return True

    def imprimir_estado(self):
        print(f"Día: {self.__dias}\nEnergía cuidador: {self.__energia}\nMascotas hospedadas: {len(self.mascotas)}")

    def recibir_mascota(self, mascotas):
        self.mascotas += (mascotas)
        for mascota in mascotas:
            mascota.saludar()
            print(f"""
            Ha aparecido un {mascota.especie} en la recepción,
            su nombre es {mascota.nombre}. {mascota.dueno}, su dueño
            te pide que lo cuides hasta que regrese.
            """)

    def despedir_mascota(self, mascota):
        self.mascotas.remove(mascota)

        print(f"""
        Oh no!
        {mascota.dueno}, el dueño de {mascota.nombre} se lo ha llevado.
        Huéspedes en el Hotel: {len(self.mascotas)}
        """)

    def imprimir_mascotas(self):
        for mascota in self.mascotas:
            print(mascota)

    def nuevo_dia(self):
        resp = self.hotel_en_buen_estado
        if resp == True:
            self.__dias += 1
            self.__energia = self.max_energia
            #falta restar entretencion
            print("Comienza un nuevo día")
        else:
            self.funcionando = False
            print(f"La simulación a terminado\nDías transcurridos: {self.__dias}")

        pass

    def revisar_energia(self):
        if self.energia >= min(p.COSTO_ENERGIA_ALIMENTAR, 
                               p.COSTO_ENERGIA_PASEAR):
            return True
        return False

    def pasear_mascota(self, mascota):
        self.energia -= p.COSTO_ENERGIA_PASEAR
        mascota.pasear()
        print(f'{mascota.nombre} salió a pasear feliz!')

    def alimentar_mascota(self, mascota):
        comida = choice(self.comidas)
        mascota.comer(comida) 
        self.__energia -= p.COSTO_ENERGIA_ALIMENTAR

