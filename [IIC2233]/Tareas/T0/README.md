# Tarea 0: DCComerce


## Consideraciones generales :octocat:

* En primera instancia el manejo de archivos se cumplió de manera correcta, se usa el ```Encoding = "utf=8"``` y son almacenados todos en la carpeta ```data``` que al llamarlos son soportados por cualquier sistema operativo.

* El programa comienza de manera correcta, se despliega el ```Menú de Inicio``` con todas las opciones requeridas. Desde inicar sesión, registrarse, ingresar como anónimo y salir. El programa nunca se rompe y si uno sale, el programa se termina.

* A la hora de navegar por los distintos menús, estos funcionan sin ningún problema. Se puede avanzar, volver, cambiar de usuario y desplazarse a otro menú. Además, aunque uno responda en el input caracteres que no te pide, el programa lo reconoce (te dice que la respuesta es incorrecta) y no se cae.

* En términos de las funciones implementadas, estas se ejecutan correctamente. Se realizan de manera correcta lo que se les pide, y se encuentran todas ordenadas según al archivo al que se relacionan en ```lecturas_archivos.py```. Además, esta relación con el archivo es ejecutada de manera correcta, agregando y borrando líneas a los archivos (archivos que mantienen el mismo formato que al inicio).

* Existe una consideración en el orden según fecha en los comentarios y publicaciones. A la hora de programar lo hice según las bases de datos entregada, que de alguna manera tenía cierto orden, por tanto, ordené de forma ascendente y descendente dichos archivos (como lo pedían). Los archivos y publicaciones que se agregaban seguían respetando el orden pedido en el enunciado. El problema está que si me hubieran entregado una base de datos con las fechas desordenadas, el programa no habría podido ordenar de buena manera los archivos iniciales. Aún así, dada la tarea con su base de datos, esta **cumple todo lo pedido** ya que se ordena como lo señala el enunciado y al agregar cosas estas siguen respetando el orden.


### Cosas implementadas y no implementadas :white_check_mark: :x:

* **Menú de inicio**:
    * **Requisitos**: Completada
    * **Iniciar sesión**: Completada
    * **Ingresar como usuario anónimo**: Completada
    * **Registar usuario**: Completada
    * **Salir**: Completada


* **Flujo del programa**:
    * **Menú Principal**: Completada
    * **Menú Publicaciones**: Completada
    * **Menú Publicaciones Realizadas**: Completada


* **Entidades**:
    * **Usuarios**: Completada
    * **Publiaciones**: Completada
    * **Comentarios**: Completada


* **Archivos**:
    * **Manejo de Archivos**: Completada

## Ejecución :computer:
* El módulo principal de la tarea a ejecutar es  ```interfaz.py```. 
* Para que se ejecute el programa debe estar en una misma carpeta:
    * ```interfaz.py```
    * ```lectura_archivos.py```
    * ```parametros.py```
    * carpeta ```data``` que contiene dentro los archivos ```.csv```

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```datetime```: ```datetime.now().strftime()```
2. ```os```: ```join()``` 

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```lecturas_archivos```: Contiene todas las funciones implementadas en el programa ordenadas según a que archivo le realizan cambios. Los menús o lo que se imprime en la consola se encuentra en el módulo principal.
2. ```parametros```: Contiene los parámetros entregados en el enunciado.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. A la hora de verificar si un usuario es válido, el programa te rechaza si es que colcas mal las minúsculas o mayúsculas. Esto se justifica ya que en la vida real existen sitios los cuales te piden el nombre de usuario de manera exacta, acercándolo así con la realidad. 

2. Tal como señala el enunciado al momento de entrar un usuario anónimo este se dirige directamente al ```Menú de Publicaciones```. Esto hace sentido ya que no ejecuta ninguna función si ingresara al ```Menú de Publicaciones Realizadas```.

3. Como se señaló anteriormente asumiremos que la base de datos entregada era la misma con la que se corrige la tarea. Esto debido a que los comentarios y publicaciones iniciales estan ordenadas como lo pide el enunciado de forma predeterminada según los datos entregados. Aún así, al agregar o quitar ```comentarios/publicaciones``` estos si respetarán el orden dado. Si es la misma base de datos **cumplen con todo lo pedido**. 

-------

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://stackoverflow.com/questions/7999935/python-datetime-to-string-without-microsecond-component>: esta función permite asignar que elementos de la fecha quiero agregar, respetando el orden en que estaban creadas las fechas de las publicaciones y omitiendo los microsegundos. Está implementado en el archivo ```lecturas_archivos.py``` en las líneas 127 y 63.
