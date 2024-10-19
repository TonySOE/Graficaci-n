import numpy as np
import cv2 as cv

rostro = cv.CascadeClassifier('haarcascade_frontalface_alt2.xml')
ojos = cv.CascadeClassifier('haarcascade_eye.xml')
cap = cv.VideoCapture(0)
x=y=w=h= 0 
count = 0
while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rostros = rostro.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in rostros:
        # Rectángulo del rostro
        frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Buscar los ojos
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detectamos los ojos dentro de la región del rostro
        detectar_ojos = ojos.detectMultiScale(roi_gray)
        
        # Dibujamos los círculos en los ojos
        for (ex, ey, ew, eh) in detectar_ojos[:2]:  # Tomamos solo los dos primeros ojos detectados
            center = (x + ex + ew // 2, y + ey + eh // 2)
            radius = ew // 4
            frame = cv.circle(frame, center, radius, (0, 255, 255), 2)  # Amarillo

        # Dibujamos la sonrisa roja en la parte inferior del rostro
        center_smile = (x + w // 2, y + int(0.75 * h))
        axes_smile = (w // 4, h // 8)
        frame = cv.ellipse(frame, center_smile, axes_smile, 0, 0, 180, (0, 0, 255), 2)  # Roja

    # Mostramos el frame con las detecciones
    cv.imshow('rostros', frame)
    
    k = cv.waitKey(1)
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()