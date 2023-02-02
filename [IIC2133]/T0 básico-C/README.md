# Tarea 0 2022-2

Recuerda subir el código de tu tarea en este repositorio a más tardar el día de la entrega a las 23:59 hrs.

Ejecutar ```./dccomics input.txt output.txt```

# Para compilar
```
make
```
## Para recompilar

```shell
make clean && make
```

## Debugeamos leaks con:

```shell
valgrind --leak-check=full --show-leak-kinds=all ./dccomics
```

## Debugeamos errores con:

```shell
valgrind --track-origins=yes ./dccomics
```

## Para revisar servidor

- Para revisar los _test generales_ en el servidor del curso se tiene que acceder al siguiente [link](http://edd.ing.puc.cl/test?repo=TX-2022-2-USERNAME)

- Para revisar los _test de evaluacion_ en el servidor del curso se tiene que acceder al siguiente [link](http://edd.ing.puc.cl/grade?repo=TX-2022-2-USERNAME)
