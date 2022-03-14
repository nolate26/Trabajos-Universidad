import os

from PyQt5 import uic
from PyQt5.QtCore import QRect, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont, QTransform
from PyQt5.QtWidgets import QLabel, QMessageBox, QPushButton

import parametros as p


# Recuerda que estamos usando QT Designer :eyes:
window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_JUEGO)

# COMPLETAR:
class VentanaJuego(window_name, base_class):

    senal_iniciar_juego = pyqtSignal()
    senal_tecla = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        # COMPLETAR

    def mostrar_ventana(self, usuario):
        self.show()
        self.casilla_puntaje.setText("0")
        self.casilla_nombre.setText(usuario)
        self.senal_iniciar_juego.emit()
        # COMPLETAR
        pass

    def keyPressEvent(self, event):
        if p.TECLA_ARRIBA == event.text().lower():
            self.senal_tecla.emit("U")
        elif p.TECLA_IZQUIERDA == event.text().lower():
            self.senal_tecla.emit("L")
        elif p.TECLA_ABAJO == event.text().lower():
            self.senal_tecla.emit("D")
        elif p.TECLA_DERECHA == event.text().lower():
            self.senal_tecla.emit("R")

    def init_gui(self):
        self.setWindowIcon(QIcon(p.RUTA_ICONO))
        self.setWindowTitle("Ventana de Juego")

        self.mensaje_derrota = QMessageBox()
        label = QLabel()
        label.setText("GAME OVER")
        label.setFont(QFont('Arial Font', 20))
        self.mensaje_derrota.layout().addWidget(label)
        self.mensaje_derrota.layout().setGeometry(QRect(80, 320, 300, 100))
        self.mensaje_derrota.setIconPixmap(QPixmap(p.RUTA_IMAGEN_SAD))
        self.mensaje_derrota.setStandardButtons(QMessageBox.Cancel)
        self.mensaje_derrota.setWindowTitle("DCCobreloa derrotada")
        self.mensaje_derrota.buttonClicked.connect(self.salir)
        self.mensaje_derrota.setWindowIcon(QIcon(p.RUTA_ICONO))

        self.logo = QPixmap(p.RUTA_LOGO)
        self.imagen_mapa = QPixmap(p.RUTA_MAPA)
        self.imagen_logo.setPixmap(self.logo)
        self.imagen_logo.setScaledContents(True)
        self.fondo_juego.setPixmap(self.imagen_mapa)
        self.fondo_juego.setScaledContents(True)

        self.boton_salir.clicked.connect(self.salir)
        self.iniciar_serpiente()

        self.imagen_item = QPixmap(p.RUTA_ITEM)
        self.item = QLabel("", self)
        self.item.setPixmap(self.imagen_item)
        self.item.setScaledContents(True)
        self.item.resize(p.WIDTH_COBRA + 10, p.WIDTH_COBRA + 10)
        self.item.move(p.POS_INICIO_ITEM[0], p.POS_INICIO_ITEM[1])

    def iniciar_serpiente(self):
        """La lista de cobra va así:
        self.cobra_list = CABEZA - CUERPO - CUERPO - CUERPO - ... - COLA
        """
        self.cobra_list = []
        self.cabeza_label = QLabel("", self)
        self.pixeles_cabeza = QPixmap(p.RUTA_COBRA_CABEZA)
        self.cabeza_label.setPixmap(self.pixeles_cabeza)
        self.cabeza_label.setScaledContents(True)
        self.cabeza_label.resize(p.WIDTH_COBRA, p.HEIGHT_COBRA)
        self.cobra_list.append(self.cabeza_label)
        self.pixeles_cuerpo = QPixmap(p.RUTA_COBRA_CUERPO)
        self.direccion = {"R": 180, "L": 0, "U": 90, "D": 270}

        for _ in range(p.LARGO_COBRA-1):
            cuerpo_label = QLabel("", self)
            cuerpo_label.setPixmap(self.pixeles_cuerpo)
            cuerpo_label.setScaledContents(True)
            cuerpo_label.resize(p.WIDTH_COBRA, p.HEIGHT_COBRA)
            self.cobra_list.append(cuerpo_label)

        for parte_cobra in self.cobra_list:
            parte_cobra.move(3000, 3000)
        self.boton = QPushButton()
        self.cabeza_label.setFocus()

    def cambiar_puntaje(self, puntaje):
        self.casilla_puntaje.setText(str(puntaje))

    def fin_del_juego(self):
        self.mensaje_derrota.exec_()

    def salir(self):
        self.close()

    def actualizar(self, dic):
        items = dic["items"]
        self.cambiar_puntaje(items)
        if dic["new_item"]:
            pos = dic["pos_item"]
            self.item.move(pos.x(), pos.y())
        self.avanzar_cobra(dic["pos_cabeza"], dic["direccion"])

    def avanzar_cobra(self, rect, direccion):
        self.cobra_list[0].setPixmap(self.pixeles_cuerpo)
        tr = QTransform()
        tr.rotate(self.direccion[direccion])
        pixeles_cabeza = self.pixeles_cabeza.transformed(tr)
        self.cobra_list[-1].setPixmap(pixeles_cabeza)
        self.cobra_list[-1].move(rect.x(), rect.y())
        self.cobra_list.insert(0, self.cobra_list.pop())
