
#include "quadtree.h"

#include <math.h>
#include <stdbool.h>
#include <stdio.h>

#include "../../imagelib/imagelib.h"

QuadtreeNode* quadtree_create(int height, int width) {
	QuadtreeNode* node = (QuadtreeNode*)calloc(1, sizeof(QuadtreeNode));
	node->height = height;
	node->width = width;
	node->hoja = false;
	return node;
}

void quadtree_completed(QuadtreeNode* root) {
	if (root->width != 1) {
		root->top_left = quadtree_create(root->height / 2, root->width / 2);
		root->top_left->x = root->x;
		root->top_left->y = root->y;

		root->top_right = quadtree_create(root->height / 2, root->width / 2);
		root->top_right->x = root->x + (root->width / 2);
		root->top_right->y = root->y;

		root->bottom_left = quadtree_create(root->height / 2, root->width / 2);
		root->bottom_left->x = root->x;
		root->bottom_left->y = root->y + (root->height / 2);

		root->bottom_right = quadtree_create(root->height / 2, root->width / 2);
		root->bottom_right->x = root->x + (root->width / 2);
		root->bottom_right->y = root->y + (root->height / 2);

		quadtree_completed(root->top_left);
		quadtree_completed(root->top_right);
		quadtree_completed(root->bottom_left);
		quadtree_completed(root->bottom_right);
	}
}

void alpha_filter(QuadtreeNode* node, Image* image, int alpha) {
	float* delta;
	delta = calculate_delta(node, image);

	if (delta[0] <= alpha) {
		img_square_paint(
		    image,
		    node->x,
		    node->y,
		    node->height,
		    (Color){.L = delta[1], .a = delta[2], .b = delta[3]});
	}
	else {
		alpha_filter(node->top_left, image, alpha);
		alpha_filter(node->top_right, image, alpha);
		alpha_filter(node->bottom_left, image, alpha);
		alpha_filter(node->bottom_right, image, alpha);
	}
}

int compresion_filter(QuadtreeNode* node, Image* image, int alpha) {
	float* delta;
	delta = calculate_delta(node, image);

	if (delta[0] <= alpha || node->width == 1) {
		return 1;
	}
	else {
		return (compresion_filter(node->top_left, image, alpha) + compresion_filter(node->top_right, image, alpha) + compresion_filter(node->bottom_left, image, alpha) + compresion_filter(node->bottom_right, image, alpha));
	}
}

// alpha comienza en 64
// min empieza en 1
// max 128

// mayor alpha -> menos h
// alpha = 0 -> todos los nodos
int compresion(QuadtreeNode* node, Image* image, int h, int alpha, int min, int max) {
	int num;

	num = compresion_filter(node, image, alpha);

	if (h < num) {
		return compresion(node, image, h, alpha + ((alpha - min) / 2), alpha, max);
	}
	else if (h == num) {
		return alpha;
	}
	else {
		num = compresion_filter(node, image, alpha - 1);

		if (h < num) {
			return alpha;
		}
		else {
			return compresion(node, image, h, alpha - ((alpha - min) / 2), min, alpha);
		}
	}
}

float* calculate_delta(QuadtreeNode* node, Image* image) {
	float delta;
	int n = node->width * node->height;
	int i, j;
	float sum_L = 0.0, mean_L, SD_L;
	float sum_a = 0.0, mean_a, SD_a;
	float sum_b = 0.0, mean_b, SD_b;
	for (i = node->x; i < node->x + node->width; i++) {
		for (j = node->y; j < node->y + node->height; j++) {
			sum_L += image->pixels[i][j].L;
			sum_a += image->pixels[i][j].a;
			sum_b += image->pixels[i][j].b;
		}
	}
	// Calculamos promedio
	mean_L = sum_L / n;
	mean_a = sum_a / n;
	mean_b = sum_b / n;

	// Calculamos SD
	float sum_1 = 0.0;
	float sum_2 = 0.0;
	float sum_3 = 0.0;
	for (i = node->x; i < node->x + node->width; i++) {
		for (j = node->y; j < node->y + node->height; j++) {
			sum_1 += (image->pixels[i][j].L - mean_L) * (image->pixels[i][j].L - mean_L);
			sum_2 += (image->pixels[i][j].a - mean_a) * (image->pixels[i][j].a - mean_a);
			sum_3 += (image->pixels[i][j].b - mean_b) * (image->pixels[i][j].b - mean_b);
		}
	}
	SD_L = sqrt(sum_1 / n);
	SD_a = sqrt(sum_2 / n);
	SD_b = sqrt(sum_3 / n);
	delta = (SD_L + SD_a + SD_b) / 3;

	static float r[4];
	r[0] = delta;
	r[1] = mean_L;
	r[2] = mean_a;
	r[3] = mean_b;
	return r;
}

void free_tree(QuadtreeNode* node) {
	if (node != NULL) {
		free_tree(node->top_left);
		free_tree(node->top_right);
		free_tree(node->bottom_right);
		free_tree(node->bottom_left);
		free(node);
	}
}