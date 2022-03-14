from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout,
)
import parametros as p

# Usando Qtdesigner
window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_SALIR)

class VentanaFinal(window_name, base_class):

    senal_enviar_puntaje = pyqtSignal(int)
    senal_salir= pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.boton_salir.clicked.connect(self.salir)

    def salir(self):
        self.senal_salir.emit()
        self.senal_enviar_puntaje.emit(self.puntaje)
        self.hide()
    
    def mostrar(self, nivel, p_total, p_ronda, vidas, monedas):
        self.puntaje = p_total
        self.nivel.setText(f"{nivel}")
        self.puntaje_total.setText(f"{p_total}")
        self.puntaje_ronda.setText(f"{p_ronda}")
        self.vidas.setText(f"{vidas}")
        self.monedas.setText(f"{monedas}")
        self.show()
