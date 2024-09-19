import cv2 as cv
import numpy as np
import math

# Cargar la imagen en escala de grises
img = cv.imread('tr.png', 0)

# Obtener el tamaño de la imagen original
x, y = img.shape

# Crear una imagen vacía para almacenar el resultado con suficiente espacio
imgRS = np.zeros((int(x * 3), int(y * 3)), dtype=np.uint8)  # Tamaño suficientemente grande para todas las transformaciones
xx, yy = imgRS.shape

# Definir el factor de escala
scale = 2  # Escala de 2 (multiplicación por 2)

# Calcular el centro de la imagen original
cx, cy = int(x // 2), int(y // 2)

# Definir los ángulos de rotación (en grados) y convertirlos a radianes
angle1 = 30  # Rotación en sentido horario
theta1 = math.radians(angle1)

angle2 = 60  # Rotación en sentido antihorario
theta2 = math.radians(-angle2)

# Aplicar la primera rotación (30 grados en sentido horario)
for i in range(x):
    for j in range(y):
         # Primera rotación
        rotated_x1 = int((j - cx) * math.cos(theta1) - (i - cy) * math.sin(theta1) + cx)
        rotated_y1 = int((j - cx) * math.sin(theta1) + (i - cy) * math.cos(theta1) + cy)

        # Aplicar la segunda rotación (60 grados en sentido antihorario) sobre el resultado de la primera
        rotated_x2 = int((rotated_x1 - cx) * math.cos(theta2) - (rotated_y1 - cy) * math.sin(theta2) + cx)
        rotated_y2 = int((rotated_x1 - cx) * math.sin(theta2) + (rotated_y1 - cy) * math.cos(theta2) + cy)
        
        # Escalar después de las rotaciones
        scaled_x = int(rotated_x2 * scale)
        scaled_y = int(rotated_y2 * scale)

        # Verificar si el píxel escalado está dentro de los límites de la imagen final
        if 0 <= scaled_x < yy and 0 <= scaled_y < xx:
            imgRS[scaled_y, scaled_x] = img[i, j]

# Mostrar la imagen original y la rotada con escalado y traslación
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Rotada y Escalada', imgRS)
cv.waitKey(0)
cv.destroyAllWindows()
