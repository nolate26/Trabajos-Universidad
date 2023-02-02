#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "batiplaylist/batiplaylist.h"
#include "cancion/cancion.h"
#include "disco/disco.h"

/* Retorna true si ambos string so iguales */
bool string_equals(char *string1, char *string2) {
	return !strcmp(string1, string2);
}

/* Función encargada de chequear los argumentos ingresados */
bool check_arguments(int argc, char **argv) {
	if (argc != 3) {
		printf("Modo de uso: %s INPUT OUTPUT\n", argv[0]);
		printf("Donde:\n");
		printf("\tINPUT es la ruta del archivo de input\n");
		printf("\tOUTPUT es la ruta del archivo de output\n");
		return false;
	}
	return true;
}

int main(int argc, char **argv) {
	/////////////////////////
	//        Input        //
	/////////////////////////
	/* Si los parámetros del programa son inválidos */
	if (!check_arguments(argc, argv)) {
		/* Salimos del programa indicando que no terminó correctamente */
		return 1;
	}

	/* Abrimos el archivo de input */
	FILE *input_file = fopen(argv[1], "r");

	/* Abrimos el archivo de output */
	FILE *output_file = fopen(argv[2], "w");

	/* String que usaremos para guardar la instrucción actual*/
	char command[32];

	// Lectura del número de batiplaylists
	int N_BATIPLAYLISTS;
	fscanf(input_file, "%d", &N_BATIPLAYLISTS);

	// Lectura del número de discos
	int N_DISCS;
	fscanf(input_file, "%d", &N_DISCS);

	/* Leemos la primera instrucción */
	fscanf(input_file, "%s", command);

	/*Creamos array con total de discos y variable de ids*/
	Disco **biblioteca = calloc(N_DISCS, sizeof(Disco *));
	int disco_id = 0;

	Batiplaylist **batibiblioteca = calloc(N_BATIPLAYLISTS, sizeof(Batiplaylist *));
	// double final = 0;
	/*IDS EMPIEZAN DESDE 0!!!!!!!!!!!!!!!!!!!!!!!!!*/

	/* Mientras la instrucción sea distinta a FIN */
	while (!string_equals(command, "FIN")) {
		/////////////////////////
		//       Parte A       //
		/////////////////////////

		if (string_equals(command, "CREAR-DISCO")) {
			/* Obtenemos la información del disco */
			int capacity, length, rating;
			fscanf(input_file, "%d", &capacity);

			/* COMPLETAR */
			int cancion_id = 0;
			Disco *disco = disco_init(disco_id, capacity);
			for (int i = 0; i < capacity; i += 1) {
				fscanf(input_file, "%d", &length);
				fscanf(input_file, "%d", &rating);
				Cancion *cancion = cancion_init(cancion_id, length, rating);
				disco->canciones[i] = cancion;
				cancion_agregada(disco->canciones[i], disco_id, output_file);
				cancion_id += 1;
			}
			biblioteca[disco_id] = disco;
			disco_id += 1;
		}

		else if (string_equals(command, "ELIMINAR-CANCION")) {
			/* Obtenemos la información de la canción */
			int disc_id, song_id;
			fscanf(input_file, "%d %d", &disc_id, &song_id);

			/* COMPLETAR */
		}

		else if (string_equals(command, "IMPRIMIR-DISCO")) {
			/* Obtenemos la información correspondiente */
			int disc_id;
			fscanf(input_file, "%d", &disc_id);

			/* COMPLETAR */

			imprimir_disco(biblioteca[disc_id], output_file);
		}
		else if (string_equals(command, "IMPRIMIR-CANCION")) {
			/* Obtenemos la información correspondiente */
			int disc_id, song_id;
			fscanf(input_file, "%d %d", &disc_id, &song_id);

			/* COMPLETAR */

			imprimir_cancion(biblioteca[disc_id], song_id, output_file);
		}

		/////////////////////////
		//       Parte B       //
		/////////////////////////

		else if (string_equals(command, "CREAR-BATIPLAYLIST")) {
			/* Obtenemos la información correspondiente */
			int playlist_id;
			fscanf(input_file, "%d", &playlist_id);

			/* COMPLETAR */

			Batiplaylist *batiplaylist = bati_init(playlist_id);
			batibiblioteca[playlist_id] = batiplaylist;
			fprintf(output_file, "BATIPLAYLIST CREATED %i\n", playlist_id);
		}

		else if (string_equals(command, "AGREGAR-CANCION-BATIPLAYLIST")) {
			int playlist_id, disc_id, song_id;
			fscanf(input_file, "%d %d %d", &playlist_id, &disc_id, &song_id);

			/* COMPLETAR */

			int max_id_disco = biblioteca[disc_id]->canciones[(biblioteca[disc_id]->n) - 1]->id;

			if ((disc_id > disco_id) | (song_id > max_id_disco) | (song_id < 0)) {
				fprintf(output_file, "SONG NOT FOUND\n");
			}
			else {
				agregar_cancion(batibiblioteca[playlist_id], biblioteca[disc_id], song_id);
				fprintf(output_file, "NEW SONG ADDED %i %i %i\n", song_id, disc_id, playlist_id);
			}
		}

		else if (string_equals(command, "ELIMINAR-CANCION-BATIPLAYLIST")) {
			int playlist_id, disc_id, song_id;
			fscanf(input_file, "%d %d %d", &playlist_id, &disc_id, &song_id);

			/* COMPLETAR */

			if ((playlist_id >= N_BATIPLAYLISTS) | (disc_id >= N_DISCS)) {
				fprintf(output_file, "SONG NOT FOUND ON PLAYLIST\n");
			}
			else {
				eliminar_cancion(batibiblioteca[playlist_id], biblioteca[disc_id], song_id, playlist_id, output_file);
			}
		}

		// OJITO CON ESTA
		else if (string_equals(command, "AGREGAR-DISCO-BATIPLAYLIST")) {
			int playlist_id, disc_id;
			fscanf(input_file, "%d %d", &playlist_id, &disc_id);

			/* COMPLETAR */

			int canciones_agregadas = 0;
			for (int i = 0; i < biblioteca[disc_id]->n; i += 1) {
				if (revisar_batiplaylist(batibiblioteca[playlist_id], disc_id, i)) {
					agregar_cancion(batibiblioteca[playlist_id], biblioteca[disc_id], i);
					canciones_agregadas += 1;
				}
			}
			fprintf(output_file, "AGREGADO %i %i %i\n", canciones_agregadas, disc_id, playlist_id);
		}

		else if (string_equals(command, "PLAY-BATIPLAYLIST")) {
			int playlist_id;
			fscanf(input_file, "%d", &playlist_id);

			/* COMPLETAR */

			play_batiplaylist(batibiblioteca[playlist_id], playlist_id, output_file);
		}

		else if (string_equals(command, "RATE-BATIPLAYLIST")) {
			int playlist_id;
			fscanf(input_file, "%d", &playlist_id);

			/* COMPLETAR */

			rate_batiplaylist(batibiblioteca[playlist_id], playlist_id, output_file);
		}

		/////////////////////////
		//       Parte C       //
		/////////////////////////

		else if (string_equals(command, "ELIMINAR-BATIPLAYLIST")) {
			int playlist_id;
			fscanf(input_file, "%d", &playlist_id);

			/* COMPLETAR */

			int canciones = contar_canciones(batibiblioteca[playlist_id], 0);
			batiplaylist_destroy(batibiblioteca[playlist_id]);
			batibiblioteca[playlist_id] = NULL;

			// revisar batiplaylist vacia-- eliminar eliminar_batiplaylist
			fprintf(output_file, "BATIPLAYLIST DELETED %i %i\n", playlist_id, canciones);
		}

		// REVISAR
		else if (string_equals(command, "UNIR-BATIPLAYLIST")) {
			int playlist_id1, playlist_id2;
			fscanf(input_file, "%d %d", &playlist_id1, &playlist_id2);

			/* COMPLETAR */
			// ERROR
			// clock_t start_t, end_t;
			// double total_t;
			// start_t = clock();

			unir_batiplaylist_nuevo2(batibiblioteca[playlist_id1], batibiblioteca[playlist_id2], playlist_id1, playlist_id2, output_file);

			/*	end_t = clock();
			    total_t = (double)(end_t - start_t) / CLOCKS_PER_SEC;
			    final += total_t;*/
			// revisar batiplaylist vacia -- eliminar eliminar_batiplaylist
			batiplaylist_destroy(batibiblioteca[playlist_id2]);
			batibiblioteca[playlist_id2] = NULL;
		}

		else if (string_equals(command, "SPLIT-BATIPLAYLIST")) {
			int playlist_id, new_playlist_id, position;
			fscanf(input_file, "%d %d %d", &playlist_id, &new_playlist_id, &position);

			/* COMPLETAR */

			batibiblioteca[new_playlist_id] = split_batiplaylist(batibiblioteca[playlist_id], position);
		}

		else if (string_equals(command, "ORDENAR-BATIPLAYLIST")) {
			int playlist_id;
			fscanf(input_file, "%d", &playlist_id);

			/* COMPLETAR */
			Batiplaylist *nuevo = ordenar_batiplaylist(batibiblioteca[playlist_id]);
			batiplaylist_destroy(batibiblioteca[playlist_id]);
			batibiblioteca[playlist_id] = nuevo;
			play_ordenar(batibiblioteca[playlist_id], playlist_id, output_file);
		}

		else if (string_equals(command, "PURGAR-BATIPLAYLIST")) {
			int playlist_id, rating;
			fscanf(input_file, "%d %d", &playlist_id, &rating);

			/* COMPLETAR */
			int rat = (int)rating;

			int canciones = purgar_batiplaylist(batibiblioteca[playlist_id], rat, 0);
			if (batibiblioteca[playlist_id]->cancion->rating < rating) {
				batibiblioteca[playlist_id] = batibiblioteca[playlist_id]->next;
			}
			fprintf(output_file, "BATIPLAYLIST PURGED %i %i\n", playlist_id, canciones);
		}

		/* Leemos la siguiente instrucción */
		fscanf(input_file, "%s", command);
	}

	/////////////////////////////////////
	//        Cerramos archivos        //
	////////////////////////////////////

	fclose(input_file);
	fclose(output_file);

	///////////////////////////////////
	//     Liberamos memoria         //
	///////////////////////////////////

	/* COMPLETAR */

	// printf("%i\n", batibiblioteca[0]->next->next->next->next->cancion->duracion);
	// printf("%i\n", batibiblioteca[0]->next->next->cancion->duracion);
	// printf("%i\n", batibiblioteca[0]->next->next->next->cancion->duracion);
	//  printf("%i\n", batibiblioteca[0]->next->next->next->cancion->duracion);
	//    printf("%i\n", batibiblioteca[1]->next->cancion->duracion);
	//    printf("%i\n", batibiblioteca[1]->next->cancion->duracion);

	for (int i = 0; i < N_DISCS; i += 1) {
		for (int j = 0; j < biblioteca[i]->n; j += 1) {
			free(biblioteca[i]->canciones[j]);
		}
		free(biblioteca[i]->canciones);
		free(biblioteca[i]);
	}
	free(biblioteca);

	for (int i = 0; i < N_BATIPLAYLISTS; i += 1) {
		if ((batibiblioteca[i] != 0) & (batibiblioteca[i] != NULL)) {
			batiplaylist_destroy(batibiblioteca[i]);
		}
	}
	free(batibiblioteca);

	/*
	clock_t start_t, end_t;
	double total_t;
	start_t = clock();
	end_t = clock();
	total_t = (double)(end_t - start_t) / CLOCKS_PER_SEC;
	printf("Total time taken by CPU: %f\n", total_t);
	*/
	// printf("Total time taken by CPU: %f\n", final);

	return 0;
}