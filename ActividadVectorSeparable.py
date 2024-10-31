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
        
# Definir el filtro convolucional 3x3 y normalizarlo
convolution_matrix = np.array([[1, 2, 1],
                               [2, 4, 2],
                               [1, 2, 1]], dtype=np.float32) / 16

filtered_img = np.zeros_like(scaled_img)

# Definir los vectores del filtro de convolución (1D)
vector_vertical = np.array([1, 2, 1], dtype=np.float32) / 4  # Normalizar dividiendo por 4
vector_horizontal = np.array([1, 2, 1], dtype=np.float32) / 4  # Normalizar dividiendo por 4

# Crear una imagen temporal para almacenar el resultado de la convolución vertical
temp_img = np.zeros_like(scaled_img)

# Iniciar el tiempo de procesamiento
tiempo1 = time.time()

# Aplicar el filtro vertical
for i in range(1, scaled_img.shape[0] - 1):
    for j in range(scaled_img.shape[1]):
        temp_img[i, j] = (
            scaled_img[i - 1, j] * vector_vertical[0] +
            scaled_img[i, j] * vector_vertical[1] +
            scaled_img[i + 1, j] * vector_vertical[2]
        )

# Crear una nueva imagen para almacenar el resultado del filtro completo (vertical + horizontal)
filtered2_img = np.zeros_like(scaled_img)

# Aplicar el filtro horizontal sobre la imagen temporal
for i in range(temp_img.shape[0]):
    for j in range(1, temp_img.shape[1] - 1):
        filtered2_img[i, j] = np.clip(
            temp_img[i, j - 1] * vector_horizontal[0] +
            temp_img[i, j] * vector_horizontal[1] +
            temp_img[i, j + 1] * vector_horizontal[2],
            0, 255
        )



# Iniciar el tiempo de procesamiento
tiempo3 = time.time()

# Aplicar el filtro convolucional 3x3
for i in range(1, scaled_img.shape[0] - 1):
    for j in range(1, scaled_img.shape[1] - 1):
        # Aplicar el filtro tomando los vecinos y multiplicando por la matriz de convolución
        region = scaled_img[i-1:i+2, j-1:j+2]
        filtered_value = np.sum(region * convolution_matrix)
        # Asignar el valor convolucionado al píxel de la imagen filtrada, aplicando clip para mantener entre 0 y 255
        filtered_img[i, j] = np.clip(filtered_value, 0, 255)

# Finalizar el tiempo de procesamiento
tiempo4 = time.time()


# Finalizar el tiempo de procesamiento
tiempo2 = time.time()
print("Tiempo separable de inicio:", tiempo1)
print("Tiempo de fin:", tiempo2)
print("Tiempo total:", tiempo2 - tiempo1)

print("Tiempo matrizde inicio:", tiempo3)
print("Tiempo de fin:", tiempo4)
print("Tiempo total:", tiempo4 - tiempo3)

# Mostrar la imagen original, la imagen escalada y la imagen filtrada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Escalada', scaled_img)
cv.imshow('Imagen Filtrada', filtered2_img)
cv.waitKey(0)
cv.destroyAllWindows()