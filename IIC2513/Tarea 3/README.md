# Tarea 3

Considerar que son carpetas a parte por lo que hay que ejecutar en 2 consolas sus respectivos códigos.

## 1. FRONTEND

### Supuestos

- Asumimos que solo se puede hacer una operación a la vez para poder trabajarlo como se pide en el Backend.
- Si bien manejo la mayoría de errores por el front en que valores poner, se señala en el enunciado: "El usuario debe ingresar un numero, luego un operador y por último otro número utilizando para ello el teclado de la calculadora en pantalla". Si bien manejo errores de tipo (*23), (3*+5), (9*). Lo único que no se maneja es estilo - al final (12-2-) o el -+-. Pero según el enunciado no es pedido.

## Consideraciones

- Se trabajó con React: todo el Front está en App.jsx, con su respectivo css App.css.
- En lugar de botón enter, usé el botón (=), que es más grande que los demás.
- Se manejan negativos a la perfección a excepción del supuesto.
- El visor se hizo logrando ver la operación completa. Por ejemplo:  1789 + 155.
- Se usa fetch para conectar con el backend.
- Luego de realizar una operación, si se comienza con un operador(+-/*), se quedará en blanco al primer click (si es un -, al segundo aparecerá)
- Se hacen todas las restricciones para solo apretar una operación (a excepción del - por los números negativos).
- La manera de elegir el primer operador de derecha a izquierda fue con la ayuda de ChatGPT, ya que antes lo hacía con encontrar el primer operador y no dividía bien cuando se trabajaba con número negativos. Además, le pedí ayuda en como hacer la diferenciación entre POST y GET, para luego aplicarlo al fetch. Lo demás fue implementación propia.
- El diseño del .css lo saque de un video en Youtube: (<https://www.youtube.com/watch?v=DgRrrOt0Vr8&t=568s>)

## Como correr el codigo

- ejecutar yarn, ya que elimine carpeta node_modules para comprimirla
- Estar en el directorio *calculadora*.
- Ejecutar `yarn dev`
- habilitar el servidor del backend

## Diseño de la solución

El Frontend se creó usando React, esto con el fin de familiarizarse más aún para el proyecto y aprender a usar estados. Para crearlo, use distintos botones con distintas funciones al apretar. Para ordenarlo y que quedará bien en pantalla use el archivo App.css y darle un orden usando Grid. Se incluye tecla de borrado. Luego al dar enter al cálculo, este es revisado, por ejemplo que no esté vació el otro lado de la operación, luego se usa fetch para mandar al backend las solicitudes. Con GET la suma y mult, POST con div y resta. Luego se recibe la respuesta, que puede ser un error (división por 0) o entrega el resultado que se hace visible en la pantalla.

## 2. BACKEND

### Supuestos

- Debido a que no me funcionaba el puerto 80, lo hice en el 3000.
- Asumimos que solo se puede hacer una operación a la vez para poder trabajarlo como se pide en el Backend.

## Consideraciones

- Se trabajó con Koa siguiendo las capsulas mediante rutas: cada operación en una ruta distinta.
- Use el módulo Cors ya que al conectarlo me daba un error, luego de indagar esta fue la solución.
- Se trabajan con GET, suma y mult. Y con POST div y resta.
- Se maneja el error de dividir por 0, mostrandolo en el resultado.
- La mayoría del trabajo fue guiada por las capsulas proporcionadas y la documentación de fetch. Lo único en que necesite de chatGPT fue al dividir por 0, enviar el error mediante proemesas, lo que me ayudo algo.

## Como correr el codigo

- AGREGAR libreria yarn add koa, ya que borre los node_modules para poder comprimir.
- Estar en el directorio *backend*.
- Ejecutar `yarn dev`
- Con esto ya pueden trabajar en el front, consultando resultados.

## Diseño de la solución

El Backend se realizó con el koa,se creó en el puerto 3000. Se siguió como base lo mostrado en las cápsulas, pero lo que se investigó a fondo era como traspasar la información de frontend a backend. Esto se hizo mediante fetch, distinguiendo entre que cosas eran POST y que era GET. Luego, fue bastante sencillo crear cada operación y retornarlo. Lo único que fue mas molesto fue el saber como retornar si es que había un error, en lo que me ayudo chatGPT. Finalmente, apoyado por la documentación lo supe y retorne fácilmente los valores para mostrarlos en la calculadora.
