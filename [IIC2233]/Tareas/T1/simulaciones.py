import parametros as p

def simulacion_hora(arena):
    menu_simulacion = True
    texto_encuentros = ""
    texto_muertos = ""
    # Desplegamos menú
    while menu_simulacion:
        print(f'\n    Simulación de hora    \n{"-"*26}' 
            '\n[1] Acción heroica'
            '\n[2] Atacar a un tributo'
            '\n[3] Pedir objeto a patrocinadores'
            '\n[4] Hacerse bolita'
            '\n[5] Volver')
        input_simulacion = input("\nIngrese su opción elegida: ")
        #Ahora que tenemos el input del usuario, podemos pedirle a nuestra función que lo valide
        try:
            validar_input = p.manejar_input(input_simulacion, 5)
        except (ValueError, IndexError) as error:
            print(error)
            validar_input = False
        if validar_input:
            # Realizamos la acción heroica
            if input_simulacion == "1":
                menu_simulacion = arena.jugador.accion_heroica()
                opcion_escogida = "Acción Heroica"
            # Atacamos a personaje
            elif input_simulacion == "2":
                eleccion_personaje = True
                # Desplegamos menú
                while eleccion_personaje:
                    print(f'\n    Escoje el tributo a atacar\n{"-"*38}')
                    print(f'{" "*4} Nombre Tributo -- Distrito')
                    for contador in range(len(arena.tributos)):
                        print(f'[{contador + 1}] {arena.tributos[contador].nombre} --'
                              f' {arena.tributos[contador].distrito}') 
                    print(f"[{len(arena.tributos) + 1}] Volver")
                    #opción escogida
                    input_personaje = input("\nIngrese su opción elegida: ")
                    # Validamos elección
                    try:
                        validar_input = p.manejar_input(input_personaje, len(arena.tributos) + 1)
                        #revisar
                    except (ValueError, IndexError) as error:
                        print(error)
                        validar_input = False
                    # Si es válida la desición
                    if validar_input:
                        # Se realiza ataque
                        if not input_personaje == str(len(arena.tributos) + 1):    
                            num_tributo_elegido = int(input_personaje) - 1
                            tupla = arena.jugador.atacar(arena.tributos[num_tributo_elegido])
                            if tupla[0] == True:
                                # Analizamos si murió
                                tupla1 = revisar_muertos(arena)
                                arena = tupla1[0]
                                texto_muertos += tupla1[1]
                                # Si murieron todos
                                if final_dccapitolio(arena) == "final":
                                    return arena
                                menu_simulacion = False
                                eleccion_personaje = False
                                opcion_escogida = "Atacar a un Tributo"
                                texto_encuentros += tupla[1]
                            else:
                                eleccion_personaje = False
                        # Si desea volver al menú principal
                        else:
                            eleccion_personaje = False
            # Si quiere pedir objeto a los patrocinadores
            elif input_simulacion == "3":
                # llama al método
                menu_simulacion = arena.jugador.pedir_objeto(arena)
                opcion_escogida = "Pedir objeto a patrocinadores"
            # Si quiere hacerse bolita
            elif input_simulacion == "4":
                # Se ejecuta el método
                menu_simulacion = arena.jugador.hacerse_bolita()
                opcion_escogida = "Hacerse bolita"
            # Si decide volver
            elif input_simulacion == "5":
                return arena        
    #ENCUENTROS ENTRE TRIBUTOS
    for encuentro in range( int((arena.riesgo * len(arena.tributos)) // 2)):
        # Realizamos encuentros
        texto_encuentros += arena.encuentro()
        # Revisamos si alguien murió
        tupla = revisar_muertos(arena)
        arena = tupla[0]
        texto_muertos += tupla[1]
        # Vemos si termina el juego
        if final_dccapitolio(arena) == "final":
            return arena
    #EJECUTAR EVENTO SI SE CUMPLE PROBABILIDAD
    texto_evento = arena.ejecutar_evento()
    for tributo in range(len(arena.tributos)):
        # Revisamos si alguien murió
        tupla = revisar_muertos(arena)
        arena = tupla[0]
        texto_muertos += tupla[1]
        # Revisamos si se termina
        if final_dccapitolio(arena) == "final":
            return arena
    # MOSTRAMOS EL RESUMEN
    texto_tributos_vida = f'{arena.jugador.nombre}\n'
    for tributo in arena.tributos:
        texto_tributos_vida += f'{tributo.nombre}\n'
    if texto_muertos == '':
        texto_muertos = "No murió ningún tributo"
    print(f'\n{" "*17}Resumen\n{"-"*50}' 
          f'\nOpción escogida al simular: {opcion_escogida}\n'
          f'\nEncuentros ocurridos:\n{texto_encuentros}'
          f'\nTributos derrotados:\n{texto_muertos}\n'
          f'\nTributos que siguen con vida:\n{texto_tributos_vida}'
          f'\n{texto_evento}')
    return arena

# FUNCIÓN DE MOSTERAR EL RESUMEN EN EL MENU-PRINCIPAL
def resumen(arena):
    if arena.contador_ciclo == 0:
        ambiente = "Playa"
    elif arena.contador_ciclo == 1:
        ambiente = "Montaña"
    else:
        ambiente = "Bosque"
    print(f'\n           Estado DCCapitolio\n{"-"*45}'
          f'\nDificultad: {arena.dificultad}\n'
          f'\nTributos vivos -- Cantidad de vida'
          f'\n{arena.jugador.nombre} -- {arena.jugador.vida}')
    for tributo in arena.tributos:
        print(f'{tributo.nombre} -- {tributo.vida}')
    print(f"\nPróximo ambiente: {ambiente}")

# FUNCIÓN PARA REVISAR SI ALGUIEN MURIÓ
def revisar_muertos(arena):
    texto = ""
    for contador in range(len(arena.tributos)):
        if arena.tributos[contador].vida <= 0:
            tributo = arena.tributos.pop(contador)
            texto = f'{tributo.nombre}\n'
            return (arena, texto) 
    return(arena, texto)

# FUNCIÓN PARA VERIFICAR SI SE TERMINA EL JUEGO
def final_dccapitolio(arena):
    if arena.tributos == [] or arena.jugador.vida <= 0:
        return "final"