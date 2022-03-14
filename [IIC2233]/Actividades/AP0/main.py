# Debes completar esta función para que retorne la información de los ayudantes
def cargar_datos(path):
    with open(path, 'rt') as archivo:
        data = archivo.readlines()
    lista_ayudantes=[]
    for linea in data:
        line=linea.strip()
        info=line.split(",")
        lista_ayudantes.append(info)
    return lista_ayudantes
    pass


# Completa esta función para encontrar la información del ayudante entregado
def buscar_info_ayudante(nombre_ayudante, lista_ayudantes):
    for sublista in lista_ayudantes:
        if sublista[0] == nombre_ayudante:
            return (f"El nombre del ayudante es {sublista[0]}, tiene cargo de {sublista[1]}, su usu\
ario de github es {sublista[2]} y usuario de Discord {sublista[3]}.")
    return None
    pass


# Completa esta función para que los ayudnates puedan saludar
def saludar_ayudante(info_ayudante):
    saludo = f"Hola soy {info_ayudante[0]} tengo el cargo de {info_ayudante[1]}. Mi usuario de Gith\
ub es {info_ayudante[2]} y el de Discord es {info_ayudante[3]}, saludos!"
    return saludo
    pass


if __name__ == '__main__':
    lista = cargar_datos('ayudantes.csv')
    #print(lista)
    print(buscar_info_ayudante("Francisca Ibarra", lista))
    print(saludar_ayudante(lista[0]))
    pass
    # El código que aquí escribas se ejecutará solo al llamar a este módulo.
    # Aquí puedes probar tu código llamando a las funciones definidas.

    # Puede llamar a cargar_datos con el path del archivo 'ayudantes.csv'
    # para probar si obtiene bien los datos.

    # Puedes intentar buscar la lista de unos de los nombres
    # que se encuentran en el archivo con la función buscar_info_ayudante.
    # Además puedes utilizar la lista obtenida para generar su saludo.

    # Hint: la función print puede se útil para revisar
    #       lo que se está retornando.
