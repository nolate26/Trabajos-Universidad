#pragma once

struct color_lab {
  /** Canal de Luminosidad */
  double L;
 /** Canal Magenta / Verde */
  double a;
  /** Canal Azul / Amarillo */
  double b;
};
/** Representa un color en el espacio CIE-Lab */
typedef struct color_lab Color;

struct image {
  /** La imagen en sí, una matriz 2D de colores */
  Color** pixels;
  /** Ancho de la imagen */
  int width;
  /** Alto de la imagen */
  int height;
};
/** Representa la imagen CIE-Lab como una matriz de colores */
typedef struct image Image;

/** Lee una imagen .png y la convierte en una matriz de colores */
Image* img_png_read_from_file (char* filename);
/** Pinta el cuadrado que va de (row, col) a (row + size - 1, col + size - 1) */
void   img_square_paint       (Image* img, int row, int col, int size, Color c);
/** Escribe la matriz de colores al archivo .png especificado */
void   img_png_write_to_file  (Image* img, char* filename);
/** Libera los recursos usados por la imagen */
void   img_png_destroy        (Image* img);
