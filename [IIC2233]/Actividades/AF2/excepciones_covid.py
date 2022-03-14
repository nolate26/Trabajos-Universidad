class RiesgoCovid(Exception):

    def __init__(self, sintoma, nombre_invitade):
        super().__init__()
        self.sintoma = sintoma
        self.nombre_invitade = nombre_invitade

    def alerta_de_covid(self):
        if self.sintoma == "fiebre":
            return f"El invitado {self.nombre_invitade} tiene fiebre, no puede ingresar :("
        
        elif self.sintoma == "dolor_cabeza":
            return f"El invitado {self.nombre_invitade} tiene dolor de cabeza, no puede ingresar :("
        
        elif self.sintoma == "tos":
            return f"El invitado {self.nombre_invitade} tiene fiebre, no puede ingresar :("
        
        
