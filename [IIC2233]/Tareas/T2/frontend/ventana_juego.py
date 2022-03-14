# IMPORTAMOS
from PyQt5 import uic
from PyQt5.QtCore import QRect, pyqtSignal, QThread, Qt
from PyQt5.QtGui import  QPixmap, QKeySequence
from PyQt5.QtWidgets import (
     QLabel, QShortcut
)
from PyQt5.Qt import Qt
import parametros as p
from time import sleep

# Usando QTdesigner
window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_JUEGO)

class VentanaJuego(window_name, base_class):

    senal_iniciar_juego = pyqtSignal()
    senal_iniciar_juego_inicial = pyqtSignal()
    senal_salir_juego = pyqtSignal()
    senal_revisar_tecla = pyqtSignal(tuple)
    senal_revisar_colision = pyqtSignal(QRect, bool)
    senal_revisar_froggy = pyqtSignal(QRect, str, bool, list)
    senal_pausar = pyqtSignal()
    senal_reanudar = pyqtSignal()
    senal_vidas_trampa = pyqtSignal()
    senal_terminar_nivel = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.boton_salir.clicked.connect(self.salir) 
        self.boton_pausar.clicked.connect(self.pausar)   
        self.vid = QShortcut(QKeySequence(Qt.Key_V, Qt.Key_I, Qt.Key_D), self)
        self.niv = QShortcut(QKeySequence(Qt.Key_N, Qt.Key_I, Qt.Key_V), self)
        self.vid.activated.connect(self.vidas_trampa)
        self.niv.activated.connect(self.ventana_post_nivel)

    def iniciar_juego(self):
        self.nivel = 1
        self.texto_vidas.setText(f"{p.VIDAS_INICIO}")
        self.texto_puntaje.setText("0")
        self.texto_nivel.setText("1")
        self.texto_tiempo.setText(f"{p.DURACION_RONDA_INICIAL} seg")
        self.texto_monedas.setText("0")
        self.cambio_nivel = False
        self.pausa = False
        self.autos = []
        self.troncos = []
        self.objetos = []
        self.show()
        self.senal_iniciar_juego_inicial.emit()

    def nuevo_nivel(self):
        self.show()
        self.autos = []
        self.troncos = []
        self.objetos = []
        self.cambio_nivel = False
        self.pausa = False
        self.senal_iniciar_juego.emit()
    
    def salir(self):
        self.senal_salir_juego.emit()
    
    def pausar(self):
        if self.pausa:
            self.pausa = False
            self.senal_reanudar.emit()
            for a in self.autos:
                a.pausa = False
            for t in self.troncos:
                t.pausa = False
        else:
            self.pausa = True
            self.senal_pausar.emit()
            for a in self.autos:
                a.pausa = True
            for t in self.troncos:
                t.pausa = True

    def vidas_trampa(self):
        self.senal_vidas_trampa.emit()

    def ventana_post_nivel(self):
        self.senal_terminar_nivel.emit()

    def cambiar_tiempo(self, num):
        self.texto_tiempo.setText(f"{num}") 

    def cambiar_vidas(self, num):
        self.texto_vidas.setText(f"{num}")

    def cambiar_monedas(self, num):
        self.texto_monedas.setText(f"{num}")

    def cambiar_nivel(self, num):
        self.texto_nivel.setText(f"{num}")
    
    def froggy_inicial(self):
        self.froggy.setPixmap(QPixmap(p.RUTA_FROGGY_INICIAL))
        self.froggy.setGeometry(*p.POSICION_INICIAL_FROGGY)
    
    def limpiar_listas(self):
        self.nivel += 1
        self.cambio_nivel = True
        for a in self.autos:
            a.auto.hide()
        for t in self.troncos:
            t.tronco.hide()
        for o in self.objetos:
            o.hide()

    def keyPressEvent(self, event):
        if p.TECLA_PAUSA == event.text().lower():
            if self.pausa:
                self.pausa = False
                self.senal_reanudar.emit()
                for a in self.autos:
                    a.pausa = False
                for t in self.troncos:
                    t.pausa = False
            else:
                self.pausa = True
                self.senal_pausar.emit()
                for a in self.autos:
                    a.pausa = True
                for t in self.troncos:
                    t.pausa = True
        if not self.pausa:
            if p.TECLA_ARRIBA == event.text().lower():
                self.senal_revisar_tecla.emit(("A",self.froggy.x(), self.froggy.y()))
            elif p.TECLA_IZQUIERDA == event.text().lower():
                self.senal_revisar_tecla.emit(("I",self.froggy.x(), self.froggy.y()))
            elif p.TECLA_ABAJO == event.text().lower():
                self.senal_revisar_tecla.emit(("AB",self.froggy.x(), self.froggy.y()))
            elif p.TECLA_DERECHA == event.text().lower():
                self.senal_revisar_tecla.emit(("D",self.froggy.x(), self.froggy.y()))
            elif p.TECLA_SALTO == event.text().lower():
                self.senal_revisar_tecla.emit(("S",self.froggy.x(), self.froggy.y()))

    def mover_froggy(self, dir_cantidad):
        if dir_cantidad[0] == "A":
            self.froggy.move(self.froggy.x(), self.froggy.y() - dir_cantidad[2])
            if dir_cantidad[1] == 0:    
                self.froggy.setPixmap(QPixmap(p.RUTA_FROGGY_ARRIBA_DETENIDO))
            elif dir_cantidad[1] == 1:
                self.froggy.setPixmap(QPixmap(p.RUTA_FROGGY_ARRIBA_MEDIO))
            else:
                self.froggy.setPixmap(QPixmap(p.RUTA_FROGGY_ARRIBA_FINAL))
        elif dir_cantidad[0] == "D":
            self.froggy.move(self.froggy.x() + dir_cantidad[2], self.froggy.y())
            if dir_cantidad[1] == 0:    
                self.froggy.setPixmap(QPixmap(p.RUTA_FROGGY_DERECHA_DETENIDO))
            elif dir_cantidad[1] == 1:
                self.froggy.setPixmap(QPixmap(p.RUTA_FROGGY_DERECHA_MEDIO))
            else:
                self.froggy.setPixmap(QPixmap(p.RUTA_FROGGY_DERECHA_FINAL))
        elif dir_cantidad[0] == "I":
            self.froggy.move(self.froggy.x() - dir_cantidad[2], self.froggy.y())
            if dir_cantidad[1] == 0:    
                self.froggy.setPixmap(QPixmap(p.RUTA_FROGGY_IZQUIERDA_DETENIDO))
            elif dir_cantidad[1] == 1:
                self.froggy.setPixmap(QPixmap(p.RUTA_FROGGY_IZQUIERDA_MEDIO))
            else:
                self.froggy.setPixmap(QPixmap(p.RUTA_FROGGY_IZQUIERDA_FINAL))
        elif dir_cantidad[0] == "AB":
            self.froggy.move(self.froggy.x(), self.froggy.y() + dir_cantidad[2])
            if dir_cantidad[1] == 0:    
                self.froggy.setPixmap(QPixmap(p.RUTA_FROGGY_ABAJO_DETENIDO))
            elif dir_cantidad[1] == 1:
                self.froggy.setPixmap(QPixmap(p.RUTA_FROGGY_ABAJO_MEDIO))
            else:
                self.froggy.setPixmap(QPixmap(p.RUTA_FROGGY_ABAJO_FINAL))
    
    def mover_froggy_tronco(self, d):
        if d == "D":
            self.froggy.move(self.froggy.x() + p.VELOCIDAD_TRONCOS, self.froggy.y())
        elif d == "I":
            self.froggy.move(self.froggy.x() - p.VELOCIDAD_TRONCOS, self.froggy.y())

    def crear_objeto(self, tipo, x ,y, nivel):
        objeto = QLabel(self)
        if tipo == 1:            
            objeto.setPixmap(QPixmap(p.RUTA_OBJETO_1))
        elif tipo == 2:
            objeto.setPixmap(QPixmap(p.RUTA_OBJETO_2))
        elif tipo == 3:
            objeto.setPixmap(QPixmap(p.RUTA_OBJETO_3))
        else:
            objeto.setPixmap(QPixmap(p.RUTA_OBJETO_4))
        objeto.setScaledContents(True)
        objeto.setGeometry(x, y, *p.TAMANO_OBJETO)            
        objeto.show()
        objeto.raise_()
        self.objetos.append(objeto)
    
    def ocultar_objeto(self, indice):
        x = self.objetos.pop(indice)
        x.hide()

    def cambiar_velocidad_troncos(self):
        for tronco in self.troncos:
            tronco.aumento_velocidad

    def mover_tronco(self, velocidad, nivel):
        tronco_1 = Tronco(self, 1, velocidad, nivel)
        tronco_2 = Tronco(self, 2, velocidad, nivel)
        tronco_3 = Tronco(self, 3, velocidad, nivel)
        tronco_1.actualizar.connect(self.actualizar_tronco)
        tronco_2.actualizar.connect(self.actualizar_tronco)
        tronco_3.actualizar.connect(self.actualizar_tronco)
        self.troncos.append(tronco_1)
        self.troncos.append(tronco_2)
        self.troncos.append(tronco_3)
        
    def mover_auto(self, velocidad, nivel):
        auto1 = Auto(self, 1, velocidad, nivel)
        auto2 = Auto(self, 2, velocidad, nivel)
        auto3 = Auto(self, 3, velocidad, nivel)
        auto4 = Auto(self, 4, velocidad, nivel)
        auto5 = Auto(self, 5, velocidad, nivel)
        auto6 = Auto(self, 6, velocidad, nivel)
        auto1.actualizar.connect(self.actualizar_auto)
        auto2.actualizar.connect(self.actualizar_auto)
        auto3.actualizar.connect(self.actualizar_auto)
        auto4.actualizar.connect(self.actualizar_auto)
        auto5.actualizar.connect(self.actualizar_auto)
        auto6.actualizar.connect(self.actualizar_auto)
        self.autos.append(auto1)
        self.autos.append(auto2)
        self.autos.append(auto3)
        self.autos.append(auto4)
        self.autos.append(auto5)
        self.autos.append(auto6)

    def actualizar_auto(self, label, x, y, nivel):
        for obj in self.objetos:
            obj.raise_()
        if nivel == self.nivel:
            label.move(x, y)
            self.senal_revisar_colision.emit(QRect(x, y, *p.TAMANO_AUTO), self.cambio_nivel)
        else: 
            return

    def actualizar_tronco(self, label, x, y, d, nivel):
        self.froggy.raise_()
        if nivel == self.nivel:
            label.move(x, y)
            self.senal_revisar_froggy.emit(QRect(x, y, *p.TAMANO_TRONCO), 
                                            d, self.cambio_nivel, self.troncos)
        else:
            return
    def ocultar(self):
        self.froggy_inicial()
        self.hide()

