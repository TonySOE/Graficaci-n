import cv2 as cv
import numpy as np

# Cargar la imagen en escala de grises
img = cv.imread('Newton.png', 0)

# Obtener el tamaño de la imagen
x, y = img.shape

# Definir el factor de escala
scale_x, scale_y = 2, 2

# Crear una nueva imagen para almacenar el escalado
scaled_img = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)

# Aplicar el escalado
for i in range(x):
    for j in range(y):
        scaled_img[i*2, j*2] = img[i, j]

# Definir el kernel del filtro de convolución (filtro promedio)
kernel = np.ones((3, 3), dtype=np.float32) / 9  # Filtro 3x3

# Aplicar el filtro de convolución a la imagen escalada
filtered_img = cv.filter2D(scaled_img, -1, kernel)

# Mostrar la imagen original, la imagen escalada y la imagen filtrada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Escalada', scaled_img)
cv.imshow('Imagen Filtrada', filtered_img)
cv.waitKey(0)
cv.destroyAllWindows()
