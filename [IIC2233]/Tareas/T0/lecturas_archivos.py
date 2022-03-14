#IMPORTS
import datetime
import os
from parametros import MAX_CARACTERES, MIN_CARACTERES

#Carga de paths relativos portables en variables no globales
def paths(nombre):
    path_usuarios = os.path.join('data', 'usuarios.csv')
    path_publicaciones = os.path.join('data', 'publicaciones.csv')
    path_comentarios = os.path.join('data', 'comentarios.csv')
    if nombre == "usuarios":
        return path_usuarios
    elif nombre == "publicaciones":
        return path_publicaciones
    elif nombre == "comentarios":
        return path_comentarios

#FUNCIONES USUARIOS
#crear lista de todos los usuarios
def lista_usuarios():
    with open(paths("usuarios"), 'rt', encoding = 'utf8') as archivo_usuarios: 
        data = archivo_usuarios.readlines()
    lista_usuarios = []
    for linea in data:
        nombre = linea.strip()
        lista_usuarios.append(nombre)
    lista_usuarios.pop(0) #borramos las categorizaciones
    return lista_usuarios

#revisar si usuario está en la lista
def revisar_usuario(nombre):
    lista = lista_usuarios()
    for persona in lista:
        if nombre == persona:
            return True
    return False

#agregar usuario en la lista escribiendo sobre el archivo
def agregar_usuario(nombre):
    archivo = open(paths("usuarios"), "a")
    archivo.write(f"\n{nombre}")
    archivo.close()


#FUNCIONES PUBLICACIONES
#lista de listas de publicaciones
def lista_publicaciones():
    with open(paths("publicaciones"), 'rt', encoding = 'utf8') as archivo_publicaciones:
        data = archivo_publicaciones.readlines()
    lista_publicaciones = []
    for linea in data:
        frase = linea.strip()
        info = frase.split(",", maxsplit=5)
        lista_publicaciones.append(info)
    lista_publicaciones.pop(0)
    return lista_publicaciones

#función para crear publicaciones
def crear_publicacion(nombre_usuario):
    nombre_p = input("\nNombre del producto: ")
    precio = input("Precio del producto: ")
    descripcion = input("Breve descripción: ")
    fecha = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    lista = lista_publicaciones()
    archivo = open(paths("publicaciones"), "a", encoding = 'utf8')
    archivo.write(f"\n{len(lista)+1},{nombre_p},{nombre_usuario},{fecha},{precio},{descripcion}")
    archivo.close() #se sobreescriben bajo el mismo formato

#función para eliminar publicaciones (incluye interfaz del menú)
def eliminar_publicacion(nombre_usuario):
    #INTERFAZ DEL MENÚ
    indice_eliminar = True
    while indice_eliminar == True:
        print("¿Qué publicación deseas eliminar?\n")
        lista_p = lista_publicaciones()
        contador = 1
        lista_eliminar = []
        for venta in lista_p:
            if venta[2] == nombre_usuario:
                lista_eliminar.append(venta)
                print(f"[{contador}] {venta[1]} -- Creado el {venta[3]}")
                contador += 1
        print(f"[{contador}] Volver")
        respuesta = input("\nIndique su opción: ")
        if contador == 1:
            if respuesta == "1":
                indice_eliminar = False
            else:
                print("La respuesta no es válida, inténtelo nuevamente.\n")
        else:
            #SI RESPONDE OTRA COSA, QUE LO INTENTE NUEVAMENTE
            for letra in respuesta:
                if letra not in "1234567890":
                    respuesta = 0
            if respuesta == "":
                respuesta = 0
            #SI RESPONDE NÚMEROS
            if 1 <= int(respuesta) < contador:
                eliminar_comentario(lista_eliminar[int(respuesta)-1][0])
                #SE ELIMINA PUBLICACIÓN ELEGIDA Y SE SOBREESCRIBE EL ARCHIVO SIN LA PUBLICACIÓN
                nueva_publicacion = []
                for indice in range(len(lista_p)):
                    if lista_p[indice] != lista_eliminar[int(respuesta)-1]:
                        nueva_publicacion.append(lista_p[indice])
                texto = "id_publicacion,nombre_publicacion,usuario,fecha_creacion,precio,descripcion\n"
                for lista in nueva_publicacion:
                    for indice1 in range(len(nueva_publicacion[0])):
                        texto += lista[indice1]
                        texto += ","
                    texto = texto[:len(texto)-1]
                    texto += "\n"
                texto = texto[:len(texto)-1] 
                nuevo_p = open(paths("publicaciones"), "w", encoding = 'utf8')
                nuevo_p.write(texto)
                nuevo_p.close()
            elif int(respuesta) == contador:
                indice_eliminar = False
            else:
                print("La respuesta no es válida, inténtelo nuevamente.\n")


