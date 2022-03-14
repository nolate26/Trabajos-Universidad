# Tarea 2: DCCrossy Frog

## Consideraciones generales :octocat:

### 1. Ventanas
* En primera instancia se visualizan correctamente los elementos mínimos de todas las ventanas y estos no se superoponen entre sí. 
    * Para la ```ventana de inicio``` se puede crear una partida nueva con las condiciones dadas. 
    * En la ```ventana de ranking``` se puede volver al inicio y se muestran los mejores 5 puntajes, con la condición de que el jugador termine la partida o pierda, ya que si cierra la ventana mientras juega se guardará el nombre sin puntaje produciendo un error.
    * En la ```ventana de juego``` las estadísticas se actualizan cada vez que ocurren, se cargan todos los elementos, se aprecia el cambio de velocidad de troncos y autos por nivel, se nota el cambio de la duración de la ronda por nivel y el boton ```salir``` ****te llevan a la ventana cuando un jugador sale**** para desde ahí volver al menú de inicio.
    * La ```ventana post-nivel``` se puede continuar y salir. Además se muestran correctamente las estadísticas de la ronda. 
    * Todo esto muy logrado 😆.


### 2.  Mecánicas de juego
***1. Personaje***
* Para el personaje su movimiento es fluido, continuo y animado al caminar y se hace con un correcto uso de señales. El movimiento del personaje es discreto al saltar y sobre un tronco solo puede saltar hacia adelante y atrás.
* Además, el movimiento respeta colisiones con el borde de la ventana de juego y objetos, troncos, río o autos. Mientras el personaje está en un tronco, se mueve junto a él.
 ***Sin embargo***, el programa tiene un pequeño problema al interactuar con el río, ya que verifica por segundo la posición de froggy en el río, por lo tanto, puede moverse dentro del tronco 1 vez x segundo, aún así no puede saltar para los lados, si está en el agua pierde una vida y se traslada en conjunto con el tronco si esta encima de este. El problema está que cuando uno se mueve muchas veces o salta muy rápido los troncos el programa reporta que perdió una vida ya que no alcanzó a reconocer el salto x seg, pero si funciona. 
 * Todo esto muy logrado a excepción de froggy en el río con un pequeño detalle 😆.

***2. Mapa y Áreas de juego***
* El mapa creado respeta los requisitos de enunciado (3 áreas de juego con al menos una carretera y un río). Se tienen 3 hileras de troncos en las zonas de río y 3 de autos en las zonas de carretera y la velocidad de autos y troncos aumenta a medida que se avanza de nivel. 
* El sentido de los autos ***no se escoge de manera aleatoria***, ya que no quería pasarme del máximo de líneas, pero en una misma hilera todos los autos se mueven en el mismo sentido. El sentido de los troncos ***no se escoge de manera aleatoria*** por la misma razón anterior :cry:, pero en una misma hilera todos los troncos se mueven en el mismo sentido y cada hilera se realiza de forma intercalada.
* Todo esto muy logrado 😆, a excepción de la salida aleatoria de autos y troncos.

***3. Objetos***
* Se implementan correctamente las vidas extra, el objeto moneda, el objeto calavera y el objeto reloj. Los objetos se ubican de forma aleatoria en el mapa. No aparecen en el río ni en la meta. No se superponen entre sí. La frecuencia de aparición está determinada por el parámetro ```TIEMPO_OBJETO```. 
* Todo esto muy logrado 😆.

***4. Fin de Nivel***
* Se calculan correctamente los puntajes al terminar el nivel. Se termina el nivel cuando el personaje se queda sin vida o llega a la meta. Se abre la ventana post-nivel automáticamente una vez acabada la ronda. Aquí, realicé una ***pequeña modificación*** a lo pedido cuando se acaba el tiempo ya que encontré que era más lógico que ***al acabar el tiempo, el jugador pierda una vida en lugar de terminal el nivel***, por lo que lo ***apliqué de esa manera***.
* Todo esto muy logrado 😆.

