#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

#include "graph.h"
int V;

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
	// Creamos V!
	fscanf(input_stream, "%d", &V);

	printf("v: %i\n", V);
	// Creamos matriz adyacencia vacía 0s
	int adjMatrix[V][V];
	init(adjMatrix);

	// Recibimos y agregamos valores según distancias
	printAdjMatrix(adjMatrix);

	// Creamos array con las distancias
	int distancias_x[V];
	int distancias_y[V];
	int value_1;
	int value_2;

	for (int i = 0; i < V; i++) {
		fscanf(input_stream, "%d", &value_1);
		fscanf(input_stream, "%d", &value_2);
		distancias_x[i] = value_1;
		distancias_y[i] = value_2;
	}

	for (int i = 0; i < V; i++) {
		for (int j = 0; j < V; j++) {
			int costo = abs(distancias_x[i] - distancias_x[j]) + abs(distancias_y[i] - distancias_y[j]);
			printf("costo: %i\n", costo);
			// printf("i: %i\n", i);
			// printf("j: %i\n", costo);
			addEdge(adjMatrix, i, j, costo);
		}
	}
	printAdjMatrix(adjMatrix);
	primMST(adjMatrix, distancias_x, distancias_y, output_stream);

	// int N;
	// fscanf(input_stream, "%d", &N);
	// int arbol[N];

	// // Crear array;
	// int value_1;
	// int value_2;
	// for (int i = 0; i < V; i++) {
	// 	fscanf(input_stream, "%d", &value_1);
	// 	fscanf(input_stream, "%d", &value_2);
	// 	addEdge(adjMatrix, value_1, value_2);
	// }
	// printAdjMatrix(adjMatrix);

	// Cerrar archivo de input
	fclose(input_stream);

	// Cerrar archivo de output
	fclose(output_stream);

	return 0;
}

void init(int arr[][V]) {
	int i, j;
	for (i = 0; i < V; i++)
		for (j = 0; j < V; j++)
			arr[i][j] = 0;
}

void addEdge(int arr[][V], int i, int j, int value) {
	arr[i][j] = value;
}

// Print the matrix
void printAdjMatrix(int arr[][V]) {
	int i, j;
	printf("que wea v:%i\n", V);
	for (i = 0; i < V; i++) {
		printf("%d: ", i);
		for (j = 0; j < V; j++) {
			printf("%d ", arr[i][j]);
		}
		printf("\n");
	}
}

// MST PRIM
int minKey(int key[], bool mstSet[]) {
	// Initialize min value
	int min = INT_MAX, min_index;

	for (int v = 0; v < V; v++)
		if (mstSet[v] == false && key[v] < min)
			min = key[v], min_index = v;

	return min_index;
}

// A utility function to print the
// constructed MST stored in parent[]
int printMST(int parent[], int graph[V][V], int distancias_x[V], int distancias_y[V], FILE* output_file) {
	int costo = 0;
	printf("%i\n", distancias_x[0]);
	for (int i = 1; i < V; i++) {
		costo += graph[i][parent[i]];
	}
	fprintf(output_file, "%i\n", costo);
	for (int i = 1; i < V; i++)
		fprintf(output_file, "%d %d %d %d\n", distancias_x[parent[i]], distancias_y[parent[i]], distancias_x[i], distancias_y[i]);
	// printf("%d - %d \t%d \n", parent[i], i,
	//        graph[i][parent[i]]);
}

// Function to construct and print MST for
// a graph represented using adjacency
// matrix representation
void primMST(int graph[V][V], int distancias_x[V], int distancias_y[V], FILE* output_file) {
	// Array to store constructed MST
	int parent[V];
	// Key values used to pick minimum weight edge in cut
	int key[V];
	// To represent set of vertices included in MST
	bool mstSet[V];

	// Initialize all keys as INFINITE
	for (int i = 0; i < V; i++)
		key[i] = INT_MAX, mstSet[i] = false;

	// Always include first 1st vertex in MST.
	// Make key 0 so that this vertex is picked as first
	// vertex.
	key[0] = 0;
	parent[0] = -1;   // First node is always root of MST

	// The MST will have V vertices
	for (int count = 0; count < V - 1; count++) {
		// Pick the minimum key vertex from the
		// set of vertices not yet included in MST
		int u = minKey(key, mstSet);

		// Add the picked vertex to the MST Set
		mstSet[u] = true;

		// Update key value and parent index of
		// the adjacent vertices of the picked vertex.
		// Consider only those vertices which are not
		// yet included in MST
		for (int v = 0; v < V; v++)

			// graph[u][v] is non zero only for adjacent
			// vertices of m mstSet[v] is false for vertices
			// not yet included in MST Update the key only
			// if graph[u][v] is smaller than key[v]
			if (graph[u][v] && mstSet[v] == false && graph[u][v] < key[v])
				parent[v] = u, key[v] = graph[u][v];
	}

	// print the constructed MST
	printMST(parent, graph, distancias_x, distancias_y, output_file);
}
