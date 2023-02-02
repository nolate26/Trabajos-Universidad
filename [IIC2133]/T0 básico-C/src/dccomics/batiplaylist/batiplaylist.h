#pragma once

#include <stdbool.h>

#include "../cancion/cancion.h"
#include "../disco/disco.h"

typedef struct batiplaylist {
	Cancion* cancion;
	int disco_id;
	struct batiplaylist* next;
	struct batiplaylist* back;
} Batiplaylist;

Batiplaylist* bati_init(int playlist_id);

void agregar_cancion(Batiplaylist* batiplaylist, Disco* disco, int song_id);

void eliminar_cancion(Batiplaylist* batiplaylist, Disco* disco, int song_id, int bati_id, FILE* output_file);

bool revisar_batiplaylist(Batiplaylist* batiplaylist, int disco_id, int song_id);

int contar_canciones(Batiplaylist* batiplaylist, int n);

void play_batiplaylist(Batiplaylist* batiplaylist, int bati_id, FILE* output_file);

void play_canciones(Batiplaylist* batiplaylist, FILE* output_file);

void rate_batiplaylist(Batiplaylist* batiplaylist, int bati_id, FILE* output_file);

double contar_rate(Batiplaylist* batiplaylist, int canciones, int rate);

void eliminar_batiplaylist(Batiplaylist* batiplaylist);

void unir_batiplaylist(Batiplaylist* batiplaylist_1, Batiplaylist* batiplaylist_2, int bati_id_1, int bati_id_2, FILE* output_file);

void unir_batiplaylist_nuevo(Batiplaylist* batiplaylist_1, Batiplaylist* batiplaylist_2, int bati_id_1, int bati_id_2, FILE* output_file);

void unir_batiplaylist_nuevo2(Batiplaylist* batiplaylist_1, Batiplaylist* batiplaylist_2, int bati_id_1, int bati_id_2, FILE* output_file);

void revisar_batiplaylist_nuevo(Batiplaylist* batiplaylist_1, Batiplaylist* batiplaylist_2);

void agregar_cancion_batiplaylist_nuevo(Batiplaylist* batiplaylist_1, Batiplaylist* batiplaylist_2);

void agregar_cancion_batiplaylist(Batiplaylist* batiplaylist, Cancion* cancion, int disco_id);

Batiplaylist* split_batiplaylist(Batiplaylist* batiplaylist, int position);

int purgar_batiplaylist(Batiplaylist* batiplaylist, int rating, int contador);

int purgar_batiplaylist2(Batiplaylist* batiplaylist, int rating, int contador);

void batiplaylist_destroy(Batiplaylist* batiplaylist);

// BONUS
Batiplaylist* ordenar_batiplaylist(Batiplaylist* batiplaylist_1);
Batiplaylist* agregar_orden(Batiplaylist* batiplaylist_1, Batiplaylist* batiplaylist_2);
void play_ordenar(Batiplaylist* batiplaylist, int bati_id, FILE* output_file);
void play_canciones_ordenar(Batiplaylist* batiplaylist, FILE* output_file);
