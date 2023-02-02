#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "hashtable.h"
#include "node.h"

int main(int argc, char** argv) {
	if (argc != 3) {
		printf("Modo de uso: %s input output\nDonde:\n", argv[0]);
		printf("\t\"input\" es la ruta al archivo de input\n");
		printf("\t\"output\" es la ruta al archivo de output\n");
		return 1;
	}

	// Abrimos el archivo de input
	FILE* input_stream = fopen(argv[1], "r");

	// Abrimos el archivo de output
	FILE* output_stream = fopen(argv[2], "w");

	// Si alguno de los dos archivos no se pudo abrir
	if (!input_stream) {
		printf("El archivo %s no existe o no se puede leer\n", argv[1]);
		return 2;
	}
	if (!output_stream) {
		printf("El archivo %s no se pudo crear o no se puede escribir\n", argv[2]);
		printf("Recuerda que \"fopen\" no puede crear carpetas\n");
		fclose(input_stream);
		return 3;
	}

	// [Aqui va tu tarea]
	int N;
	fscanf(input_stream, "%d", &N);
	int arbol[N];

	// Crear array;
	int value;
	for (int i = 0; i < N; i++) {
		fscanf(input_stream, "%d", &value);
		arbol[i] = value;
	}
	// crear arbol
	Node* root;
	root = insertLevelOrder(arbol, 0, N);

	// calcular h
	int h = log10(N + 1) / log10(2);

	// Estimar rango (revisar)
	int range = 0;
	int n;
	for (int i = 1; i <= h; i++) {
		n = pow(2, i) - 1;
		range += n;
	}
	range = nextPrime(range);

	// creamos la tabla
	HashItem** table = calloc(range, sizeof(HashItem*));

	// ingresamos los valores
	for (int i = h; i >= 2; i--) {
		calculate_hash(table, root, i);
	}

	// FETCH
	int consultas;
	fscanf(input_stream, "%d", &consultas);
	// recorro cada consulta
	for (int i = 0; i < consultas; i++) {
		int largo_arbol;
		fscanf(input_stream, "%d", &largo_arbol);
		int arr_arbol[largo_arbol];
		int h = log10(largo_arbol + 1) / log10(2);
		int valor;
		for (int i = 0; i < largo_arbol; i++) {
			fscanf(input_stream, "%d", &valor);
			arr_arbol[i] = valor;
		}
		Node* root_consulta;
		root_consulta = insertLevelOrder(arr_arbol, 0, largo_arbol);
		fetch_value(table, root_consulta, h, output_stream, arbol);
		free_tree(root_consulta);
	}

	// free
	free_tree(root);
	free_table(table, range);
	free(table);

	// Cerrar archivo de input
	fclose(input_stream);

	// Cerrar archivo de output
	fclose(output_stream);

	return 0;
}
