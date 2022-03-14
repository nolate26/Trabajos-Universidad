import os

# RUTAS DE VENTANAS
RUTA_UI_VENTANA_INICIO = os.path.join("extras", "qtdesigner", "ventana_inicio.ui")
RUTA_UI_VENTANA_RANKING = os.path.join("extras", "qtdesigner", "ventana_puntajes.ui")
RUTA_UI_VENTANA_JUEGO = os.path.join("extras", "qtdesigner", "ventana_juego.ui")
RUTA_UI_VENTANA_SIG_NIVEL = os.path.join("extras", "qtdesigner", "ventana_post_nivel1.ui")
RUTA_UI_VENTANA_SALIR = os.path.join("extras", "qtdesigner", "ventana_post_nivel2.ui")

# RUTAS DE AUTOS Y TRONCO
RUTA_AUTO_1 = os.path.join("sprites", "Mapa", "autos", "blanco_left.png")
RUTA_AUTO_2 = os.path.join("sprites", "Mapa", "autos", "amarillo_right.png")
RUTA_AUTO_3 = os.path.join("sprites", "Mapa", "autos", "rojo_left.png")
RUTA_AUTO_4 = os.path.join("sprites", "Mapa", "autos", "plata_right.png")
RUTA_AUTO_5 = os.path.join("sprites", "Mapa", "autos", "azul_left.png")
RUTA_AUTO_6 = os.path.join("sprites", "Mapa", "autos", "negro_right.png")
RUTA_TRONCO = os.path.join("sprites", "Mapa", "elementos", "tronco.png")

# RUTA PUNTAJES .txt
RUTA_PUNTAJES = os.path.join("puntajes.txt")

# RUTA FROGGY
RUTA_FROGGY_INICIAL = os.path.join("sprites", "Personajes", "Verde", "still.png")
RUTA_FROGGY_IZQUIERDA_DETENIDO = os.path.join("sprites", "Personajes", "Verde", "left_1.png")
RUTA_FROGGY_DERECHA_DETENIDO = os.path.join("sprites", "Personajes", "Verde", "right_1.png")
RUTA_FROGGY_ARRIBA_DETENIDO = os.path.join("sprites", "Personajes", "Verde", "up_1.png")
RUTA_FROGGY_ABAJO_DETENIDO = os.path.join("sprites", "Personajes", "Verde", "down_1.png")

RUTA_FROGGY_IZQUIERDA_MEDIO = os.path.join("sprites", "Personajes", "Verde", "left_2.png")
RUTA_FROGGY_DERECHA_MEDIO = os.path.join("sprites", "Personajes", "Verde", "right_2.png")
RUTA_FROGGY_ARRIBA_MEDIO = os.path.join("sprites", "Personajes", "Verde", "up_2.png")
RUTA_FROGGY_ABAJO_MEDIO = os.path.join("sprites", "Personajes", "Verde", "down_2.png")

RUTA_FROGGY_IZQUIERDA_FINAL = os.path.join("sprites", "Personajes", "Verde", "left_3.png")
RUTA_FROGGY_DERECHA_FINAL = os.path.join("sprites", "Personajes", "Verde", "right_3.png")
RUTA_FROGGY_ARRIBA_FINAL = os.path.join("sprites", "Personajes", "Verde", "up_3.png")
RUTA_FROGGY_ABAJO_FINAL = os.path.join("sprites", "Personajes", "Verde", "down_3.png")

# RUTA OBJETOS
RUTA_OBJETO_1 = os.path.join("sprites", "Objetos", "Calavera.png")
RUTA_OBJETO_2 = os.path.join("sprites", "Objetos", "Corazon.png")
RUTA_OBJETO_3 = os.path.join("sprites", "Objetos", "Moneda.png")
RUTA_OBJETO_4 = os.path.join("sprites", "Objetos", "Reloj.png")

# CARACTERES
MIN_CARACTERES = 5
MAX_CARACTERES = 15

# PARAMETROS DE INICIO DE LA PARTIDA 
VIDAS_INICIO = 3
DURACION_RONDA_INICIAL = 60
PONDERADOR_DIFICULTAD = 0.8
CANTIDAD_MONEDAS = 100
VIDAS_TRAMPA = 2


# TECLAS DE MOVIMIENTO, SALTO Y PAUSA
TECLA_ARRIBA = "w"
TECLA_IZQUIERDA = "a"
TECLA_ABAJO = "s"
TECLA_DERECHA = "d"
TECLA_SALTO = "j"
TECLA_PAUSA = "p"

# VELOCIDADES 
VELOCIDAD_AUTOS = 25
VELOCIDAD_TRONCOS = 20
VELOCIDAD_CAMINAR = 2
PIXELES_SALTO = 28

# POSICIONES INICIALES OBJETOS
POSICION_INICIAL_FROGGY = (280, 580, 25, 20)
POSICION_INICIAL_AUTO_1 = (580, 520, 60, 24)
POSICION_INICIAL_AUTO_2 = (-40, 488, 60, 24)
POSICION_INICIAL_AUTO_3 = (580, 455, 60, 24)
POSICION_INICIAL_AUTO_4 = (-40, 385, 60, 24)
POSICION_INICIAL_AUTO_5 = (580, 355, 60, 24)
POSICION_INICIAL_AUTO_6 = (-40, 320, 60, 24)
POSICION_INICIAL_TRONCO_1 = (-60, 250, 74, 22)
POSICION_INICIAL_TRONCO_2 = (585, 222, 74, 22)
POSICION_INICIAL_TRONCO_3 = (-60, 194, 74, 22)
POS_AUTO_1 = (580, 520)
POS_AUTO_2 = (-40, 488)
POS_AUTO_3 = (580, 455)
POS_AUTO_4 = (-40, 385)
POS_AUTO_5 = (580, 355)
POS_AUTO_6 = (-40, 320)
POS_TRONCO_1 = (585, 250)
POS_TRONCO_2 = (-60, 222)
POS_TRONCO_3 = (585, 194)

# TAMAÑOS OBJETOS
TAMANO_FROGGY = (25, 20)
TAMANO_AUTO = (60, 24)
TAMANO_TRONCO = (74, 22)
TAMANO_OBJETO = (25, 20)

# TIEMPOS DE APARICIONES
TIEMPO_AUTOS = 8000
TIEMPO_TRONCOS = 10000
TIEMPO_OBJETOS = 7000

# PARAMETROS EXTREMOS 
EXTREMO_IZQUIERDA_FROGGY = -5
EXTREMO_DERECHA_FROGGY = 580
EXTREMO_ABAJO_FROGGY = 580
EXTREMO_ARRIBA_FROGGY = 155
EXTREMO_RIO_SUPERIOR = 270
EXTREMO_RIO_INFERIOR = 175

