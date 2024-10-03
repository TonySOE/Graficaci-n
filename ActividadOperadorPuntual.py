import cv2 as cv
import numpy as np

# Cargar la imagen en escala de grises
img = cv.imread('mandala.png', 0)

# Mostrar imagen original
cv.imshow('Imagen Original', img)

# Obtener dimensiones de la imagen
x, y = img.shape

# Aplicación 1: Corrección de imágenes (Escalado Lineal - Mejora de brillo y contraste)
alpha = 1.5  # Factor de escala (modifica el contraste)
beta = 30    # Desplazamiento (modifica el brillo)
escala_lineal = cv.convertScaleAbs(img, alpha=alpha, beta=beta)
cv.imshow('Correccion de imagen - Escalado Lineal', escala_lineal)

# Aplicación 2: Segmentación (Umbralización binaria)
threshold = 150
_, umbralizacion = cv.threshold(img, threshold, 255, cv.THRESH_BINARY)
cv.imshow('Segmentacion - Umbralizacion Binaria', umbralizacion)

# Aplicación 3: Análisis médico (Transformación Logarítmica)
c = 255 / np.log(1 + np.max(img))  # Constante de normalización
log_transform = c * (np.log(img + 1))  # Aplicación de la transformación logarítmica
log_transform = np.array(log_transform, dtype=np.uint8)
cv.imshow('Analisis medico - Transformacion Logaritmica', log_transform)

# Aplicación 4: Procesamiento en tiempo real (Inversión de Colores - Negativo)
negativo = 255 - img
cv.imshow('Procesamiento en tiempo real - Negativo', negativo)

# Aplicación 5: Procesamiento en tiempo real (Umbralización inversa)
umbral_inversa = img.copy()
for i in range(x):
    for j in range(y):
        if umbral_inversa[i, j] > threshold:
            umbral_inversa[i, j] = 0  # Píxeles mayores al umbral se hacen 0
        else:
            umbral_inversa[i, j] = 255  # Píxeles menores o iguales se hacen 255
cv.imshow('Procesamiento en tiempo real: Umbralizacion Inversa', umbral_inversa)

# Aplicación 6: Ecualización de Histograma
ecualizacion = cv.equalizeHist(img)  # Aplica la ecualización de histograma a la imagen
cv.imshow('Ecualizacion de Histograma', ecualizacion)

# Esperar a que el usuario presione cualquier tecla para continuar
cv.waitKey(0)

# Cerrar todas las ventanas
cv.destroyAllWindows()