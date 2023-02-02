#pragma once

#include <stdbool.h>

#include "../cancion/cancion.h"

typedef struct Disco {
	int id;
	int n;
	Cancion** canciones;
} Disco;

Disco* disco_init(int id, int n);

void imprimir_disco(Disco* disco, FILE* output_file);
void imprimir_cancion(Disco* disco, int song_id, FILE* output_file);
void disco_destroy(Disco* disco);