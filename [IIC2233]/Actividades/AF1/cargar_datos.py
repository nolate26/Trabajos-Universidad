from mascota import Mascota, Perro, Gato, Conejo


def cargar_mascotas(archivo_mascotas):
    with open(archivo_mascotas, 'rt', encoding = 'utf8') as archivo: 
        data = archivo.readlines()
    lista_mascotas = []
    for linea in data:
        frase = linea.strip()
        info = frase.split(",")
        if info[1] == "gato":
            gato = Gato(info[0], info[2], info[3], int(info[4]), int(info[5]))
            lista_mascotas.append(gato)
        elif info[1] == "perro":
            perro = Perro(info[0], info[2], info[3], int(info[4]), int(info[5]))
            lista_mascotas.append(perro)
        elif info[1] == "conejo":
            conejo = Conejo(info[0], info[2], info[3], int(info[4]), int(info[5]))
            lista_mascotas.append(conejo)
    return lista_mascotas
