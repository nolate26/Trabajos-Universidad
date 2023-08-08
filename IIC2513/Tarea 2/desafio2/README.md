# Desafio 2

## Supuestos

- El nombre de archivo incluye dentro del programa el `.txt`, por lo que solo debe colocar el nombre del archivo y solo serán archivos de este tipo.
- El programa se corre en el directorio desafio2.
- Se debe instalar prompt-sync para que funcione correctamente (npm install prompt-sync), ya que no sabía otra manera para manejar inputs, fue lo que encontré en Internet.
- Manejé todos los inputs, como si el número no es un número o que las rutas o nombres del archivo sean correctas. En caso que no lo sean se ejecutará nuevamente el programa.
- Se revisa si es que el número pedido es efectivamente un número y si es un decimal se trunca
- El abecedario a usar es: 'aábcdeéfghiíjklmnñoópqrstuúüvxyz'

## Como correr el codigo

- Estar en el directorio desafio2.
- Correr en el terminal `node index.js`.
- Responder las preguntas que aparecen en este.
- En el mismo directorio aparecerá el archivo encriptado, donde si se quería encriptar `nicolas.txt`, el archivo encriptado será `nicolas_cifrado.txt`.

## Diseño de la solución

Para poder solucionar este problema, se requiere del funcionamiento de 3 funciones:
Primero se ejecuta el codigo principal con la función runCode(), aquí se piden los inputs solicitados (se utilizó el paquete `prompt-sync`, la cual permite interactuar con el usuario a través del terminal de manera sincrónica) y se revisa el número entregado.

Luego pasa a el procesamiento del archivo (function procesarArchivo(rotacion, rutaRelativa, nombreArchivo)). Aquí, se busca la ruta relativa dada y se lee el archivo. Si no existe o hubo un error se notifica y se inicia denuevo el proceso. De todo estar OK, se ejecuta la función encriptar(contenido, rotacion);. Aquí, se cambia el contenido dado y es retornado para que finalmente la función de procesamiento la escriba en el nuevo archivo '_cifrado.txt'.
