#pragma once
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#include "node.h"

typedef struct hashitem_t {
	int key;
	struct node_t *node;
	int h;
	struct hashitem_t *next;
	struct hashitem_t *down;
} HashItem;

int calculate_hash_fetch(Node *root, int h);
void insert_or_update(HashItem **table, int key, Node *root, int h2);

void fetch_value(HashItem **table, Node *root, int h2, FILE *output_file, int arr[]);

bool isPrime(int n);
int nextPrime(int N);

int calculate_hash(HashItem **tabla, Node *root, int h);

// bool check(int arr[], int i, Node *node);
bool check(Node *esta, Node *revisar);
void free_linkedlist(HashItem *list);
void free_table(HashItem **table, int range);
// void add_subtree(int i, char *arbol, int h_actual, int h_quiero, int h, int N);
void free_tree(Node *node);