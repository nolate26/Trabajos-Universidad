#include "node.h"

Node* node_create(int value, int indice) {
	Node* node = (Node*)calloc(1, sizeof(Node));
	node->value = value;
	node->indice = indice;
	return node;
}

Node* insertLevelOrder(int arr[], int i, int n) {
	Node* root = NULL;
	// Base case for recursion
	if (i < n) {
		root = node_create(arr[i], i + 1);

		// insert left child
		root->left_child = insertLevelOrder(arr, 2 * i + 1, n);

		// insert right child
		root->right_child = insertLevelOrder(arr, 2 * i + 2, n);
	}
	return root;
}

void print_tree(Node* root) {
	printf("%d ", root->value);
	if (root->left_child) {
		print_tree(root->left_child);
	};
	if (root->right_child) {
		print_tree(root->right_child);
	};
}
