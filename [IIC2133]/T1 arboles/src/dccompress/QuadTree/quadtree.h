#pragma once

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#include "../../imagelib/imagelib.h"

typedef struct QuadtreeNode {
	// ancho de la imagen
	int width;
	/** Alto de la imagen */
	int height;
	int x;
	int y;
	struct QuadtreeNode *top_left;
	struct QuadtreeNode *top_right;
	struct QuadtreeNode *bottom_left;
	struct QuadtreeNode *bottom_right;
	bool hoja;
} QuadtreeNode;

QuadtreeNode *quadtree_create(int height, int width);
void quadtree_completed(QuadtreeNode *root);

float *calculate_delta(QuadtreeNode *node, Image *image);
void alpha_filter(QuadtreeNode *node, Image *image, int alpha);

int compresion_filter(QuadtreeNode *node, Image *image, int alpha);
int compresion(QuadtreeNode *node, Image *image, int h, int alpha, int min, int max);

void free_tree(QuadtreeNode *node);
