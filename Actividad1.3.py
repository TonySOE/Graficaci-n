import cv2 as cv
import numpy as np
import math

# Cargar la imagen en escala de grises
img = cv.imread('tr.png', 0)

# Obtener el tamaño de la imagen original
x, y = img.shape

# Crear una imagen vacía para almacenar el resultado, con espacio para traslación y escalado
imgRST = np.zeros((int(x * 4), int(y * 4)), dtype=np.uint8)
xx, yy = imgRST.shape

# Definir el desplazamiento en x e y
dx, dy = 20, 20 

# Definir el factor de escala
scale = 2  

# Calcular el centro de la imagen
cx, cy = int(x // 2), int(y // 2)

# Definir el ángulo de rotación (en grados) y convertirlo a radianes
angle = 70
theta = math.radians(angle)

# Rotar, escalar y trasladar la imagen directamente en las fórmulas de coordenadas
for i in range(x):
    for j in range(y):
        # Aplicar la rotación, escala y traslación en una sola fórmula
        rotated_x = int(((j - cx) * math.cos(theta) * scale) - ((i - cy) * math.sin(theta) * scale) + cx + dx)
        rotated_y = int(((j - cx) * math.sin(theta) * scale) + ((i - cy) * math.cos(theta) * scale) + cy + dy)
        
        # Verificar si el nuevo píxel está dentro de los límites de la imagen resultante
        if 0 <= rotated_x < yy and 0 <= rotated_y < xx:
            imgRST[rotated_y, rotated_x] = img[i, j]

# Mostrar la imagen original y la rotada con escalado y traslación
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Rotada, Escalada y Trasladada', imgRST)
cv.waitKey(0)
cv.destroyAllWindows()
