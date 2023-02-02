#pragma once

#include <stdbool.h>
#include <stdio.h>

typedef struct Cancion {
	int id;
	int duracion;
	int rating;
} Cancion;

Cancion* cancion_init(int id, int duracion, int rating);
void cancion_agregada(Cancion* cancion, int id_disco, FILE* output_file);
void cancion_destroy(Cancion* cancion);