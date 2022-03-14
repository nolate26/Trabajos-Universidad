#Archivos -> Guardar cosas para usar despues 
#muchos archivos-> contiene info interpretable
#abrir emoji con word o con fotos-> docc etc
#depende de extension-> jpg, docx, txt, xlsx
#aprender a manejar archivos de texto plano-> bloc de notas
#los archivos están en los ficheros-> "carpetas" directorios


#Archivos con python: 2 funciones 
# 1- open()
# 2- close()...distintas formas de leer



#leer archivo(almacenarlo en lista) 
archivo = open('ejemplo.txt', 'r')  # abrimos el archivo en formato lectura (esto lo indica la 'r' de read)
data = archivo.readlines()  # lo leemos guardandolo como lista
archivo.close()         # ¡Siempre cerrar el archivo!
# si queremos imprimir cada linea
for linea in data:
    print(linea.strip("\n")) # eliminamos los saltos de línea e imprimimos

#Escribir en archivos 
texto = 'Intro es bacán, pero yo soy mucho más bacán porque le gané a Peachy Head <3\nfin.'
archivo = open('ejemplo.txt', 'w')
archivo.write(texto)  # se guardará el el texto en el archivo
archivo.close()

#ejemplo para dejarlo en una lista limpia 
lista=open("mejorescanciones.txt")
lineas=lista.readlines()
lista.close()

canciones=[]
for l in lineas:
    linea=l.strip()
    info=linea.split(",")
    canciones.append(info)




#LEER ARCHIVOS
#abrir-> x=open("archivo.txt")
#leer ->lineas = x.readlines() -> retorna una lista de strings
            #->x.readline()retorna en posicion  
#cerrar -> x.close

print("hola","chao","jajajaj",sep=",") #hola,chao,jajajaj
print("hola","chao","jajajaj",sep="  \n, ") #siempre split para sacar /n

#ESCRIBIR ARCHIVOS
#abrir-> x=open("archivo.txt","w") o w+-> ESCRIBIR RUTA COMPLETA SINO
#leer-> print(texto, file(x))
#cerrar-> x.close()

n=int(input("Tabla del:"))
tabla=open("tabladel"+str(n)+".txt","w+")
for i in range(1,11):
    print(n*i,file=tabla)
tabla.close()

#write-> agrega texto
#s+=str(num)+/n
#escritor.write

#cambiar nombre de archivo
#abrir-> open.("archivo.txt","w")
#print("sss")

#¿pQ importante cerrar archivo?
#indicar que terminamos de usar y ver.

#/n queda con dos saltos de líneas -> para esto usamos strip: elimina espacios y saltos de linea
#x.strip("\n"," ") elimina de los lados 

#sort()-> 
