import cv2
import numpy as np

# Leer la imagen en formato RGB
imagen = cv2.imread('Newton.png', 1)

# Convertir la imagen de RGB a HSV
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Definir el rango de color rojo en HSV
bajo_rojo1 = np.array([0, 40, 40])
alto_rojo1 = np.array([10, 255, 255])
bajo_rojo2 = np.array([160, 40, 40])
alto_rojo2 = np.array([180, 255, 255])

# Definir el rango de color verde en HSV (rango correcto para verde)
bajo_verde = np.array([35, 40, 40])
alto_verde = np.array([85, 255, 255])

# Definir el rango de color amarillo en HSV
bajo_amarillo = np.array([25, 40, 40])
alto_amarillo = np.array([35, 255, 255])

# Definir el rango de color azul en HSV
bajo_azul = np.array([90, 40, 40])
alto_azul = np.array([130, 255, 255]) 

# Definir el rango de color magenta en HSV
bajo_magenta = np.array([140, 40, 40])
alto_magenta = np.array([160, 255, 255])

# Crear una máscara para el color rojo
mascara_rojo1 = cv2.inRange(imagen_hsv, bajo_rojo1, alto_rojo1)
mascara_rojo2 = cv2.inRange(imagen_hsv, bajo_rojo2, alto_rojo2)
mascara_rojo = cv2.add(mascara_rojo1, mascara_rojo2)

# Crear una máscara para el color verde
mascara_verde = cv2.inRange(imagen_hsv, bajo_verde, alto_verde)

# Crear una máscara para el color amarillo
mascara_amarillo = cv2.inRange(imagen_hsv, bajo_amarillo, alto_amarillo)

# Crear una máscara para el color azul
mascara_azul = cv2.inRange(imagen_hsv, bajo_azul, alto_azul)

# Crear una máscara para el color magenta
mascara_magenta = cv2.inRange(imagen_hsv, bajo_magenta, alto_magenta)

# Convertir la imagen original a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Convertir la imagen gris a un formato BGR para que coincida con la original
imagen_gris_bgr = cv2.cvtColor(imagen_gris, cv2.COLOR_GRAY2BGR)

# Combinar la imagen en gris con las áreas en rojo y verde
resultadoRojo = np.where(mascara_rojo[:, :, None] == 255, imagen, imagen_gris_bgr)
resultadoVerde = np.where(mascara_verde[:, :, None] == 255, imagen, imagen_gris_bgr)
resultadoAzul = np.where(mascara_azul[:, :, None] == 255, imagen, imagen_gris_bgr)
resultadoAmarillo = np.where(mascara_amarillo[:, :, None] == 255, imagen, imagen_gris_bgr)
resultadoMagenta = np.where(mascara_magenta[:, :, None] == 255, imagen, imagen_gris_bgr)

# Mostrar la imagen final
cv2.imshow('Color rojo resaltado', resultadoRojo)
cv2.imshow('Color verde resaltado', resultadoVerde)
cv2.imshow('Color azul resaltado', resultadoAzul)
cv2.imshow('Color amarillo resaltado', resultadoAmarillo)
cv2.imshow('Color magenta resaltado', resultadoMagenta)

resultadoVerde = np.where(mascara_verde[:, :, None] == 255, imagen, resultadoRojo)
resultadoAmarillo = np.where(mascara_amarillo[:, :, None] == 255, imagen, resultadoVerde)
resultadoAzul = np.where(mascara_azul[:, :, None] == 255, imagen, resultadoAmarillo)
resultadoFinal = np.where(mascara_magenta[:, :, None] == 255, imagen, resultadoAzul)

# Mostrar la imagen final con todos los colores resaltados
cv2.imshow('Colores rojo, verde, amarillo, azul y magenta resaltados ', resultadoFinal)
cv2.waitKey(0)
cv2.destroyAllWindows()