import sys
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication

# import parametros as p
from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego, Froggy
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_ranking import VentanaRanking
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_siguiente_nivel import VentanaNivel
from frontend.ventana_final import VentanaFinal

if __name__ == '__main__':
    app = QApplication([])

    # # Instanciación de ventanas
    ventana_inicio = VentanaInicio()
    ventana_ranking = VentanaRanking()
    ventana_juego = VentanaJuego()
    ventana_final = VentanaFinal()

    # # Instanciación de lógica
    logica_inicio = LogicaInicio()
    froggy = Froggy()
    logica_juego = LogicaJuego(froggy)
    ventana_nivel = VentanaNivel()

    # # ~~ Conexiones de señales ~~
    # # Ventana Inicio
    ventana_inicio.senal_enviar_usuario.connect(logica_inicio.comprobar_usuario)
    ventana_inicio.senal_calcular_ranking.connect(logica_inicio.calcular_ranking)
    logica_inicio.senal_respuesta_validacion.connect(ventana_inicio.recibir_validacion)
    
    # # Ventana Rankings
    logica_inicio.senal_rankings_creados.connect(ventana_ranking.instalar_rankings)
    ventana_ranking.senal_volver.connect(ventana_inicio.mostrar)
    ventana_nivel.senal_enviar_puntaje.connect(ventana_ranking.guardar_puntaje)
    ventana_final.senal_enviar_puntaje.connect(ventana_ranking.guardar_puntaje)

    # # Ventana Juego
    logica_inicio.senal_abrir_juego.connect(ventana_juego.iniciar_juego)
    ventana_juego.senal_iniciar_juego_inicial.connect(logica_juego.iniciar_juego_inicio)
    ventana_juego.senal_iniciar_juego.connect(logica_juego.iniciar_juego)
    ventana_juego.senal_salir_juego.connect(logica_juego.salir_juego)
    ventana_juego.senal_revisar_tecla.connect(froggy.revisar_movimiento)
    froggy.senal_moverse.connect(ventana_juego.mover_froggy)
    logica_juego.senal_generar_auto.connect(ventana_juego.mover_auto)
    ventana_juego.senal_revisar_colision.connect(logica_juego.revisar_colision)
    logica_juego.senal_generar_tronco.connect(ventana_juego.mover_tronco)
    logica_juego.senal_generar_objeto.connect(ventana_juego.crear_objeto)
    ventana_juego.senal_revisar_froggy.connect(logica_juego.revisar_froggy_tronco)
    logica_juego.senal_froggy_tronco.connect(ventana_juego.mover_froggy_tronco)
    logica_juego.senal_actualizar_tiempo.connect(ventana_juego.cambiar_tiempo)
    logica_juego.senal_actualizar_vidas.connect(ventana_juego.cambiar_vidas)
    logica_juego.senal_actualizar_monedas.connect(ventana_juego.cambiar_monedas)
    logica_juego.senal_actualizar_nivel.connect(ventana_juego.cambiar_nivel)
    logica_juego.senal_borrar_objeto.connect(ventana_juego.ocultar_objeto)
    logica_juego.senal_froggy_inicial.connect(ventana_juego.froggy_inicial)
    logica_juego.senal_limpiar_listas.connect(ventana_juego.limpiar_listas)
    froggy.senal_ganar_ronda.connect(logica_juego.ganar_ronda)
    logica_juego.senal_cerrar_ventana.connect(ventana_juego.ocultar)
    froggy.senal_perder_ronda.connect(logica_juego.perder_ronda)
    froggy.senal_revisar_objeto.connect(logica_juego.revisar_objeto)
    logica_juego.senal_cambiar_velocidad_troncos.connect(ventana_juego.cambiar_velocidad_troncos)
    ventana_juego.senal_pausar.connect(logica_juego.pausar)
    ventana_juego.senal_reanudar.connect(logica_juego.reanudar)
    ventana_juego.senal_vidas_trampa.connect(logica_juego.vidas_trampa)
    ventana_juego.senal_terminar_nivel.connect(logica_juego.ganar_ronda)
    
    # # Ventana Nuevo nivel
    logica_juego.senal_abrir_ventana.connect(ventana_nivel.mostrar)
    ventana_nivel.senal_siguiente_nivel.connect(ventana_juego.nuevo_nivel)
    
    # # Ventana Final
    logica_juego.senal_final.connect(ventana_final.mostrar)
    ventana_nivel.senal_salir.connect(ventana_inicio.mostrar)
    ventana_final.senal_salir.connect(ventana_inicio.mostrar)

    ventana_inicio.mostrar()
    sys.exit(app.exec_())