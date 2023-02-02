#pragma once
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node_t {
	int value;
	int indice;
	struct node_t* left_child;
	struct node_t* right_child;
} Node;

Node* node_create(int value, int indice);
Node* insertLevelOrder(int arr[], int i, int n);
void print_tree(Node* root);