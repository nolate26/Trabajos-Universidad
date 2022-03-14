# Tarea 1: DCCapitolio


## Consideraciones generales :octocat:

* En primera instancia el manejo de archivos se cumplió de manera correcta, esto se realizó en el archivo ```lectura_archivo.py```, en que la mayoría fueron transformados instantaneamente en una lista de objetos dados. Se usa el ```Encoding = "utf=8"``` y son soportados por cualquier sistema operativo. Además, se repeta el ```PEP8``` y esta distribuido el código en módulos ordenados.

* El programa comienza de ***manera correcta***, se despliega el ```Menú de Inicio``` con todas las opciones requeridas. El programa nunca se rompe, ya que se utilizaron excepciones, cabe destacar que me inspiré en el código dado en la ayudantía 2. Además,si uno sale, el programa se termina.

* A la hora de comenzar la partida, se despliegan correctamente los tributos para escoger el que el usuario quiera y la arena respectiva. También, al llegar al ```menú principal```, sigue sin existir algún problema que se caiga el programa y se acepta correctamente la opción de salir o "rendirse" en que lleva al usuario al ***menu de inicio.***

* En términos de las funciones implementadas, estas se ejecutan correctamente. La mayoría de las funciones son las que realiza cada método de la clase la cual cada una se encuentran en un archivo ```.py```. Las demás funciones se encuentran en el archivo ```simulaciones.py``` en que se ejecutan los mini menús y las funciones ejecutadas para el funcionamiento de la simulación de hora. El código se encuentra ***bien explicado ya que está comentado en cada momento.***

* El programa funciona correctamente, en cada simulación de hora, primero se muestran en consola lo que va pasando linealmente, y luego se muestra el resumen. Toda la información queda guardada y se hacen los cambios correspondientes a las funciones. ***Solo implementé algo diferente a lo que leí de mis compañeros.*** En el parámetro ```PROBABILIDAD_EVENTO``` ya que lo tome como un valor constante entre 1 y 10 (usé 5), y use un random entre 1 y 10. Para ver si salía el evento verifiqué si el número del random era mayor a ```PROBABILIDAD_EVENTO```. Por lo que ese fue mi método para generar esa probabilidad.

* El ```diagrama de clases``` junto a la explicación de este se encuentra en la carpeta ```diagrama_clases```.

* El programa es creado de manera lineal, es decir, si el jugador elegido muere o no quedan tributos vivos, el programa detiene la simulación de la hora y tras escribir en consola algunos mensajes, se dirige directamente al menú de inicio.

* Con el fin de tener un mayor orden en los valores de las características de los tributos, tomé la desición de casi siempre dividir ```//``` para obtener valores enteros, cosa que sea mas legible.

* No use el atributo de los tributos ```esta_vivo``` ya que no me di cuenta que estaba, y aunque lo incluí en la clase ```Tributo``` porque lo pedía el enunciado, para saber si estaba vivo solo me maneje con el atributo ```vida``` y su propertie correspondiente.  

### Cosas implementadas y no implementadas :white_check_mark: :x:

* **Programación Orientada a Objetos**:
    * **Diagrama**: Completada
    * **Definición de clases, atributos y métodos**: Completada
    * **Relaciones entre clases**: Completada

* **Simulaciones**:
    * **Crear partida**: Completada

* **Acciones**:
    * **Tributo**: Completada
    * **Objeto**: Completada
    * **Ambiente**: Completada
    * **Arena**: Completada

* **Consola**:
    * **Menu Inicio**: Completada
    * **Menu Principal**: Completada
    * **Simular Hora**: Completada
    * **Robustez**: Completada

* **Manejo de archivos**:
    * **Archivos CSV**: Completada
    * **parametros.py**: Completada


## Ejecución :computer:
* El módulo principal de la tarea a ejecutar es  ```main.py```. 
* Para que se ejecute el programa debe estar en una misma carpeta:
    * ```main.py```
    * ```lectura_archivos.py```
    * ```parametros.py```
    * ```simulaciones.py```
    * ```tributos.py```
    * ```ambientes.py```
    * ```arena.py```
    * ```objetoss.py```
    * Archivos tipo ```.csv```

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```.randint``` ; ```.choice```
2. ```os```: ```join()``` 

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```lecturas_archivos.py```: Se leen los archivos ```.csv``` y se transforman en su mayoría a objeto de las clases creadas.
2. ```parametros.py```: Contiene los parámetros entregados en el enunciado.
3. ```main.py```: Se ejecuta el programa, se encarga de dar los menús, elecciones y llamar a las funciones necesarias.
4. ```simulaciones.py```: Se encarga de ejecutar todas las opciones que se dan al simular una hora, donde revisa si se termina el programa y llama a los métodos de los objetos para que cumplan sus funciones.
5. ```arena.py```: Contiene la clase ```Arena``` con sus respectivos atributos y métodos. 
6. ```ambientes.py```: Contiene la clase ```Ambiente``` con sus respectivos atributos y métodos.
7. ```tributos.py```: Contiene la clase ```Tributo``` con sus respectivos atributos y métodos.
8. ```objetos.py```: Contiene la clase ```Objeto``` con sus respectivos atributos y métodos.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. En el parámetro ```PROBABILIDAD_EVENTO``` lo tomé como un valor constante entre 1 y 10 (usé 5), y use un random entre 1 y 10. Para ver si salía el evento verifiqué si el número del random era mayor a ```PROBABILIDAD_EVENTO```. Por lo que ese fue mi método para generar esa probabilidad.

2. Al calcular el daño hecho por el ambiente y el ataque hecho por los tributos, solo se daba con números enteros.

3. Cuando se accede al ```menu principal``` uno se puede rendir, llevándolo al ```menu de inicio``` pero dentro de cada submenú en que se tomaban desiciones, di la opción para volver al menu principal, sentí que debía ser lo más interactivo posible. Además, mostraba en consola cada acción que se hacia para que tenga un mayor sentido el resumen que se mostraba al final de cada hora.
-------

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. ```Ayudantia 2```: Me inspiré en ese código para crear las excepciones en los menús para que el código no tuviera errores.