***5. Fin del juego***
* En caso de derrota, se almacena correctamente el nombre de usuario y puntaje en el puntajes.txt, a excepción que el jugador cierre repentinamente la ventana o corte el juego (explicado anteriormente). En caso de derrota, se notifica al usuario y no se puede continuar jugando. En caso de victoria, se notifica al usuario y se permite jugar el siguiente nivel.
* Todo esto muy logrado 😆.
### Chatcodes
* Se implimenta correctamente la pausa con el botón Pausa y la letra P, al seleccionarlo se detienen todas las animaciones. Además se deshabilita la interacción del teclado de flechas con el juego.
*Al escribir (V+I+D), aumenta la cantidad de vidas del jugador. ***Deben ser en ese orden y en conjunto*** (se escribe la v, luego la i y finalmente la d)
* Al escribir (N+I+V) se termina el nivel, calculando correctamente lo realizado al momento. No se puede usar fuera de la ventana de juego. ***Deben ser en ese orden y en conjunto*** (se escribe la n, luego la i y finalmente la d)
* Todo esto muy logrado 😆.

### General
* El juego presenta una adecuada separación backend-frontend ya que en el frontend solo se encuentran funciones que modifican o crean elementos de la ventana. Además, existe un bajo acomplamiento y alta cohesión del programa.
* Se trabaja correctamente con todos los archivos  entregados, se utiliza e importa correctamente parametros.py que contiene todos los parámetros pedidos.
* Todo esto muy logrado 😆.

***Nota***
* No se hizo ningún bonus.

### Cosas implementadas y no implementadas :white_check_mark: :x:

* **Ventanas**:
    * **Inicio**: Completada
    * **Ranking**: Completada
    * **Juego**: Completada
    * **Post-nivel**: Completada

* **Mecanicas de juego**:
    * **Personaje**: Completada a excepción del froggy en el río.
    * **Mapa y áreas de juego**: Completada a excepción de disposición aleatoria.
    * **Objetos**: Completada.
    * **Fin de nivel**: Completada.
    * **Fin del juego**: Completada.

* **Cheatcodes**:
    * **Pausa**: Completada
    * **V + I + D**: Completada
    * **N + I + V**: Completada

* **General**:
    * **Modularización**: Completada
    * **Modelación**: Completada
    * **Archivos**: Completada
    * **Parametros.py**: Completada


## Ejecución :computer:
* El módulo principal de la tarea a ejecutar es  ```main.py```. 
* Para que se ejecute el programa debe estar en una misma carpeta:
    * ```main.py```
    * ```backend```: ```logica_inicio.py```, ```logica_juego.py```.
    * ```frontend```: ```ventana_inicio.py```, ```ventana_juego.py```, ```ventana_ranking.py```, ```ventana_siguiente_nivel.py```, ```ventana_final.py```.
    * ```extras```: ```qtdesigner```: ```ventana_inicio.ui```, ```ventana_juego.ui```, ```ventana_post_nivel1.ui```, ```ventana_post_nivel.ui```, ```ventana_puntajes.ui```.
    * ```parametros.py```
    * ```sprites```
    * ```.gitignore```
    * ```puntajes.txt```

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```.randint``` ; ```.choice```
2. ```os```: ```join()``` 

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```logica_inicio.py```, ```logica_juego.py```: Contiene la lógica usada en el programa
2. ```parametros.py```: Contiene los parámetros entregados en el enunciado.
3. ```main.py```: Se ejecuta el programa, se encarga de llamar a las funciones necesarias mediante señales.
4. ```ventana_inicio.py```, ```ventana_juego.py```, ```ventana_ranking.py```, ```ventana_siguiente_nivel.py```, ```ventana_final.py```: Muestran el contenido de las ventanas.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Cuando se acaba el tiempo ya que encontré que era más lógico que ***al acabar el tiempo, el jugador pierda una vida en lugar de terminal el nivel***, por lo que lo ***apliqué de esa manera***.
2. Se asumen que las dimensiones de la ventana no van a cambiar ya que está ajustado todo bajo esas dimensiones.
3. Para el salto, había un problema para la ```Space-bar``` ya que me apretaba los botones al hacerlo. Por eso se uso la letra ```J``` (jump) para el salto.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. Para verificar elemento alfanumérico:
* https://codingornot.com/08-python-validar-entradas-ejemplos
2. ordenar lista en python para orden de los puntajes:
* https://j2logo.com/python/ordenar-una-lista-en-python/
3. Para los Cheatcodes se uso esta función de pyqt5:
* https://doc.qt.io/qtforpython-5/PySide2/QtGui/QKeySequence.html#more