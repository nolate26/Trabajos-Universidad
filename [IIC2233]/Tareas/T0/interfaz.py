# Código en el cual se ejecuta el programa
# IMPORTS
import lecturas_archivos # archivo contiene todas las funciones que se ejecutan


# CREACIÓN DE LA INTERFAZ DE LOS MENÚS DEL PROGRAMA:

# MENU DE INICIO
def menu_inicio():
    print("\n***¡Bienvenidos al DCCommerce!***\n\n---- Menu de Inicio ----\n")
    print("[1] Ingresar con sesión\n[2] Registrar nuevo usuario")
    print("[3] Ingresar como usuario anónimo\n[4] Salir\n")
    respuesta = input("Seleccione una opción: ")
    return respuesta

# MENU PRINCIPAL
def menu_principal(registrado, nombre_usuario):
    indice_principal = True
    while indice_principal == True:    
        print("\n---- Menú Principal ----\n")
        print("[1] Menú de Publicaciones\n[2] Menú de Publicaciones Realizadas\n[3] Volver\n")
        r_menup = input("Seleccione una opción: ")
        if r_menup == "1":
            menu_publicaciones(True, nombre_usuario)
            #IR AL MENÚ DE PUBLICACIONES
        elif r_menup == "2":
            menu_preguntas_realizadas(nombre_usuario)
            #IR AL MENÚ DE PUBLICACIONES REALIZADAS
        elif r_menup == "3":
            indice_principal = False
            #VOLVER AL MENÚ DE INICIO
        else:
            print("La respuesta no es válida, inténtelo nuevamente.")

#MENU DE PUBLICACIONES
def menu_publicaciones(registrado, nombre_usuario):
    indice_mpublicacion = True
    while indice_mpublicacion == True:
        print("\n---- Menú de Publicaciones ----\n")
        lista_publicaciones = lecturas_archivos.lista_publicaciones()
        #ORDENAMOS DE FORMA DESCENDENTE
        for indice in range(len(lista_publicaciones)):
            print(f"[{indice + 1}] {lista_publicaciones[-(indice+1)][1]}")
        print(f"[{len(lista_publicaciones)+1}] Volver")
        respuesta = input("Indique su opción: ")
        #SI RESPONDE OTRA COSA, QUE LO INTENTE NUEVAMENTE
        for letra in respuesta:
            if letra not in "1234567890":
                respuesta = 0
        if respuesta == "":
            respuesta = 0
        #SI RESPONDE NÚMEROS
        if 1 <= int(respuesta) <= len(lista_publicaciones):
            lecturas_archivos.publicacion(registrado, int(respuesta), nombre_usuario)
            #SE DIRIGE AL SUBMENÚ EN QUE SE VISUALIZA LA PUBLICACIÓN
        elif int(respuesta) == (len(lista_publicaciones)+1):
            indice_mpublicacion = False
            #VUELVE AL MENÚ PRINCIPAL
        else:
            print("La respuesta no es válida, inténtelo nuevamente.")

#MENU DE PREGUNTAS REALIZADAS
def menu_preguntas_realizadas(nombre_usuario):
    indice_menu_prealizadas = True
    while indice_menu_prealizadas == True:
        print("\n---- Menú de Publicaciones Realizadas ----\n\nMis publicaciones:")
        lista_publicaciones = lecturas_archivos.lista_publicaciones()
        for venta in lista_publicaciones:
            if venta[2] == nombre_usuario:
                print(f"- {venta[1]}")
        print("\n[1] Crear nueva publicación\n[2] Eliminar publicación\n[3] Volver")
        respuesta = input("\nIndique su opción: ")
        if respuesta == "1":
            lecturas_archivos.crear_publicacion(nombre_usuario)
            #SE EJECUTA FUNCIÓN PARA CREAR PUBLICACIÓN
        elif respuesta == "2":
            lecturas_archivos.eliminar_publicacion(nombre_usuario)
            #SE EJECUTA FUNCIÓN PARA ELIMINAR PUBLICACIÓN
        elif respuesta == "3":
            indice_menu_prealizadas = False
            #VUELVE AL MENÚ PRINCIPAL
        else:
            print("La respuesta no es válida, inténtelo nuevamente.")

            
#Código principal para iniciar el programa
#lo que se ejecuta
def inicio_programa():
    programa = True
    while programa == True:
        respuesta = menu_inicio()
        if respuesta == "1":
            print("\n*Recuerde escribir su usuario con las mayúsculas y signos correspondientes*")
            nombre_usuario = input("Nombre de usuario: ")
            es_usuario = lecturas_archivos.revisar_usuario(nombre_usuario)
            #REVISAR QUE USUARIO SE ENCUENTRE EN USUARIOS.CSV
            if es_usuario:
                menu_principal(True, nombre_usuario)
                #LO DIRIGE AL MENU PRINCIPAL
            else:
                print("\nEste usuario no existe, regístrese, ingrese como anónimo o intente nuevamente.\
                \n")
        elif respuesta == "2":
            print("\n*El nombre no debe contener ',' y debe ser de un máximo de 15 caracteres*")
            nombre_usuario = input("Nombre de usuario a crear: ")
            condicion = lecturas_archivos.condiciones_usuario(nombre_usuario)
            #REVISAR QUE USUARIO CUMPLA CON TODAS LAS CONDICIONES PARA CREAR USUARIO
            if condicion == True:
                lecturas_archivos.agregar_usuario(nombre_usuario) #se agrega a usuarios.csv
                menu_principal(True, nombre_usuario) #dirige al menú principal
        elif respuesta == "3":
            menu_publicaciones(False, "") #va directo al menu de publicaciones
            #entrar al menu con menos funcionalidades
        elif respuesta == "4":
            programa = False
            print("\nGracias por confiar en el DCCCOMERCE, que tenga un buen día.")
        else:
            print("La respuesta no es válida, inténtelo nuevamente.")

#Código para ejecución:
inicio_programa()