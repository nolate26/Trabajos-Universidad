#include "cancion.h"

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

Cancion* cancion_init(int id, int duracion, int rating) {
	// Creamos una cancion, pidiendo memoria
	Cancion* cancion = malloc(1 * sizeof(Cancion));

	*cancion = (Cancion){
	    .id = id,
	    .duracion = duracion,
	    .rating = rating,
	};

	return cancion;
}
void cancion_agregada(Cancion* cancion, int id_disco, FILE* output_file) {
	fprintf(output_file, "CANCION AGREGADA %i %i\n", cancion->id, id_disco);
}

// Definimos el destructor de Cancion
void cancion_destroy(Cancion* cancion) {
	free(cancion);
}