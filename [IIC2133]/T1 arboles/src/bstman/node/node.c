#include "node.h"

Node* node_create(int value) {
	Node* node = (Node*)calloc(1, sizeof(Node));
	node->value = value;
	return node;
}

// revisar caso que hay empate de valores
void insert_node(Node* root, Node* node) {
	Node* actual_node = root;
	bool is_inserted = false;

	while (!is_inserted) {
		if (actual_node->value == node->value) {
			is_inserted = true;
		}

		else if (actual_node->value > node->value) {
			if (actual_node->left_child) {
				actual_node = actual_node->left_child;
			}
			else {
				actual_node->left_child = node;
				is_inserted = true;
			}
		}
		else {
			if (actual_node->right_child) {
				actual_node = actual_node->right_child;
			}
			else {
				actual_node->right_child = node;
				is_inserted = true;
			}
		}
	}
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

void find_parent(Node* root, int value) {
	Node* actual_node = root;
	while (1) {
		if (actual_node->value > value) {
			if (actual_node->left_child->value == value) {
				printf("%d ", actual_node->value);
				break;
			}
			actual_node = actual_node->left_child;
		}
		else {
			if (actual_node->right_child->value == value) {
				printf("%d ", actual_node->value);
				break;
			}
			actual_node = actual_node->right_child;
		}
	}
}

// FUNCIONES:
// 1. path
void path_value(Node* root, int value, FILE* output_file) {
	Node* actual_node = root;
	while (1) {
		if (actual_node->value > value) {
			fprintf(output_file, "%d ", actual_node->value);
			if (!actual_node->left_child) {
				fprintf(output_file, "X\n");
				break;
			}
			actual_node = actual_node->left_child;
		}
		else if (actual_node->value < value) {
			fprintf(output_file, "%d ", actual_node->value);
			if (!actual_node->right_child) {
				fprintf(output_file, "X\n");
				break;
			}
			actual_node = actual_node->right_child;
		}

		else {
			fprintf(output_file, "%d\n", actual_node->value);
			break;
		}
	}
}

// DEEP

// Helper function for getLevel(). It returns level of the
// data if data is present in tree, otherwise returns 0.
int getLevelUtil(Node* node, int data, int level) {
	if (!node)
		return 0;

	if (node->value == data)
		return level;

	int downlevel = getLevelUtil(node->left_child, data, level + 1);
	if (downlevel != 0)
		return downlevel;

	downlevel = getLevelUtil(node->right_child, data, level + 1);
	return downlevel;
}
/* Returns level of given data value */
int getLevel(Node* node, int valor) {
	return getLevelUtil(node, valor, 0);
}
///
/// ORDER:
void Order(Node* root, FILE* output_file) {
	Node* actual_node = root;
	if (!actual_node) {
		return;
	}
	Order(root->left_child, output_file);
	fprintf(output_file, "%d ", root->value);
	Order(root->right_child, output_file);
}

///
// SUBTREE
//
bool areIdentical(Node* root1, Node* root2) {
	/* base cases */
	if (root1 == NULL && root2 == NULL)
		return true;

	if (root1 == NULL || root2 == NULL)
		return false;

	/* Check if the data of both roots is same and data of left and right
	   subtrees are also same */
	return (root1->value == root2->value &&
	        areIdentical(root1->left_child, root2->left_child) &&
	        areIdentical(root1->right_child, root2->right_child));
}

/* This function returns true if S is a subtree of T, otherwise false */
bool isSubtree(Node* T, Node* S) {
	/* base cases */
	if (S == NULL)
		return true;

	if (T == NULL)
		return false;

	/* Check the tree with root as current node */
	if (areIdentical(T, S))
		return true;

	/* If the tree with root as current node doesn't match then
	   try left and right subtrees one by one */
	return isSubtree(T->left_child, S) ||
	       isSubtree(T->right_child, S);
}

///
// CREAR FUNCIÓN PARA ELIMINAR MEMORIA -
//
void free_tree(Node* node) {
	// post-order like FatalError hinted at
	if (node != NULL) {
		free_tree(node->right_child);
		free_tree(node->left_child);
		free(node);
	}
}
