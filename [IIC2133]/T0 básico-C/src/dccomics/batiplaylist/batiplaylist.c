#include "batiplaylist.h"

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "../cancion/cancion.h"

// Definimos el inicializador de la lista, recibe el valor a guardar
Batiplaylist* bati_init(int playlist_id) {
	// Pedimos memoria para la lista
	Batiplaylist* batiplaylist = malloc(sizeof(Batiplaylist));

	// Inicializamos la lista directamente
	*batiplaylist = (Batiplaylist){
	    .cancion = NULL,
	    .disco_id = -1,
	    .next = NULL,   // como no tiene siguiente lista y es un puntero, debe partir en NULL
	    .back = NULL,
	};
	return batiplaylist;
}

void agregar_cancion(Batiplaylist* batiplaylist, Disco* disco, int song_id) {
	if (batiplaylist->cancion == NULL) {
		batiplaylist->cancion = disco->canciones[song_id];
		batiplaylist->disco_id = disco->id;
	}
	else {
		Batiplaylist* last = batiplaylist;
		while (last->next) {
			last = last->next;
		}
		// Creamos el nuevo nodo
		Batiplaylist* new_batiplaylist = malloc(sizeof(Batiplaylist));

		// Inicializamos la lista directamente
		*new_batiplaylist = (Batiplaylist){
		    .cancion = disco->canciones[song_id],
		    .disco_id = disco->id,
		    .next = NULL,   // como no tiene siguiente lista y es un puntero, debe partir en NULL
		    .back = last,
		};
		//  Lo agregamos como el nodo siguiente al ultimo nodo de la lista
		last->next = new_batiplaylist;
	}
}

void eliminar_cancion(Batiplaylist* batiplaylist, Disco* disco, int song_id, int bati_id, FILE* output_file) {
	if ((batiplaylist->cancion->id == song_id) & (batiplaylist->disco_id == disco->id)) {
		if (!batiplaylist->back) {
			Batiplaylist* bati = batiplaylist->next->next;
			batiplaylist->cancion = batiplaylist->next->cancion;
			batiplaylist->disco_id = batiplaylist->next->disco_id;
			free(batiplaylist->next);
			batiplaylist->next = bati;
		}
		else {
			if (!batiplaylist->next) {
				batiplaylist->back->next = NULL;
				free(batiplaylist);
			}
			else {
				batiplaylist->back->next = batiplaylist->next;
				batiplaylist->next->back = batiplaylist->back;
				free(batiplaylist);
			}
		}

		fprintf(output_file, "ELIMINADO %i %i %i\n", song_id, disco->id, bati_id);
	}
	else if (!batiplaylist->next) {
		fprintf(output_file, "SONG NOT FOUND ON PLAYLIST\n");
	}
	else {
		eliminar_cancion(batiplaylist->next, disco, song_id, bati_id, output_file);
	}
}

bool revisar_batiplaylist(Batiplaylist* batiplaylist, int disco_id, int song_id) {
	if (batiplaylist->cancion == NULL) {
		return true;
	}
	else {
		if ((batiplaylist->cancion->id == song_id) & (batiplaylist->disco_id == disco_id)) {
			return false;
		}
		else {
			if (!batiplaylist->next) {
				return true;
			}
			else {
				return revisar_batiplaylist(batiplaylist->next, disco_id, song_id);
			}
		}
	}
}

void play_batiplaylist(Batiplaylist* batiplaylist, int bati_id, FILE* output_file) {
	int canciones = contar_canciones(batiplaylist, 0);
	fprintf(output_file, "ESTADO BATIPLAYLIST %i\n", bati_id);
	fprintf(output_file, "\t%i\n", canciones);
	fprintf(output_file, "\tCANCIONES\n");
	play_canciones(batiplaylist, output_file);
}