class Auto(QThread):

    actualizar = pyqtSignal(QLabel, int, int, int)

    def __init__(self, parent, num, velocidad, nivel): # tal vez colocar argumentos 
        super().__init__()    
        self.pausa = False  
        self.nivel = nivel
        self.velocidad = velocidad
        self.auto = QLabel(parent)
        if num == 1:
            self.auto.setPixmap(QPixmap(p.RUTA_AUTO_1))
            self.auto.setScaledContents(True)
            self.auto.setGeometry(*p.POSICION_INICIAL_AUTO_1)            
            self.__posicion = p.POS_AUTO_1
            self.posicion = p.POS_AUTO_1
        elif num == 2:
            self.auto.setPixmap(QPixmap(p.RUTA_AUTO_2))
            self.auto.setScaledContents(True)
            self.auto.setGeometry(*p.POSICION_INICIAL_AUTO_2)            
            self.__posicion = (p.POS_AUTO_2)
            self.posicion = (p.POS_AUTO_2)
        elif num == 3:
            self.auto.setPixmap(QPixmap(p.RUTA_AUTO_3))
            self.auto.setScaledContents(True)
            self.auto.setGeometry(*p.POSICION_INICIAL_AUTO_3)            
            self.__posicion = (p.POS_AUTO_3)
            self.posicion = (p.POS_AUTO_3)
        elif num == 4:
            self.auto.setPixmap(QPixmap(p.RUTA_AUTO_4))
            self.auto.setScaledContents(True)
            self.auto.setGeometry(*p.POSICION_INICIAL_AUTO_4)            
            self.__posicion = (p.POS_AUTO_4)
            self.posicion = (p.POS_AUTO_4)
        elif num == 5:
            self.auto.setPixmap(QPixmap(p.RUTA_AUTO_5))
            self.auto.setScaledContents(True)
            self.auto.setGeometry(*p.POSICION_INICIAL_AUTO_5)            
            self.__posicion = (p.POS_AUTO_5)
            self.posicion = (p.POS_AUTO_5)
        else:
            self.auto.setPixmap(QPixmap(p.RUTA_AUTO_6))
            self.auto.setScaledContents(True)
            self.auto.setGeometry(*p.POSICION_INICIAL_AUTO_6)            
            self.__posicion = (p.POS_AUTO_6)
            self.posicion = (p.POS_AUTO_6)
        self.auto.show()
        self.start()
    @property
    def posicion(self):
        return self.__posicion
    # Cada vez que se actualicé la posición,
    # se actualiza la posición de la etiqueta
    @posicion.setter
    def posicion(self, valor):
        self.__posicion = valor
        self.actualizar.emit(self.auto, self.posicion[0], self.posicion[1], self.nivel)

    def run(self):
        if self.posicion[0] > 0:
            while self.posicion[0] > - 50:
                if not self.pausa:
                    sleep(1)
                    nuevo_x = self.posicion[0] - self.velocidad
                    self.posicion = (nuevo_x, self.posicion[1]) 
        elif self.posicion[0] < 0:
            while self.posicion[0] < 640:
                if not self.pausa:
                    sleep(1)
                    nuevo_x = self.posicion[0] + self.velocidad
                    self.posicion = (nuevo_x, self.posicion[1]) 


