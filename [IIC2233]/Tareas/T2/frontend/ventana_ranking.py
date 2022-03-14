from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout,
)
import parametros as p

# Usando Qtdesigner
window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_RANKING)

class VentanaRanking(window_name, base_class):

    senal_volver = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.boton_volver.clicked.connect(self.volver_inicio)

    def volver_inicio(self):
        self.ocultar()
        self.senal_volver.emit()
       
    def guardar_puntaje(self, puntaje):
        archivo = open(p.RUTA_PUNTAJES, "a", encoding = 'utf8')
        archivo.write(f"{puntaje}")
        archivo.close()

    def instalar_rankings(self, lista):
        self.nombre1.setText(f"{lista[0][0]}")
        self.nombre2.setText(f"{lista[1][0]}")
        self.nombre3.setText(f"{lista[2][0]}")
        self.nombre4.setText(f"{lista[3][0]}")
        self.nombre5.setText(f"{lista[4][0]}")
        self.puntos1.setText(f"{lista[0][1]}")
        self.puntos2.setText(f"{lista[1][1]}")
        self.puntos3.setText(f"{lista[2][1]}")
        self.puntos4.setText(f"{lista[3][1]}")
        self.puntos5.setText(f"{lista[4][1]}")
        self.mostrar()

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()