void play_canciones(Batiplaylist* batiplaylist, FILE* output_file) {
	if (batiplaylist->cancion == NULL) {
		fprintf(output_file, "FIN ESTADO\n");
	}

	else if (!batiplaylist->next) {
		fprintf(output_file, "\t\t%i %i\n", batiplaylist->cancion->id, batiplaylist->disco_id);
		fprintf(output_file, "FIN ESTADO\n");
	}
	else {
		fprintf(output_file, "\t\t%i %i\n", batiplaylist->cancion->id, batiplaylist->disco_id);
		play_canciones(batiplaylist->next, output_file);
	}
}
int contar_canciones(Batiplaylist* batiplaylist, int n) {
	if (batiplaylist->cancion == NULL) {
		return n;
	}
	else if (!batiplaylist->next) {
		n += 1;
		return n;
	}
	else {
		n += 1;
		return contar_canciones(batiplaylist->next, n);
	}
}

void rate_batiplaylist(Batiplaylist* batiplaylist, int bati_id, FILE* output_file) {
	float final = contar_rate(batiplaylist, 0, 0);
	fprintf(output_file, "BATIPLAYLIST %i: %.2f\n", bati_id, final);
}

double contar_rate(Batiplaylist* batiplaylist, int canciones, int rate) {
	if (batiplaylist->cancion == NULL) {
		return 0;
	}
	else if (!batiplaylist->next) {
		canciones += 1;
		rate += batiplaylist->cancion->rating;
		double final = (double)rate / canciones;
		return final;
	}
	else {
		canciones += 1;
		rate += batiplaylist->cancion->rating;
		return contar_rate(batiplaylist->next, canciones, rate);
	}
}

void unir_batiplaylist_nuevo2(Batiplaylist* batiplaylist_1, Batiplaylist* batiplaylist_2, int bati_id_1, int bati_id_2, FILE* output_file) {
	Batiplaylist* agregar = batiplaylist_2;
	while (agregar) {
		Batiplaylist* revisar = batiplaylist_1;
		while (revisar->next) {
			if ((revisar->cancion->id == agregar->cancion->id) & (revisar->disco_id == agregar->disco_id)) {
				break;
			}
			revisar = revisar->next;
		}
		if ((revisar->cancion->id != agregar->cancion->id) | (revisar->disco_id != agregar->disco_id)) {
			agregar_cancion_batiplaylist(revisar, agregar->cancion, agregar->disco_id);
		}
		agregar = agregar->next;
	}
	fprintf(output_file, "JOINED %i AND %i\n", bati_id_1, bati_id_2);
}

void agregar_cancion_batiplaylist(Batiplaylist* batiplaylist, Cancion* cancion, int disco_id) {
	Batiplaylist* last = batiplaylist;
	while (last->next) {
		last = last->next;
	}
	// Creamos el nuevo nodo
	Batiplaylist* new_batiplaylist = malloc(sizeof(Batiplaylist));

	// Inicializamos la lista directamente
	*new_batiplaylist = (Batiplaylist){
	    .cancion = cancion,
	    .disco_id = disco_id,
	    .next = NULL,   // como no tiene siguiente lista y es un puntero, debe partir en NULL
	    .back = last,
	};
	//  Lo agregamos como el nodo siguiente al ultimo nodo de la lista
	last->next = new_batiplaylist;
}

Batiplaylist* split_batiplaylist(Batiplaylist* batiplaylist, int position) {
	if (position == 0) {
		batiplaylist->back->next = NULL;
		batiplaylist->back = NULL;
		return batiplaylist;
	}
	else {
		return split_batiplaylist(batiplaylist->next, position - 1);
	}
}

int purgar_batiplaylist(Batiplaylist* batiplaylist, int rating, int contador) {
	if (batiplaylist->cancion->rating < rating) {
		if (batiplaylist->back == NULL) {
			batiplaylist = batiplaylist->next;
			return purgar_batiplaylist(batiplaylist, rating, contador + 1);
		}
		else {
			if (!batiplaylist->next) {
				batiplaylist->back->next = NULL;
				free(batiplaylist);
				return (contador + 1);
			}
			else {
				batiplaylist->back->next = batiplaylist->next;
				batiplaylist->next->back = batiplaylist->back;
				return purgar_batiplaylist(batiplaylist->next, rating, contador + 1);
				free(batiplaylist);
			}
		}
	}
	else if (!batiplaylist->next) {
		return (contador);
	}
	else {
		return purgar_batiplaylist(batiplaylist->next, rating, contador);
	}
}

