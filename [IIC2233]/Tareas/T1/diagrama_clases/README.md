# Explicación Diagrama de Clases 

La tarea se desarrolló en que el programa principal funcionaba en torno a la clase  ```Arena```, el cual contenía a las demás clases mediante relaciones de composición; ya que si terminaba la arena, significaba que terminaba el juego **condicionando a las demás clases a terminar de funcionar**.

La  ```Arena``` tiene una relación de composición con la clase  ```Tributo``` y  ```Ambiente```, es más, eran atributos de la clase  ```Arena```. Para el caso de la clase  ```Ambiente```, está se modelo como una clase abstracta que tenía 3 subclases dependiendo del tipo de ambiente. Estas subclases eran: ```Playa```,  ```Montana``` y  ```Bosque```. ***Estos realizaban el mismo método de la clase padre pero sus atributos variaban.***

Para el caso de la clase  ```Tributo``` está realizaba las acciones de cada jugador. En esta clase se generó una relación de composición con la clase  ```Objeto```. Esta tenía este tipo de relación dependiente ya que, si vivía o no el tributo, ***afectaba si seguian los objetos de tipo  ```Objeto```.***

Aún así, existían diversos tipos de  ```Objeto``` por lo que esta clase era de tipo abstracta y heredaba las clases:  ```Consumible```,  ```Arma``` y ```Especial```. Estas clases, tenían los mismos atributos pero se diferenciaban en ***cada una realizaba un método distinto al ser usados.***
