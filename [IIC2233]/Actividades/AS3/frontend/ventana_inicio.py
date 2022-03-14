from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout,
)

import parametros as p


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(tuple)

    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)

    def init_gui(self, tamano_ventana):

        self.setWindowIcon(QIcon(p.RUTA_ICONO))
        self.setGeometry(tamano_ventana)
        #usuario
        self.usuario_form = QLineEdit('', self)
        self.label1 = QLabel('Usuario:', self)
        #contraseña
        self.clave_form = QLineEdit('', self)
        self.clave_form.setEchoMode(QLineEdit.Password)
        self.label2 = QLabel('Contraseña:', self)
        #foto
        self.foto = QLabel(self)
        pixeles = QPixmap(p.RUTA_LOGO)
        self.foto.setPixmap(pixeles)
        self.foto.setScaledContents(True)
        self.foto.setMaximumSize(400,400)
        self.foto.setGeometry(0, 0, 400, 400)

        self.ingresar_button = QPushButton('&Ingresar', self)
        self.ingresar_button.resize(self.ingresar_button.sizeHint())
        self.ingresar_button.clicked.connect(self.enviar_login)
        
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.usuario_form)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.label2)
        hbox2.addWidget(self.clave_form)

        vbox1 = QVBoxLayout()
        vbox1.addLayout(hbox1)
        vbox1.addLayout(hbox2)

        hbox3 = QHBoxLayout()
        hbox3.addLayout(vbox1)
        hbox3.addWidget(self.ingresar_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.foto)
        vbox.addLayout(hbox3)
        vbox.addStretch(1)
        self.setLayout(vbox)

        self.agregar_estilo()
        # COMPLETAR



    def enviar_login(self):
        tupla = (self.usuario_form.text(), self.clave_form.text())
        self.senal_enviar_login.emit(tupla)
        # COMPLETAR

    def agregar_estilo(self):
        # Acciones y señales
        self.clave_form.returnPressed.connect(
            lambda: self.ingresar_button.click()
        )  # Permite usar "ENTER" para iniciar sesión

        # Estilo extra
        self.setStyleSheet("background-color: #fdf600")
        self.usuario_form.setStyleSheet("background-color: #000000;"
                                        "border-radius: 5px;"
                                        "color: white")
        self.clave_form.setStyleSheet("background-color: #000000;"
                                      "border-radius: 5px;"
                                      "color: white")
        self.ingresar_button.setStyleSheet(p.stylesheet_boton)

    def recibir_validacion(self, tupla_respuesta):
        if tupla_respuesta[1]:
            self.ocultar()
        else:
            self.clave_form.setText("")
            self.clave_form.setPlaceholderText("Contraseña inválida!")

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()
