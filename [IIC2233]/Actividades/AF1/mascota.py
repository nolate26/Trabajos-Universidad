import random
import parametros as p

class Mascota:
    def __init__(self, nombre, raza, dueno,
                 saciedad, entretencion):
        self.nombre = nombre
        self.raza = raza
        self.dueno = dueno
        
        # Los siguientes valores están en %.
        self._saciedad = saciedad
        self._entretencion = entretencion

    @property
    def saciedad(self):
        return self._saciedad

    
    @saciedad.setter
    def saciedad(self, extremo):
        if extremo > 100:
            self._saciedad = 100
        elif extremo < 0:
            self._saciedad = 0
        else:
            self._saciedad = extremo

    @property
    def entretencion(self):
        return self._entretencion
    
    @entretencion.setter
    def entretencion(self, extremo):
        if extremo > 100:
            self._entretencion = 100
        elif extremo < 0:
            self._entretencion = 0
        else:
            self._entretencion = int(extremo)

    @property
    def satisfaccion(self):
        return (self.saciedad//2 + self.entretencion//2)
    
    def comer(self, comida):
        r_random = random.random()
        if r_random < comida.probabilidad_vencer:
            self.saciedad -= comida.calorias
            print(f"La comida estaba vencida! A {self.nombre} le duele la pancita :(")
        else:
            self.saciedad += comida.calorias
            print(f"{self.nombre} está comiendo {comida.nombre}, que rico!")


    def pasear(self):
        self.entretencion += p.ENTRETENCION_PASEAR
        self.saciedad += p.SACIEDAD_PASEAR
    
    def __str__(self):
        a = f"Nombre: {self.nombre}\nSaciedad: {self.saciedad}\n"
        b =  f"Entretención: {self.entretencion}\nSatisfacción {self.saciedad}"
        return a+b



class Perro(Mascota):

    def __init__(self, nombre, raza, dueno, saciedad, entretencion):
        super().__init__(nombre, raza, dueno, saciedad, entretencion)
        self.especie = "PERRO"
        pass
    
    def saludar(self):
        print("guau guau")
        pass
        

class Gato(Mascota):
    def __init__(self, nombre, raza, dueno, saciedad, entretencion):
        super().__init__(nombre, raza, dueno, saciedad, entretencion)
        self.especie = "GATO"
        pass
    

    def saludar(self):
        print("miau miau")
        pass

class Conejo(Mascota):
    def __init__(self, nombre, raza, dueno, saciedad, entretencion):
        super().__init__(nombre, raza, dueno, saciedad, entretencion)
        self.especie = "CONEJO"
        pass
    

    def saludar(self):
        print("CHILLIDOSSSSS")
        pass
