#include "disco.h"

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#include "../cancion/cancion.h"

Disco* disco_init(int id, int n) {
	Disco* disco = malloc(sizeof(Disco));
	/*Cancion* canciones = calloc(n, sizeof(Cancion));*/
	*disco = (Disco){
	    .id = id,
	    .n = n,
	    .canciones = calloc(n, sizeof(Cancion)),
	};

	return disco;
}

void imprimir_disco(Disco* disco, FILE* output_file) {
	int maximo = 0;
	int minimo = 1000000;
	int id_maximo = 0;
	int id_minimo = 0;
	int largo_total = 0;
	for (int i = 0; i < disco->n; i += 1) {
		if (disco->canciones[i]->rating > maximo) {
			maximo = disco->canciones[i]->rating;
			id_maximo = disco->canciones[i]->id;
		}
		if (disco->canciones[i]->rating < minimo) {
			minimo = disco->canciones[i]->rating;
			id_minimo = disco->canciones[i]->id;
		}
		largo_total += disco->canciones[i]->duracion;
	}

	fprintf(output_file, "ESTADO DISCO %i\n", disco->id);
	fprintf(output_file, "\t%i\n", disco->n);
	fprintf(output_file, "\t%i %i\n", maximo, id_maximo);
	fprintf(output_file, "\t%i %i\n", minimo, id_minimo);
	fprintf(output_file, "\t%i\n", largo_total);
	fprintf(output_file, "\tCANCIONES\n");
	for (int i = 0; i < disco->n; i += 1) {
		fprintf(output_file, "\t\t%i\n", disco->canciones[i]->id);
	}
	fprintf(output_file, "FIN ESTADO\n");
}
void imprimir_cancion(Disco* disco, int song_id, FILE* output_file) {
	fprintf(output_file, "ESTADO CANCION %i\n", song_id);
	fprintf(output_file, "\t%i\n", disco->canciones[song_id]->duracion);
	fprintf(output_file, "\t%i\n", disco->canciones[song_id]->rating);
	fprintf(output_file, "FIN ESTADO\n");
}

// Definimos el destructor de Cancion
void disco_destroy(Disco* disco) {
	free(disco);
}