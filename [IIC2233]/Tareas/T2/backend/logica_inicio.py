from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool)
    senal_abrir_juego = pyqtSignal()
    senal_rankings_creados = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, usuario):
        if usuario.isalnum() and p.MIN_CARACTERES <= len(usuario) <= p.MAX_CARACTERES:
            archivo = open(p.RUTA_PUNTAJES, "a", encoding = 'utf8')
            archivo.write(f"\n{usuario},")
            archivo.close()
            self.senal_abrir_juego.emit()
            booleano = True
        else:
            booleano = False
        self.senal_respuesta_validacion.emit(booleano)

    def calcular_ranking(self):
        with open(p.RUTA_PUNTAJES, 'rt', encoding = 'utf8') as rankings:
            data = rankings.readlines()
            lista_rankings = []
            for linea in data:
                frase = linea.strip().split(",")
                lista_rankings.append(frase)
            ordenados = sorted(lista_rankings, key=lambda num : int(num[1]), reverse=True)
            self.senal_rankings_creados.emit(ordenados[:5])
