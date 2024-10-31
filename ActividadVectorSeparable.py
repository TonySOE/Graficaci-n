import time
import cv2 as cv
import numpy as np

# Cargar la imagen en escala de grises
img = cv.imread('bob.png', 0)

# Obtener el tamaño de la imagen
x, y = img.shape

# Definir el factor de escala
scale_x, scale_y = 2, 2

# Crear una nueva imagen para almacenar el escalado
img_escalada = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)

# Aplicar el escalado
for i in range(x):
    for j in range(y):
        img_escalada[i*2, j*2] = img[i, j]

# Definir la matriz de convolución 3x3 y normalizarla
matriz_convolucion = np.array([[1, 2, 1],
                               [2, 4, 2],
                               [1, 2, 1]], dtype=np.float32) / 16

# Imagen para almacenar el resultado de la convolución 3x3
convolucion1 = np.zeros_like(img_escalada)

# Definir los vectores de convolución para el filtro separable (1D) y normalizar
vector_vertical = np.array([1, 2, 1], dtype=np.float32) / 4
vector_horizontal = np.array([1, 2, 1], dtype=np.float32) / 4

# Imagen temporal para almacenar el resultado de la convolución vertical (para filtro separable)
imagen_temporal = np.zeros_like(img_escalada)
convolucion2 = np.zeros_like(img_escalada)  # Para almacenar el resultado final del filtro separable

# Tiempo de inicio para la convolución separable
tiempo1 = time.time()

# Aplicar el filtro separable: convolución vertical
for i in range(1, img_escalada.shape[0] - 1):
    for j in range(img_escalada.shape[1]):
        imagen_temporal[i, j] = (
            img_escalada[i - 1, j] * vector_vertical[0] +
            img_escalada[i, j] * vector_vertical[1] +
            img_escalada[i + 1, j] * vector_vertical[2]
        )

# Aplicar el filtro separable: convolución horizontal sobre temp_img
for i in range(imagen_temporal.shape[0]):
    for j in range(1, imagen_temporal.shape[1] - 1):
        convolucion2[i, j] = np.clip(
            imagen_temporal[i, j - 1] * vector_horizontal[0] +
            imagen_temporal[i, j] * vector_horizontal[1] +
            imagen_temporal[i, j + 1] * vector_horizontal[2],
            0, 255
        )

# Tiempo final para la convolución separable
tiempo2 = time.time()

# Tiempo de inicio para la convolución completa 3x3
tiempo3 = time.time()

# Aplicar la convolución completa 3x3
for i in range(1, img_escalada.shape[0] - 1):
    for j in range(1, img_escalada.shape[1] - 1):
        # Obtener la región de vecinos 3x3
        region = img_escalada[i-1:i+2, j-1:j+2]
        # Calcular el valor convolucionado con la matriz 3x3
        valor_convolucionado = np.sum(region * matriz_convolucion)
        # Asignar el valor al píxel correspondiente en filtered_img
        convolucion1[i, j] = np.clip(valor_convolucionado, 0, 255)

# Tiempo final para la convolución completa 3x3
tiempo4 = time.time()

# Resultados de tiempo
print("Tiempo total 2 vectores:", tiempo2 - tiempo1)
print("Tiempo total matriz 3x3:", tiempo4 - tiempo3)

# Mostrar las imágenes: original, escalada, y filtradas (separable y completa)
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Escalada', img_escalada)
cv.imshow('Imagen Filtrada - Convolución Separable', convolucion2)
cv.imshow('Imagen Filtrada - Convolución Completa', convolucion1)
cv.waitKey(0)
cv.destroyAllWindows()