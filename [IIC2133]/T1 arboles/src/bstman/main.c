#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "node/node.h"

/* Retorna true si ambos strings son iguales */
bool string_equals(char* string1, char* string2) {
	return !strcmp(string1, string2);
}

/* Revisa que los parametros del programa sean válidos */
bool check_arguments(int argc, char** argv) {
	if (argc != 3) {
		printf("Modo de uso: %s INPUT OUTPUT\n", argv[0]);
		printf("Donde:\n");
		printf("\tINPUT es la ruta del archivo de input\n");
		printf("\tOUTPUT es la ruta del archivo de output\n");
		exit(1);
	}

	return true;
}

int main(int argc, char** argv) {
	check_arguments(argc, argv);

	FILE* input_file = fopen(argv[1], "r");
	FILE* output_file = fopen(argv[2], "w");

	int node_count;
	int query_count;

	fscanf(input_file, "%d", &node_count);

	int value;
	Node* root;
	Node* node;

	fscanf(input_file, "%d", &value);

	root = node_create(value);

	for (int i = 1; i < node_count; i++) {
		fscanf(input_file, "%d", &value);
		node = node_create(value);
		insert_node(root, node);
	}
	// print_tree(root);
	// printf("\n");

	fscanf(input_file, "%d", &query_count);
	/* leemos las consultas */
	char command[32];
	int valor;
	for (int i = 0; i < query_count; i++) {
		fscanf(input_file, "%s", command);
		/* completar la revision de comando y ejecucion de los mismos */
		//
		if (string_equals(command, "PATH")) {
			fscanf(input_file, "%d", &valor);
			path_value(root, valor, output_file);
		}
		else if (string_equals(command, "DEEP")) {
			fscanf(input_file, "%d", &valor);
			int deep = getLevel(root, valor);
			fprintf(output_file, "%i\n", deep);
		}
		else if (string_equals(command, "ORDER")) {
			Order(root, output_file);
			fprintf(output_file, "\n");
		}
		else if (string_equals(command, "SUBTREE")) {
			fscanf(input_file, "%d", &valor);
			fscanf(input_file, "%d", &value);

			Node* raiz;
			Node* node;

			raiz = node_create(value);

			for (int i = 1; i < valor; i++) {
				fscanf(input_file, "%d", &value);
				node = node_create(value);
				insert_node(raiz, node);
			}
			if (isSubtree(root, raiz)) {
				fprintf(output_file, "1");
			}
			else {
				// revisar
				fprintf(output_file, "0");
			}
			fprintf(output_file, "\n");
			free_tree(raiz);
		}
	}
	///
	///
	// ELIMINAR ÁRBOL
	free_tree(root);

	fclose(input_file);
	fclose(output_file);
	return 0;
}
