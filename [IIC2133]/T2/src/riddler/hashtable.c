#include "hashtable.h"

#include <stdbool.h>

void insert_or_update(HashItem **table, int key, Node *root, int h2) {
	HashItem *item = table[key];
	if (item == NULL) {
		item = calloc(1, sizeof(HashItem));
		item->key = key;
		item->node = root;
		item->h = h2;
		item->next = NULL;
		item->down = NULL;
		table[key] = item;
	}
	else {
		while (item->h != h2) {
			if (item->next == NULL) {
				item->next = calloc(1, sizeof(HashItem));
				item->next->key = key;
				item->next->node = root;
				item->next->h = h2;
				item->next->next = NULL;
				item->next->down = NULL;
				return;
			}
			item = item->next;
		}
		while (item->down != NULL) {
			item = item->down;
		}
		item->down = calloc(1, sizeof(HashItem));
		item->down->key = key;
		item->down->node = root;
		item->down->h = h2;
		item->down->next = NULL;
		item->down->down = NULL;
	}
}

// entregar el arbol y calcular acá para revisar
void fetch_value(HashItem **table, Node *root, int h2, FILE *output_file, int arr[]) {
	int key;
	key = calculate_hash_fetch(root, h2);
	HashItem *item = table[key];
	if (item == NULL) {
		fprintf(output_file, "%d\n", -1);
		return;
	}

	while (item->h != h2) {
		if (item->next == NULL) {
			fprintf(output_file, "%d\n", -1);
			return;
		}
		item = item->next;
	}
	int contador = 0;

	while (item != NULL) {
		bool is_ok;
		is_ok = check(item->node, root);
		if (is_ok) {
			contador += 1;
			fprintf(output_file, "%d ", item->node->indice);
		}
		item = item->down;
	}
	if (contador == 0) {
		fprintf(output_file, "%d ", -1);
	}
	fprintf(output_file, "\n");
}

bool isPrime(int n) {
	// Corner cases
	if (n <= 1) return false;
	if (n <= 3) return true;

	// This is checked so that we can skip
	// middle five numbers in below loop
	if (n % 2 == 0 || n % 3 == 0)
		return false;

	for (int i = 5; i * i <= n; i = i + 6)
		if (n % i == 0 || n % (i + 2) == 0)
			return false;

	return true;
}

// Function to return the smallest
// prime number greater than N
int nextPrime(int N) {
	// Base case
	if (N <= 1)
		return 2;

	int prime = N;
	bool found = false;
	while (!found) {
		prime += 1;

		if (isPrime(prime))
			found = true;
	}
	return prime;
}

int calculate_hash(HashItem **tabla, Node *root, int h) {
	int hash;
	if (h == 1) {
		hash = root->value << 1;
		return hash;
	}
	else {
		hash = (root->value << 1) ^ (calculate_hash(tabla, root->left_child, h - 1)) ^ (calculate_hash(tabla, root->right_child, h - 1));
		insert_or_update(tabla, hash, root, h);
		return hash;
	}
}
int calculate_hash_fetch(Node *root, int h) {
	int hash;
	if (h == 1) {
		hash = root->value << 1;
		return hash;
	}
	else {
		hash = (root->value << 1) ^ (calculate_hash_fetch(root->left_child, h - 1)) ^ (calculate_hash_fetch(root->right_child, h - 1));
		return hash;
	}
}

bool check(Node *esta, Node *revisar) {
	/* base cases */
	if (revisar == NULL)
		return true;

	/* Check if the data of both roots is same and data of left and right
	   subtrees are also same */
	return (esta->value == revisar->value &&
	        check(esta->left_child, revisar->left_child) &&
	        check(esta->right_child, revisar->right_child));
}

void free_linkedlist(HashItem *list) {
	HashItem *temp;
	while (list != NULL) {
		temp = list;
		list = list->down;
		free(temp);
	}
}

void free_table(HashItem **table, int range) {
	// Frees the table
	for (int i = 0; i < range; i++) {
		HashItem *item = table[i];
		while (item != NULL) {
			HashItem *temp = item;
			item = item->next;
			free_linkedlist(temp);
		}
	}
}
void free_tree(Node *node) {
	// post-order like FatalError hinted at
	if (node != NULL) {
		free_tree(node->right_child);
		free_tree(node->left_child);
		free(node);
	}
}