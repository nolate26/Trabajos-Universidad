# Desafio 1

## Supuestos

- Asumimos que la función abrirSistemas no arrojará error.
- Primeo el usuario ingresa el codigo de su viaje. Luego si tiene sentido el input (el código es alfanumérico, tres letras y dos dígitos) se abre el sistema.
- Se creó una promesa que busca el codigo y devuelve el destino con sus restricciones. Esta toma cierto tiempo en buscar.
- Se debe agregar posibles errores para las promesas, los cuales se manejan con *.catch*. Se implementó revisar destinos con strings vacios y se alteraron códigos de planificacion.js (como en la funcion restriccionesSanitarias).
- Se utilizó *eslintr* con extensión de airbnb para revisar el estilo, sin embargo, se desactivó para el archivo `planificacion.js` ya que venía con muchos errores.
-- No se revisa sintaxis *airbnb* de codigo de `planificacion.js` (venía con demasiados errores).

## Consideraciones

- Se agregó a `planificacion.js` un *module.exports* para importar las funciones en `index.js`.
- Para agregar una 'base de datos' con el arreglo en el formato pedido, cree en la línea 5 de `index.js` un arreglo con datos al azar con nombre 'destinos', estos los calcule en el archivo rando.py. Contiene diccionarios con los codigos, nombre y restricciones de cada uno.
- Se debe instalar prompt-sync para que funcione correctamente (npm install prompt-sync). Es para el manejo del input.

## Como correr el codigo

- Estar en el directorio *desafio1*.
- Ejecutar `node index.js`.
- Ingresar el codigo de destino.

## Diseño de la solución

La solución se implementó utilizando cuatro promesas: *abrirSistema*, *buscarDestino*, *restricciónSanitaria* y *emiteCertificado*. Primero, se lee el input (el cual es validado). Tras leer el input se abre el sistema. Si esta promesa se resuelve, se revisa si el destino se encuentra en los destinos que tenemos en nuestro arreglo. Luego, si se resuelve la promesa se revisa si tiene restricciones sanitarias. Si esa promesa se resuelve y no tiene restricción, se emite un certificado. Sin embargo, si tiene restricción, pero se resuelve la promesa, el certificado no se emite. Al final, el sistema se cierra usando la función cerrarSistemas. Además, para cada una de estas promesas manejamos sus errores si es que no se cumplen con su respectivo mensaje dependiendo del error.