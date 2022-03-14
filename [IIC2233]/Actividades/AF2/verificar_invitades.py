def verificar_edad(invitade):
    if invitade.edad <= 0:
        raise ValueError(f"Error: la edad de {invitade.nombre} es negativa")

def corregir_edad(invitade):
    try:
        verificar_edad(invitade)
    
    except ValueError as error:
        invitade.edad = abs(invitade.edad)
        print(f"El error en la edad de {invitade.nombre} ha sido corregido")  
    
def verificar_pase_movilidad(invitade):
    if not isinstance(invitade.pase_movilidad, bool):
        raise TypeError(f"Error: el pase de movilidad de {invitade.nombre} no es un bool")


def corregir_pase_movilidad(invitade):
    try:
        verificar_pase_movilidad(invitade)
    except TypeError as error:
        invitade.pase_movilidad = True
        print(f"El error en el pase de movilidad de {invitade.nombre} ha sido corregido")


def verificar_mail(invitade):
    if "@uc.cl" not in invitade.mail:
        raise ValueError(f"Error: El mail de {invitade.nombre} no está en el formato correcto")    
def corregir_mail(invitade):
    try:
        verificar_mail(invitade)
    except ValueError as error:
        nombre = invitade.mail[3:-4] #uc@nombre.cl ->  nombre@uc.cl
        mail = f"{nombre}@uc.cl"
        invitade.mail = mail
        print(f"El error en el mail de {invitade.nombre} ha sido corregido")

def dar_alerta_colado(nombre_asistente, diccionario_invitades):
    try:
        diccionario_invitades[nombre_asistente]
    except KeyError as error:
        print(f"Error: {nombre_asistente} se está intentando colar al carrete")
    else:
        print(f"{nombre_asistente} esta en la lista!!!")



