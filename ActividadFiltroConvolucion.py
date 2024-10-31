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
scaled_img = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)

# Aplicar el escalado
for i in range(x):
    for j in range(y):
        scaled_img[i*2, j*2] = img[i, j]

# Definir el kernel del filtro de convolución (filtro promedio)
matriz = np.ones((3, 3), dtype=np.float32) / 9  # Filtro 3x3
matrizTamanio = matriz.shape[0]  # Tamaño del kernel (3)

tiempo1 = time.time()

# Crear una nueva imagen para almacenar el resultado del filtro
filtered_img = np.zeros_like(scaled_img)

# Aplicar el filtro de convolución manualmente
for i in range(1, scaled_img.shape[0] - 1):  # Evitar bordes
    for j in range(1, scaled_img.shape[1] - 1):  # Evitar bordes
        # Inicializar la suma para el nuevo píxel
        valor_pixel = 0.0
        
        # Aplicar el kernel
        for k in range(matrizTamanio):
            for l in range(matrizTamanio):
                # Multiplicar el valor del píxel por el valor del kernel
                valor_pixel += scaled_img[i + k - 1, j + l - 1] * matriz[k, l]

        # Asignar el valor calculado al nuevo píxel
        filtered_img[i, j] = np.clip(valor_pixel, 0, 255)  # Asegurarse de que el valor esté en el rango correcto

tiempo2 = time.time()
print("Tiempo de inicio:", tiempo1)
print("Tiempo de fin:", tiempo2)
print("Tiempo total:", tiempo2 - tiempo1)

# Mostrar la imagen original, la imagen escalada y la imagen filtrada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Escalada', scaled_img)
cv.imshow('Imagen Filtrada', filtered_img)
cv.waitKey(0)
cv.destroyAllWindows()