#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
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

	int inicio;
	int termino;
	int E;
	fscanf(input_stream, "%d", &inicio);
	fscanf(input_stream, "%d", &termino);
	fscanf(input_stream, "%d", &E);
	printf("inicio: %i\n", inicio);
	printf("termino: %i\n", termino);
	printf("E: %i\n", E);

	// Creamos matriz adyacencia vacía 0s
	int** matrix = calloc(V, sizeof(int*));
	int i, j;
	for (i = 0; i < V; i++)
		matrix[i] = calloc(V, sizeof(int));

	for (i = 0; i < V; i++)
		for (j = 0; j < V; j++)
			matrix[i][j] = 0;   // Or *(*(matrix+i)+j) = ++count

	// for (i = 0; i < V; i++)
	// 	for (j = 0; j < V; j++) {
	// 		printf("%d ", matrix[i][j]);
	// 	}
	// int adjMatrix[V][V];
	// init(adjMatrix);

	// Recibimos y agregamos valores según distancias
	// printAdjMatrix(adjMatrix);
	printf("\nNUEVA\n");

	printf("\n");

	// agregamos aristas con costos
	int nodo_1;
	int nodo_2;
	int cost;
	for (int i = 0; i < E; i++) {
		fscanf(input_stream, "%d", &nodo_1);
		fscanf(input_stream, "%d", &nodo_2);
		fscanf(input_stream, "%d", &cost);

		addEdge(matrix, nodo_1, nodo_2, cost);
	}

	dijkstra(matrix, inicio, termino, output_stream);

	// FREE
	for (int i = 0; i < V; i++)
		free(matrix[i]);
	free(matrix);
	// Cerrar archivo de input
	fclose(input_stream);

	// Cerrar archivo de output
	fclose(output_stream);

	return 0;
}

// CREAR LISTA DE ADYACENCIA
void init(int arr[][V]) {
	int i, j;
	for (i = 0; i < V; i++)
		for (j = 0; j < V; j++)
			arr[i][j] = 0;
}

void addEdge(int** arr, int i, int j, int value) {
	arr[i][j] = value;
	arr[j][i] = value;
}
// Print the matrix
void printAdjMatrix(int* arr[][V]) {
	int i, j;
	for (i = 0; i < V; i++) {
		printf("%d: ", i);
		for (j = 0; j < V; j++) {
			printf("%d ", arr[i][j]);
		}
		printf("\n");
	}
}
//
//
//
//
//
// Dijkstra
int minDistance(int* dist, bool* sptSet) {
	int min = INT_MAX, min_index;
	for (int v = 0; v < V; v++)
		if (sptSet[v] == false && dist[v] <= min)
			min = dist[v], min_index = v;
	return min_index;
}
int printSolution(int* dist, int termino, FILE* output_file) {
	fprintf(output_file, "%d\n", dist[termino]);
}
void dijkstra(int** graph, int src, int termino, FILE* output_file) {
	// int dist[V];
	int* dist = calloc(V, sizeof(int));
	// bool sptSet[V];
	bool* sptSet = malloc(V * sizeof(int));

	for (int i = 0; i < V; i++) {
		dist[i] = INT_MAX, sptSet[i] = false;
	}

	dist[src] = 0;
	for (int count = 0; count < V - 1; count++) {
		int u = minDistance(dist, sptSet);
		sptSet[u] = true;
		for (int v = 0; v < V; v++)
			if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v]) dist[v] = dist[u] + graph[u][v];
	}
	printSolution(dist, termino, output_file);
	free(dist);
	free(sptSet);
}

// LINKS UTILIZADOS:
// https://www.tutorialspoint.com/c-cplusplus-program-for-dijkstra-s-shortest-path-algorithm#:~:text=Step%201%20%3A%20Create%20a%20set,graph%20are%20in%20the%20shortPath.
// https://www.programiz.com/dsa/prim-algorithm
// https://www.programiz.com/dsa/graph-adjacency-matrix
// https://www.geeksforgeeks.org/how-does-c-allocate-memory-of-data-items-in-a-multidimensional-array/