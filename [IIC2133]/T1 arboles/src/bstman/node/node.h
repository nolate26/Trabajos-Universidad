#pragma once
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node_t {
	int value;
	struct node_t* left_child;
	struct node_t* right_child;
} Node;

Node* node_create(int value);
void insert_node(Node* root, Node* node);
void print_tree(Node* root);
void find_parent(Node* root, int value);
// Nuevas funciones
void path_value(Node* root, int value, FILE* output_file);

int getLevel(Node* node, int valor);
int getLevelUtil(Node* node, int data, int level);

void Order(Node* root, FILE* output_file);

// subtree
bool areIdentical(Node* root1, Node* root2);
bool isSubtree(Node* T, Node* S);
//
void free_tree(Node* node);