void batiplaylist_destroy(Batiplaylist* batiplaylist) {
	// Definimos el destructor de la lista
	// Si hay un nodo en la sig posicion, llamamos recursivamente a la funcion
	if (batiplaylist->next) {
		batiplaylist_destroy(batiplaylist->next);
	}

	// Luego, liberamos la lista
	free(batiplaylist);
}

Batiplaylist* ordenar_batiplaylist(Batiplaylist* batiplaylist_1) {
	// Batiplaylist* itera = batiplaylist_1;
	Batiplaylist* batiplaylist_2 = bati_init(batiplaylist_1->disco_id);

	while (batiplaylist_1) {
		batiplaylist_2 = agregar_orden(batiplaylist_1, batiplaylist_2);

		batiplaylist_1 = batiplaylist_1->next;
	}
	return batiplaylist_2;
}
Batiplaylist* agregar_orden(Batiplaylist* batiplaylist_1, Batiplaylist* batiplaylist_2) {
	if (batiplaylist_2->cancion == NULL) {
		batiplaylist_2->cancion = batiplaylist_1->cancion;
		batiplaylist_2->disco_id = batiplaylist_1->disco_id;
		batiplaylist_2->back = NULL;
		batiplaylist_2->next = NULL;
		return batiplaylist_2;
	}

	else if (batiplaylist_1->cancion->duracion <= batiplaylist_2->cancion->duracion) {
		Batiplaylist* new_batiplaylist = malloc(sizeof(Batiplaylist));

		// Inicializamos la lista directamente
		*new_batiplaylist = (Batiplaylist){
		    .cancion = batiplaylist_1->cancion,
		    .disco_id = batiplaylist_1->disco_id,
		    .next = NULL,   // como no tiene siguiente lista y es un puntero, debe partir en NULL
		    .back = NULL,
		};
		if (batiplaylist_2->back == NULL) {
			batiplaylist_2->next = batiplaylist_2;
			batiplaylist_2 = new_batiplaylist;
		}
		else {
			new_batiplaylist->back = batiplaylist_2->back;
			batiplaylist_2->back->next = new_batiplaylist;
			batiplaylist_2->back = new_batiplaylist;
			new_batiplaylist->next = batiplaylist_2;
		}
		Batiplaylist* last = batiplaylist_2;
		while (last->back) {
			last = last->back;
		}
		return last;
	}
	else {
		if (batiplaylist_2->next == NULL) {
			Batiplaylist* new_batiplaylist = malloc(sizeof(Batiplaylist));

			// Inicializamos la lista directamente
			*new_batiplaylist = (Batiplaylist){
			    .cancion = batiplaylist_1->cancion,
			    .disco_id = batiplaylist_1->disco_id,
			    .next = NULL,   // como no tiene siguiente lista y es un puntero, debe partir en NULL
			    .back = NULL,
			};
			new_batiplaylist->back = batiplaylist_2;
			batiplaylist_2->next = new_batiplaylist;
			Batiplaylist* last = batiplaylist_2;
			while (last->back) {
				last = last->back;
			}
			return last;
		}
		else {
			agregar_orden(batiplaylist_1, batiplaylist_2->next);
		}
	}
}

void play_ordenar(Batiplaylist* batiplaylist, int bati_id, FILE* output_file) {
	fprintf(output_file, "SORTED BATIPLAYLIST %i\n", bati_id);
	play_canciones_ordenar(batiplaylist, output_file);
}
void play_canciones_ordenar(Batiplaylist* batiplaylist, FILE* output_file) {
	if (batiplaylist->cancion == NULL) {
		fprintf(output_file, "END SORTED\n");
	}

	else if (!batiplaylist->next) {
		fprintf(output_file, "\tCANCION %i\n", batiplaylist->cancion->id);
		fprintf(output_file, "END SORTED\n");
	}
	else {
		fprintf(output_file, "\tCANCION %i\n", batiplaylist->cancion->id);
		play_canciones_ordenar(batiplaylist->next, output_file);
	}
}