class Tronco(QThread):
    actualizar = pyqtSignal(QLabel, int, int, str, int)

    def __init__(self, parent, num, velocidad, nivel): 
        super().__init__()      
        self.pausa = False
        self.nivel = nivel
        self.velocidad = velocidad
        self.tronco = QLabel(parent)
        if num == 1:
            self.tronco.setPixmap(QPixmap(p.RUTA_TRONCO))
            self.tronco.setScaledContents(True)
            self.tronco.setGeometry(*p.POSICION_INICIAL_TRONCO_1) 
            self.direccion = "I"
            self.posicion = p.POS_TRONCO_1
        elif num == 2:
            self.tronco.setPixmap(QPixmap(p.RUTA_TRONCO))
            self.tronco.setScaledContents(True)
            self.tronco.setGeometry(*p.POSICION_INICIAL_TRONCO_2)            
            self.direccion = "D"
            self.posicion = (p.POS_TRONCO_2)
        elif num == 3:
            self.tronco.setPixmap(QPixmap(p.RUTA_TRONCO))
            self.tronco.setScaledContents(True)
            self.tronco.setGeometry(*p.POSICION_INICIAL_TRONCO_3)            
            self.direccion = "I"
            self.posicion = (p.POS_TRONCO_3)
        self.tronco.show()
        self.start()
    def run(self):
        if self.direccion == "I":
            while self.posicion[0] > - 50:
                if not self.pausa:
                    sleep(1)
                    nuevo_x = self.posicion[0] - self.velocidad
                    self.posicion = (nuevo_x, self.posicion[1])
                    self.actualizar.emit(self.tronco, self.posicion[0],
                                        self.posicion[1], "I", self.nivel) 
            self.tronco.hide()
        elif self.direccion == "D":
            while self.posicion[0] < 640:
                if not self.pausa:
                    sleep(1)
                    nuevo_x = self.posicion[0] + self.velocidad
                    self.posicion = (nuevo_x, self.posicion[1]) 
                    self.actualizar.emit(self.tronco, self.posicion[0], 
                                            self.posicion[1], "D", self.nivel)
            self.tronco.hide()
    def aumento_velocidad(self):
        self.velocidad += self.velocidad * 1.05
