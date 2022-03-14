from random import choice
from PyQt5.QtCore import QObject, QRect, pyqtSignal, QTimer
import parametros as p
from random import randint
        
class LogicaJuego(QObject):
    
    senal_crear_auto = pyqtSignal()
    senal_mover_auto = pyqtSignal()
    senal_generar_auto = pyqtSignal(int, int)
    senal_generar_tronco = pyqtSignal(int, int)
    senal_generar_objeto = pyqtSignal(int, int, int, int)
    senal_froggy_tronco = pyqtSignal(str)
    senal_actualizar_tiempo = pyqtSignal(int)
    senal_actualizar_vidas = pyqtSignal(int)
    senal_actualizar_monedas = pyqtSignal(int)
    senal_actualizar_nivel = pyqtSignal(int)
    senal_cambiar_velocidad_troncos = pyqtSignal()
    senal_borrar_objeto = pyqtSignal(int)
    senal_froggy_inicial = pyqtSignal()
    senal_limpiar_listas = pyqtSignal()
    senal_terminar_trhead_auto = pyqtSignal()
    senal_cerrar_ventana = pyqtSignal()
    senal_abrir_ventana = pyqtSignal(int, int, int, int, int)
    senal_final = pyqtSignal(int, int, int, int, int)

    def __init__(self, froggy):
        super().__init__()
        self.froggy = froggy
        self.instanciar_timer_autos_troncos()

    def instanciar_timer_autos_troncos(self):
        self.timer_salida_autos = QTimer(self)
        self.timer_salida_autos.setInterval(p.TIEMPO_AUTOS) 
        self.timer_salida_autos.timeout.connect(self.enviar_auto)   
        self.timer_salida_troncos = QTimer(self)
        self.timer_salida_troncos.setInterval(p.TIEMPO_TRONCOS) 
        self.timer_salida_troncos.timeout.connect(self.enviar_tronco)   
        self.timer_ronda = QTimer(self)
        self.timer_ronda.setInterval(1000) 
        self.timer_ronda.timeout.connect(self.cambiar_tiempo)   
        self.timer_objetos = QTimer(self)
        self.timer_objetos.setInterval(p.TIEMPO_OBJETOS) 
        self.timer_objetos.timeout.connect(self.mandar_objeto) 
        
    def mandar_objeto(self):
        objeto = choice((1, 2 ,3 ,4))
        x = randint(p.EXTREMO_IZQUIERDA_FROGGY, p.EXTREMO_DERECHA_FROGGY)
        y = randint(p.EXTREMO_RIO_SUPERIOR, p.EXTREMO_ABAJO_FROGGY)
        for obj in self.objetos:
            if x - 30 <= obj[0].x() <= x + 30 or y - 20 <= obj[0].y() <= y + 20:
                x = randint(p.EXTREMO_IZQUIERDA_FROGGY, p.EXTREMO_DERECHA_FROGGY)
                y = randint(p.EXTREMO_RIO_SUPERIOR, p.EXTREMO_ABAJO_FROGGY)
        self.senal_generar_objeto.emit(objeto, x, y, self.nivel)
        self.objeto = QRect(x, y, *p.TAMANO_OBJETO)
        self.objetos.append((self.objeto, objeto))
    
    def revisar_objeto(self):
        for indice in range(len(self.objetos)):
            if self.froggy.bloque_froggy.intersects(self.objetos[indice][0]):
                if self.objetos[indice][1] == 1:
                    self.contador_calaveras += 1
                    self.senal_cambiar_velocidad_troncos.emit()
                elif self.objetos[indice][1] == 2:
                    self.vidas += 1
                    self.senal_actualizar_vidas.emit(self.vidas)
                elif self.objetos[indice][1] == 3:
                    self.monedas += p.CANTIDAD_MONEDAS
                    self.senal_actualizar_monedas.emit(self.monedas)
                else:
                    tiempo_adicional = (10*(self.tiempo/self.tiempo_ronda)) // 1
                    self.tiempo += tiempo_adicional
                    self.senal_actualizar_tiempo.emit(self.tiempo)
                self.senal_borrar_objeto.emit(indice)
                self.objetos.pop(indice)
                break
    
    def vidas_trampa(self):
        self.vidas += p.VIDAS_TRAMPA
        self.senal_actualizar_vidas.emit(self.vidas)
    
    def cambiar_tiempo(self):
        if self.tiempo > 0:
            self.senal_actualizar_tiempo.emit(self.tiempo - 1)
            self.tiempo -= 1
        else:
            self.perder_ronda()

    def enviar_auto(self):
        self.senal_generar_auto.emit(self.velocidad_autos, self.nivel)

    def enviar_tronco(self):
        valor_calaveras = 1.05 ** self.contador_calaveras
        self.senal_generar_tronco.emit(self.velocidad_troncos * valor_calaveras, self.nivel)

    def revisar_colision(self, caja, cambio_nivel):
        if cambio_nivel == False:
            if self.froggy.bloque_froggy.intersects(caja):
                self.perder_ronda()
    
    def revisar_froggy_tronco(self, caja, d, cambio_nivel):
        if cambio_nivel == False:
            if self.froggy.bloque_froggy.intersects(caja):
                self.froggy.en_tronco = True
                x = self.froggy.bloque_froggy.x()
                y = self.froggy.bloque_froggy.y()
                bloque_d = QRect(x + p.VELOCIDAD_CAMINAR, y, *p.TAMANO_FROGGY)
                bloque_i = QRect(x - p.VELOCIDAD_CAMINAR, y, *p.TAMANO_FROGGY)
                bloque_a = QRect(x, y - p.VELOCIDAD_CAMINAR, *p.TAMANO_FROGGY)
                bloque_ab = QRect(x, y + p.VELOCIDAD_CAMINAR, *p.TAMANO_FROGGY)
                if self.froggy.bloque_froggy.x() < 2 or self.froggy.bloque_froggy.x() > 600:
                    self.perder_ronda()
                    print("PERDIÓ")
                if bloque_d.intersects(caja):
                    self.froggy.mov_tronco_d = True
                else:
                    self.froggy.mov_tronco_d = False
                if bloque_i.intersects(caja):
                    self.froggy.mov_tronco_i = True
                else:
                    self.froggy.mov_tronco_i = False
                if bloque_a.intersects(caja):
                    self.froggy.mov_tronco_a = True
                else:
                    self.froggy.mov_tronco_a = False
                if bloque_ab.intersects(caja):
                    self.froggy.mov_tronco_ab = True
                else:
                    self.froggy.mov_tronco_ab = False
                if d == "D":
                    self.froggy.bloque_froggy.translate(self.velocidad_troncos, 0)
                    self.senal_froggy_tronco.emit("D")
                elif d == "I":
                    self.froggy.bloque_froggy.translate(- self.velocidad_troncos, 0)
                    self.senal_froggy_tronco.emit("I")

    def iniciar_juego_inicio(self):
        self.vidas = p.VIDAS_INICIO
        self.tiempo_ronda = p.DURACION_RONDA_INICIAL
        self.tiempo = p.DURACION_RONDA_INICIAL
        self.puntaje = 0 
        self.puntaje_nivel = 0
        self.nivel = 1
        self.monedas = 0 
        self.velocidad_autos = p.VELOCIDAD_AUTOS
        self.velocidad_troncos = p.VELOCIDAD_TRONCOS
        self.contador_calaveras = 0 
        self.objetos = []
        self.enviar_auto()
        self.enviar_tronco()
        self.timer_salida_autos.start()
        self.timer_salida_troncos.start()
        self.timer_ronda.start()
        self.timer_objetos.start()

    def iniciar_juego(self):
        self.objetos = []
        self.contador_calaveras = 0 
        self.enviar_auto()
        self.enviar_tronco()
        self.timer_salida_autos.start()
        self.timer_salida_troncos.start()
        self.timer_ronda.start()
        self.timer_objetos.start()

    def salir_juego(self):
        self.timer_ronda.stop()
        self.timer_salida_autos.stop()
        self.timer_salida_troncos.stop()
        self.timer_objetos.stop()
        self.senal_limpiar_listas.emit()
        self.senal_cerrar_ventana.emit()
        self.senal_final.emit(self.nivel, self.puntaje, self.puntaje_nivel, self.vidas, self.monedas)
    
    def pausar(self):
        self.timer_ronda.stop()
        self.timer_salida_autos.stop()
        self.timer_salida_troncos.stop()
        self.timer_objetos.stop()

    def reanudar(self):
        self.timer_ronda.start()
        self.timer_salida_autos.start()
        self.timer_salida_troncos.start()
        self.timer_objetos.start()

    def perder_ronda(self):
        self.timer_ronda.stop()
        self.vidas -= 1
        if self.vidas == 0: 
            self.timer_salida_autos.stop()
            self.timer_salida_troncos.stop()
            self.timer_objetos.stop()
            self.senal_limpiar_listas.emit()
            self.senal_cerrar_ventana.emit()
            self.senal_final.emit(self.nivel, self.puntaje, self.puntaje_nivel, self.vidas, self.monedas)
        else:
            self.senal_actualizar_vidas.emit(self.vidas)
            self.froggy.bloque_froggy = QRect(*p.POSICION_INICIAL_FROGGY)
            self.senal_froggy_inicial.emit()
            self.tiempo = self.tiempo_ronda
            self.timer_ronda.start()

    def ganar_ronda(self):
        self.timer_ronda.stop()
        self.timer_salida_autos.stop()
        self.timer_salida_troncos.stop()
        self.timer_objetos.stop()
        self.senal_limpiar_listas.emit()
        self.puntaje_nivel = (self.vidas * 100 + self.tiempo * 50) * self.nivel
        self.puntaje = self.puntaje + self.puntaje_nivel
        self.nivel += 1 
        self.senal_actualizar_nivel.emit(self.nivel)
        self.tiempo_ronda = int((self.tiempo_ronda * p.PONDERADOR_DIFICULTAD) // 1)
        self.tiempo = self.tiempo_ronda
        self.velocidad_autos = int((self.velocidad_autos * 2 /(1 + p.PONDERADOR_DIFICULTAD)) // 1) 
        self.velocidad_troncos = int(
                                 (self.velocidad_troncos * 2 /(1 + p.PONDERADOR_DIFICULTAD)) // 1
                                    ) 
        self.froggy.bloque_froggy = QRect(*p.POSICION_INICIAL_FROGGY)
        self.senal_cerrar_ventana.emit()
        self.senal_abrir_ventana.emit(self.nivel - 1, self.puntaje, self.puntaje_nivel, self.vidas, self.monedas)
        
class Froggy(QObject):

    senal_moverse = pyqtSignal(tuple)
    senal_ganar_ronda = pyqtSignal()
    senal_movimiento_troncos = pyqtSignal()
    senal_perder_ronda = pyqtSignal()
    senal_revisar_objeto = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.pos = True
        self.contador_a = 0 
        self.contador_d = 0 
        self.contador_i = 0 
        self.contador_ab = 0 
        self.en_tronco = False
        self.mov_tronco_a = False
        self.mov_tronco_d = False
        self.mov_tronco_i = False
        self.mov_tronco_ab = False
        self.salto_tronco = False
        self.bloque_froggy = QRect(*p.POSICION_INICIAL_FROGGY)

    def revisar_movimiento(self, tupla):
        if tupla[0] == "A":
            if p.EXTREMO_RIO_INFERIOR <= tupla[2] - p.VELOCIDAD_CAMINAR <= p.EXTREMO_RIO_SUPERIOR:
                if self.mov_tronco_a:
                    self.bloque_froggy.translate(0, - p.VELOCIDAD_CAMINAR)
                    self.senal_moverse.emit(("A", self.contador_a % 3, p.VELOCIDAD_CAMINAR))
                    self.mov_tronco_a = False
                else:
                    self.senal_perder_ronda.emit()
            elif tupla[2] - p.VELOCIDAD_CAMINAR <= p.EXTREMO_ARRIBA_FROGGY:
                self.bloque_froggy.translate(0, - p.VELOCIDAD_CAMINAR)
                self.senal_moverse.emit(("A", self.contador_a % 3, p.VELOCIDAD_CAMINAR))
                self.senal_ganar_ronda.emit()
            else:
                self.senal_moverse.emit(("A", self.contador_a % 3, p.VELOCIDAD_CAMINAR))
                self.bloque_froggy.translate(0, - p.VELOCIDAD_CAMINAR)
                self.senal_revisar_objeto.emit()
            self.contador_a += 1
            self.contador_d = 0
            self.contador_i = 0
            self.contador_ab = 0

        elif tupla[0] == "D":
            if p.EXTREMO_RIO_INFERIOR <= tupla[2] <= p.EXTREMO_RIO_SUPERIOR:
                if self.mov_tronco_d:
                    self.bloque_froggy.translate(p.VELOCIDAD_CAMINAR, 0)
                    self.senal_moverse.emit(("D", self.contador_d % 3, p.VELOCIDAD_CAMINAR))
                    self.mov_tronco_d = False
                else:
                    self.senal_perder_ronda.emit()
            elif tupla[1] + p.VELOCIDAD_CAMINAR <= p.EXTREMO_DERECHA_FROGGY:
                self.bloque_froggy.translate(p.VELOCIDAD_CAMINAR, 0)
                self.senal_moverse.emit(("D", self.contador_d % 3, p.VELOCIDAD_CAMINAR))
                self.senal_revisar_objeto.emit()
            self.contador_d += 1
            self.contador_a = 0
            self.contador_i = 0
            self.contador_ab = 0

        elif tupla[0] == "I": 
            if p.EXTREMO_RIO_INFERIOR <= tupla[2] <= p.EXTREMO_RIO_SUPERIOR:
                if self.mov_tronco_i:
                    self.bloque_froggy.translate(- p.VELOCIDAD_CAMINAR, 0) 
                    self.senal_moverse.emit(("I", self.contador_i % 3, p.VELOCIDAD_CAMINAR))
                    self.mov_tronco_i = False
                else:
                    self.senal_perder_ronda.emit()
            elif tupla[1] - p.VELOCIDAD_CAMINAR >= p.EXTREMO_IZQUIERDA_FROGGY:
                self.senal_moverse.emit(("I", self.contador_i % 3, p.VELOCIDAD_CAMINAR))
                self.bloque_froggy.translate(- p.VELOCIDAD_CAMINAR, 0)
                self.senal_revisar_objeto.emit()
            self.contador_i += 1
            self.contador_d = 0
            self.contador_a = 0
            self.contador_ab = 0

        elif tupla[0] == "AB": 
            if p.EXTREMO_RIO_INFERIOR <= tupla[2] <= p.EXTREMO_RIO_SUPERIOR:
                if self.mov_tronco_ab:
                    self.bloque_froggy.translate(0, p.VELOCIDAD_CAMINAR)
                    self.senal_moverse.emit(("AB", self.contador_ab % 3, p.VELOCIDAD_CAMINAR))
                    self.mov_tronco_ab = False
                else:
                    self.senal_perder_ronda.emit()
            elif tupla[2] + p.VELOCIDAD_CAMINAR <= p.EXTREMO_ABAJO_FROGGY:
                self.bloque_froggy.translate(0, p.VELOCIDAD_CAMINAR)
                self.senal_moverse.emit(("AB", self.contador_ab % 3, p.VELOCIDAD_CAMINAR))
                self.senal_revisar_objeto.emit()
            self.contador_ab += 1
            self.contador_d = 0
            self.contador_i = 0
            self.contador_a = 0              

        elif tupla[0] == "S":
            if p.EXTREMO_RIO_INFERIOR <= tupla[2] <= p.EXTREMO_RIO_SUPERIOR:
                if self.en_tronco:
                    self.en_tronco = False
                    if self.contador_a >= 1:
                        if tupla[2] - p.PIXELES_SALTO <= p.EXTREMO_ARRIBA_FROGGY:
                            self.bloque_froggy.translate(0, - p.PIXELES_SALTO) 
                            self.senal_moverse.emit(("A", self.contador_a, p.PIXELES_SALTO))
                            self.senal_ganar_ronda.emit()
                        else:
                            self.senal_moverse.emit(("A", self.contador_a, p.PIXELES_SALTO))
                            self.bloque_froggy.translate(0, -p.PIXELES_SALTO)
                    
                    elif self.contador_ab >= 1:
                        if tupla[2] + p.PIXELES_SALTO <= p.EXTREMO_ABAJO_FROGGY:
                            self.bloque_froggy.translate(0, p.PIXELES_SALTO)
                            self.senal_moverse.emit(("AB", self.contador_ab, p.PIXELES_SALTO))
                else:
                    self.senal_perder_ronda.emit()  

            else:
                if self.contador_a >= 1:
                    if tupla[2] - p.PIXELES_SALTO <= p.EXTREMO_ARRIBA_FROGGY:
                        self.bloque_froggy.translate(0, - p.PIXELES_SALTO)
                        self.senal_moverse.emit(("A", self.contador_a, p.PIXELES_SALTO))
                        self.senal_ganar_ronda.emit()
                    else:
                        self.senal_moverse.emit(("A", self.contador_a, p.PIXELES_SALTO))
                        self.bloque_froggy.translate(0, - p.PIXELES_SALTO)
                        self.senal_revisar_objeto.emit()
                
                elif self.contador_d >= 1:
                    if tupla[1] + p.PIXELES_SALTO <= p.EXTREMO_DERECHA_FROGGY:
                        self.bloque_froggy.translate(p.PIXELES_SALTO, 0)
                        self.senal_moverse.emit(("D", self.contador_d, p.PIXELES_SALTO))
                        self.senal_revisar_objeto.emit()

                elif self.contador_i >= 1:
                    if tupla[1] - p.PIXELES_SALTO >= p.EXTREMO_IZQUIERDA_FROGGY:
                        self.senal_moverse.emit(("I", self.contador_i, p.PIXELES_SALTO))
                        self.bloque_froggy.translate(- p.PIXELES_SALTO, 0)
                        self.senal_revisar_objeto.emit()

                elif self.contador_ab >= 1:
                    if tupla[2] + p.PIXELES_SALTO <= p.EXTREMO_ABAJO_FROGGY:
                        self.bloque_froggy.translate(0, p.PIXELES_SALTO)
                        self.senal_moverse.emit(("AB", self.contador_ab, p.PIXELES_SALTO))
                        self.senal_revisar_objeto.emit()