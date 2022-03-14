#Importamos los archivos y modulos 
import lectura_archivos
import tributos
import parametros as p
from arena import Arena
from simulaciones import simulacion_hora, resumen

# Menú de inicio 
def menu_inicio():
    # Desplegamos el menú 
    menu_inicio = True
    while menu_inicio:
        print(f'\n*** Menú de Inicio ***\n{"-"*22}' 
            '\n[1] Iniciar partida'
            '\n[2] Salir')
        input_usuario_menu_inicio = input("\nIngrese su opción elegida: ")
        #Ahora que tenemos el input del usuario, podemos pedirle a nuestra función que lo valide
        try:
            validar_input = p.manejar_input(input_usuario_menu_inicio, 2)
        except (ValueError, IndexError) as error:
            print(error)
            validar_input = False
        if validar_input:
            #Si quiere salir
            if input_usuario_menu_inicio == "2":
                break
            #si inicia partida - elige personaje
            else:
                eleccion = eleccion_personaje()
                if eleccion == "salir":
                    break

# Se elige el personaje  
def eleccion_personaje():
    # Desplegamos el menú
    eleccion_personaje = True
    while eleccion_personaje:
        lista_tributos = lectura_archivos.lista_tributos()
        print(f'\n   Escoje tu Tributo para el DCCapitolio\n{"-"*45}')
        print(f'{" "*4} Nombre Tributo -- Distrito')
        for contador in range(len(lista_tributos)):
            print(f'[{contador + 1}] {lista_tributos[contador].nombre} --'
                  f' {lista_tributos[contador].distrito}') 
        print(f'[{len(lista_tributos) + 1}] Volver')
        print(f'[{len(lista_tributos) + 2}] Salir')
        # Pedimos la respuesta
        input_usuario_personaje = input("\nIngrese su opción elegida: ")
        #Ahora que tenemos el input del usuario, podemos pedirle a nuestra función que lo valide
        try:
            validar_input = p.manejar_input(input_usuario_personaje, len(lista_tributos) + 2)
        except (ValueError, IndexError) as error:
            print(error)
            validar_input = False
        if validar_input:
            # Caso en que selecciona salir
            if input_usuario_personaje == str(len(lista_tributos) + 2):
                return "salir"
            # Caso de volver
            elif input_usuario_personaje == str(len(lista_tributos) + 1):
                return "volver"
            # Tributo elegido
            else:
                # Elegimos al tributo escogido
                num_tributo_elegido = int(input_usuario_personaje) - 1
                tributo_elegido = lista_tributos.pop(num_tributo_elegido)
                # Pasamos a elegir arena dando el tributo elegido y los demás tributos
                eleccion = eleccion_arena(tributo_elegido, lista_tributos)
                if eleccion == "salir":
                    # Se sale del programa
                    return "salir"
                elif eleccion == "menu_inicio":
                    # Se dirige al menu de inicio
                    return "menu_inicio"

# Se elige la arena
def eleccion_arena(jugador, tributos):
    # desplegamos el menú
    eleccion_arena = True          
    while eleccion_arena:
        pre_arenas = lectura_archivos.arenas()
        print(f'\n   Arena en la que deseas jugar\n{"-"*36}')
        print(f'{" "*4} Nombre Arena -- Dificultad')
        contador = 1
        for lugar in pre_arenas:
            print(f'[{contador}] {lugar[0]} -- {lugar[1]}')
            contador += 1
        print(f'[{contador}] Volver')
        print(f'[{contador + 1}] Salir')
        # Usuario selecciona opción
        input_arena = input("\nIngrese su opción elegida: ")
        # Verificamos si está correcto
        try:
            validar_input = p.manejar_input(input_arena, contador + 1)
        except (ValueError, IndexError) as error:
            print(error)
            validar_input = False
        if validar_input:
            # Si desea salir
            if input_arena == str(contador + 1):
                return "salir"
            # Si quiere volver a elegir tributo
            elif input_arena == str(contador):
                return "volver"
            else:
                # Recopilamos datos para crear arena
                valor =  int(input_arena) - 1
                lista_ambientes = lectura_archivos.ambientes() 
                eleccion = menu_principal(pre_arenas[valor], jugador, tributos, 
                                            lista_ambientes)
                # Si desea salir
                if eleccion == "salir":
                    return "salir"
                # Si desea ir al menu de inicio
                elif eleccion == "menu_inicio":
                    return "menu_inicio"

def menu_principal(datos_arenas, jugador, tributos, ambientes):
    # Menú principal
    print("\n--- COMENZÓ EL DCCAPITOLIO ---")
    # Se genera la arena
    arena = Arena(datos_arenas[0], float(datos_arenas[2]), datos_arenas[1], 
                            jugador, tributos, ambientes)
    # Despliega el menú                        
    menu_principal = True
    while menu_principal:
        print(f'\n*** Menú Principal ***\n{"-"*22}'
            '\n[1] Simulación hora'
            '\n[2] Mostrar estado del tributo'
            '\n[3] Utilizar objeto'
            '\n[4] Resumen DCCapitolio'
            '\n[5] Rendirse'
            '\n[6] Salir')
        input_usuario_menu_principal = input("Ingrese su opción elegida: ")
        # Verificamos input
        try:
            validar_input = p.manejar_input(input_usuario_menu_principal, 6)
        except (ValueError, IndexError) as error:
            print(error)
            validar_input = False
        # Opciones del menú principal
        if validar_input:
            if input_usuario_menu_principal == "1":
                # Se simula una hora
                arena = simulacion_hora(arena)
            elif input_usuario_menu_principal == "2":
                # Muestra el estado del tributo
                print(arena.jugador)
            elif input_usuario_menu_principal == "3":
                # Utiliza objeto (si es que tiene)
                arena.jugador.utilizar_objeto(arena.riesgo)
            elif input_usuario_menu_principal == "4":
                # Muestra el resumen de los tributos
                resumen(arena)
            elif input_usuario_menu_principal == "5":
                #vuelve al menú inicio -> RETIRARSE
                return "menu_inicio"
            elif input_usuario_menu_principal == "6":
                # Sale
                return "salir"    
        # Si el jugador muere - termino de juego 
        if arena.jugador.vida <= 0:
            print(f"\nTu jugador '{arena.jugador.nombre}' ha muerto :((((("
                  f"\nANIMO! Perdiste una batalla, pero no la GUERRA\n")
            return "menu_inicio"
        # Si los tributos mueren - término de juego
        elif arena.tributos == []:
            print(f'\n{arena.jugador.nombre} ¡¡¡ GANASTE EL DCCAPITOLIO !!!'
                   '\nHan muerto todos los demás, felicitaciones\n') 
            return "menu_inicio"

menu_inicio()
print("\n¡Gracias por participar!\nHasta la próxima...")