#FUNCIONES COMENTARIOS
#lista de listas de comentarios
def lista_comentarios():
    with open(paths("comentarios"), 'rt', encoding = 'utf8') as archivo_comentarios:
        data = archivo_comentarios.readlines()
    lista_comentarios = []
    for linea in data:
        frase = linea.strip()
        info = frase.split(",", maxsplit=3)
        lista_comentarios.append(info)
    lista_comentarios.pop(0)
    return lista_comentarios
    
#Agregar comentario
def agregar_comentario(comentario, nombre_usuario, id):
    fecha = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    archivo = open(paths("comentarios"), "a", encoding = 'utf8')
    archivo.write(f"\n{id},{nombre_usuario},{fecha},{comentario}")
    archivo.close()

#Eliminar comentario
def eliminar_comentario(id):
    lista = lista_comentarios()
    nuevos_comentarios = []
    for comentario1 in lista:
        if comentario1[0] != id:
            nuevos_comentarios.append(comentario1)
    texto = "id_publicacion,usuario,fecha_emision,contenido\n"
    for comentario in nuevos_comentarios:
        for indice in range(len(nuevos_comentarios[0])):
            texto += comentario[indice]
            texto += ","
        texto = texto[:len(texto)-1]
        texto += "\n"
    texto = texto[:len(texto)-1]
    nuevo_c = open(paths("comentarios"), "w", encoding = 'utf8')
    nuevo_c.write(texto)
    nuevo_c.close() 


#FUNCIONES ESPECÍFICAS
#revisar que usuario logre registrarse correctamente
def condiciones_usuario(nombre):
    if len(nombre) > MAX_CARACTERES or len(nombre) < MIN_CARACTERES:
        print("El usuario debe tener entre 1 y 15 caracteres. Ingrese como anónimo o inténtelo\
 nuevamente.\n")
        return False
    nueva_palabra = ""
    for letra in nombre:
        if letra == ",":
            print("El usuario no debe contener ','. Ingrese como anónimo o inténtelo nuevamente.\n")
            return False
    for persona in lista_usuarios():
        if persona == nombre:
            print("Este usuario ya existe. Ingrese como anónimo o inténtelo nuevamente.\n")
            return False
    return True

#Interfaz al entrar a una publicación específica
def publicacion(registrado, respuesta, nombre_usuario):
    indice_publicacion = True
    while indice_publicacion == True:
        lista_p = lista_publicaciones()
        print(f"\n*** {lista_p[-(respuesta)][1]} ***\n")
        print(f"Creado: {lista_p[-respuesta][3]}\nVendedor: {lista_p[-respuesta][2]}\nPrecio: \
{lista_p[-respuesta][4]}\nDescripción: {lista_p[-respuesta][5]}\n\nComentarios de la publicación:")
        lista_comentario = lista_comentarios()
        for comentario in lista_comentario:
            if comentario[0] == lista_p[-respuesta][0]:
                print(f"{comentario[2]} -- {comentario[1]}: {comentario[3]}")
        if registrado == True:
            print("[1] Agregar comentario\n[2] Volver")
            resp = input("\nIndique su opción: ")
            if resp == "1":
                comentario = input("Ingrese el comentario: ")
                agregar_comentario(comentario, nombre_usuario, lista_p[-respuesta][0])
            elif resp == "2":
                indice_publicacion = False
            else:
                print("\nLa respuesta no es válida, inténtelo nuevamente.")    
        else:
            print("[1] Volver")
            resp = input("\nIndique su opción:")
            if resp == "1":
                indice_publicacion = False
            else:
                print("La respuesta no es válida, inténtelo nuevamente.")