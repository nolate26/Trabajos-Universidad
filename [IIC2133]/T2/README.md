# Tarea 2 2022-2

Recuerda subir el código de tu tarea en este repositorio a más tardar el día de la entrega a las 23:59 hrs.

## Compilar

```
make
```

## Recompilar

```
make clean && make
```

## Ejecutar

```
./riddler input.txt output.txt
```

## Comparar respuesta

Para esto les subimos un script de Python que les permite comparar su respuesta con la respuesta correcta. Para ejecutarlo, deben tener instalado Python 3.6 o superior:
```
python check_output.py correc_output.txt student_output.txt
```

## Debugeamos leaks con:

```shell
valgrind --leak-check=full --show-leak-kinds=all ./riddler input.txt output.txt
```

## Debugeamos errores con:

```shell
valgrind --track-origins=yes ./riddler input.txt output.txt
```

## Para revisar servidor

En algunos días se subirán testcases al servidor para que puedas probar tu tarea.

- Para revisar los _test publicos_ en el servidor del curso se tiene que acceder al siguiente [link](http://edd.ing.puc.cl/test?repo=T2-2022-2-USERNAME)

- Para revisar los _test de evaluacion_ en el servidor del curso se tiene que acceder al siguiente [link](http://edd.ing.puc.cl/grade?repo=T2-2022-2-USERNAME)

**Tiene que remplazar *USERNAME* por su usuario de github**
