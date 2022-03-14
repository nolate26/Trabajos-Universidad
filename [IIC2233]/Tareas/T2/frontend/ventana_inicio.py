from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout,
)
import parametros as p

# Usando Qtdesigner
window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_INICIO)

class VentanaInicio(window_name, base_class):

    senal_enviar_usuario = pyqtSignal(str)
    senal_calcular_ranking = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.boton_iniciar.clicked.connect(self.enviar_usuario)
        self.boton_ranking.clicked.connect(self.abrir_ranking)

    def abrir_ranking(self):
        self.ocultar()
        self.senal_calcular_ranking.emit()

    def enviar_usuario(self):
        usuario = self.lineEdit_ususario.text()
        self.senal_enviar_usuario.emit(usuario)

    def recibir_validacion(self, bool):
        if bool:
            self.ocultar()
        else:
            self.lineEdit_ususario.setText("")
            texto = "Usuario inválido! (4-15 caracteres alfanuméricos)"
            self.lineEdit_ususario.setPlaceholderText(texto)
            
    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()