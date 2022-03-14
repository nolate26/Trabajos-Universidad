#IMPORTAMOS
import parametros as p
import random
import lectura_archivos

# Creamos la clase tributo
class Tributo():
    
    def __init__(self, nombre, distrito, edad, vida, energia, agilidad, fuerza, ingenio, popularidad):
        self.nombre = nombre
        self.distrito = distrito
        self.edad = edad
        self.__vida = vida
        self.__energia = energia
        self.agilidad = agilidad
        self.fuerza = fuerza 
        self.ingenio = ingenio
        self.popularidad = popularidad
        self.vivo = True
        self.mochila = []
        self.peso = 0

    # Creamos propertie de vida 0-100
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, valor):
        if valor <= 0:
            valor = 0
            print(f'{self.nombre} ha muerto')
        elif valor > 100:
            valor = 100
        self.__vida = valor

    # Creamos propertie de energía 0-100
    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self, valor):
        if valor <= 0:
            valor = 0
            print(f'{self.nombre} no tiene la energía necesaria  ')
        if valor > 100:
            valor = 100
        self.__energia = valor

    # Creamos función de ataque del jugador
    def atacar(self, tributo):
        # Condición -- Retornamos si es que se efectuó el ataque con su el texto
        if self.energia >= p.ENERGIA_ATACAR:
            print("\n-- SUCESOS OCURRIDOS --")
            self.energia -= p.ENERGIA_ATACAR
            # Calculamos el ataque y mostramos en consola
            calculo = int(((60 * self.fuerza) + (40 * self.agilidad) + (40 * self.ingenio) 
            - (30 * self.peso)) // self.edad)
            valor = min(90, max(5, calculo))
            print(f"{self.nombre} atacó a {tributo.nombre} quitándole {valor} de vida")
            texto = f"{self.nombre} atacó a {tributo.nombre}\n"
            tributo.vida -= valor
            if tributo.vida <= 0:
                self.popularidad += p.POPULARIDAD_ATACAR
                print(f"EL público enloquece!!!"
                      f"\n{self.nombre} ganó {p.POPULARIDAD_ATACAR} de popularidad")
            else:
                print(f"{tributo.nombre} quedó con {tributo.vida} de vida")
            print(f"{self.nombre} quedó con una energía de: {self.energia}")
            return (True, texto)
        else:
            print(f"{self.nombre} no tiene la energía necesaria para atacar"
                  f"\nIntenta con otra acción\n")
            return (False, 0)

    # Función de ataques de los tributos 
    def atacar_tributos(self, tributo):
        # Calculo de ataque - retorna texto
        calculo = int(((60 * self.fuerza) + (40 * self.agilidad) + (40 * self.ingenio) 
        - (30 * self.peso)) // self.edad)
        valor = min(90, max(5, calculo))
        print(f"\n{self.nombre} atacó a {tributo.nombre} quitándole {valor} de vida")
        texto = f"{self.nombre} atacó a {tributo.nombre}"
        tributo.vida -= valor
        if not tributo.vida <= 0:
            print(f"{tributo.nombre} quedó con {tributo.vida} de vida")
        return texto
    
    # Función para usar objeto
    def utilizar_objeto(self, riesgo):
        if self.mochila == []:
            print("\nNo hay objetos en tu mochila :(\nPuedes pedirle a los patrocinadores...")
        else:
            # Desplegamos menú de los objetos
            interfaz = True
            while interfaz:
                print(f'\n*** Objetos en la mochila ***\n{"-"*28}\n'
                    f'{" "*4} Nombre objeto -- Tipo')
                contador = 1
                for objeto in self.mochila:
                    print(f'[{contador}] {objeto.nombre} -- {objeto.tipo}')
                    contador += 1
                print(f"[{contador}] Volver")
                eleccion = input("\nIngrese su opción elegida: ")
                try:
                    validar_input = p.manejar_input(eleccion, contador)
                except (ValueError, IndexError) as error:
                    print(error)
                    validar_input = False
                if validar_input:
                    if eleccion != str(contador):
                        obj = self.mochila.pop(int(eleccion)-1)
                        self.peso -= obj.peso
                        print(f"\n{self.nombre} utilizó el objeto {obj.nombre}")
                        # Se usa objeto y se entrega el beneficio
                        obj.entregar_beneficio(self, riesgo)
                        interfaz = False
                    else:
                        interfaz = False

    # Función para pedir un objeto
    def pedir_objeto(self, arena):
        lista_objetos = lectura_archivos.objetos()
        if self.popularidad >= p.COSTO_OBJETO:
            obj = random.choice(lista_objetos)
            # Recibe objeto
            self.mochila.append(obj)
            self.peso += obj.peso
            self.popularidad -= p.COSTO_OBJETO
            print("\n-- SUCESOS OCURRIDOS --")
            print(f"Los patrocinadores le entregaron un/una '{obj.nombre}' a {self.nombre}"
                  f"\nObjeto de tipo: '{obj.tipo}'")
            return False
        else:
            print("\nNo tienes la popularidad suficiente para pedir un objeto a los patrocinadores")
            return True

    # Función de acción heroica
    def accion_heroica(self):
        if p.ENERGIA_ACCION_HEROICA <= self.__energia:
            print("\n-- SUCESOS OCURRIDOS --")
            self.popularidad += p.POPULARIDAD_ACCION_HEROICA
            self.__energia -= p.ENERGIA_ACCION_HEROICA
            print(f'{self.nombre} hizo una gran acción heroica!!!'
                  f'\nGanó {p.POPULARIDAD_ACCION_HEROICA} de popularidad :P'
                  f'\nPopularidad: {self.popularidad}' 
                  f'\nEnergía restante: {self.energia}')
            return False
        else:
            print(f"{self.nombre} no tiene la energía necesaria para realizar una acción heroica"
                  f"\nIntenta con otra acción\n")
            return True

    # Función de hacerse bolita
    def hacerse_bolita(self):
        print("\n-- SUCESOS OCURRIDOS --")
        self.energia += p.ENERGIA_BOLITA
        print(f"{self.nombre} se hizo bolita y recuperó {p.ENERGIA_BOLITA} de energía"
              f"\nAhora tiene {self.energia} de energía")
        return False


    def __str__(self):
        # Llamando al tributo imprimirá su estado
        objetos = ""
        if self.mochila != []:
            for obj in self.mochila:
                objetos += obj.nombre
                objetos += ', '
            objetos = objetos[:-2]
        else:
            objetos = "El tributo no tiene objetos :(" 
        texto = (f'\n{" "*10}Estado tributo'
                 f'\n{"-"*40}'
                 f'\nNombre: {self.nombre}'
                 f'\nDistrito: {self.distrito}'
                 f'\nEdad: {self.edad}'
                 f'\nVida: {self.__vida}'
                 f'\nEnergía: {self.__energia}'
                 f'\nAgilidad: {self.agilidad}'
                 f'\nFuerza: {self.fuerza}'
                 f'\nIngenio: {self.ingenio}'
                 f'\nPopularidad: {self.popularidad}'
                 f'\nObjetos: {objetos}'
                 f'\nPeso: {self.peso}')
        return texto

        