import cv2
import numpy as np

# Captura de video desde la cámara
cap = cv2.VideoCapture(0)

# Permitir que la cámara se estabilice
cv2.waitKey(2000)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir el cuadro a espacio de color HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definir el rango de color azul en HSV
    bajo_azul = np.array([90, 40, 40])
    alto_azul = np.array([130, 255, 255])

    # Crear una máscara que detecta el área azul
    mascara_azul = cv2.inRange(hsv, bajo_azul, alto_azul)

    # Convertir la imagen original a escala de grises
    imagen_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convertir la imagen gris a un formato BGR para que coincida con el formato de la imagen original
    imagen_gris_bgr = cv2.cvtColor(imagen_gris, cv2.COLOR_GRAY2BGR)

    # Combinar la imagen en gris con las áreas en azul resaltadas
    resultadoFinal = np.where(mascara_azul[:, :, None] == 255, frame, imagen_gris_bgr)

    # Mostrar el resultado final
    cv2.imshow('Color azul resaltado', resultadoFinal)

    # Presionar 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
