import cv2 as cv
import numpy as np

img = np.ones((600, 900, 3), dtype = np.uint8) * 255

# Cielo
cv.rectangle(img, (0, 0), (900, 600), (246, 209, 0), -1)

# Montaña 1
pts = np.array([[-400, 600], [200, 200], [400, 600]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.fillPoly(img, [pts], (21, 28, 8))

## Nube izquierda
cv.circle(img, (300, 200), 40, (255, 255, 255), -1)
cv.circle(img, (260, 220), 60, (255, 255, 255), -1)
cv.circle(img, (210, 210), 50, (255, 255, 255), -1)

# Montaña 2
pts = np.array([[200, 600], [300, 170], [600, 600]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.fillPoly(img, [pts], (21, 28, 8))

# Montaña 3
pts = np.array([[400, 600], [550, 220], [800, 600]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.fillPoly(img, [pts], (21, 28, 8))

# Montaña 4
pts = np.array([[600, 600], [750, 160], [900, 600]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.fillPoly(img, [pts], (21, 28, 8))

# Montaña 5
pts = np.array([[700, 600], [850, 180], [1000, 600]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.fillPoly(img, [pts], (21, 28, 8))

# Montaña 6
pts = np.array([[200, 600], [500, 180], [600, 600]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.fillPoly(img, [pts], (21, 28, 8))

# Círculo del sol
cv.circle(img, (10, 0), 200, (0, 190, 255), -1)

## Nube centro
cv.circle(img, (400, 100), 50, (255, 255, 255), -1)
cv.circle(img, (460, 100), 80, (255, 255, 255), -1)
cv.circle(img, (550, 120), 50, (255, 255, 255), -1)

# Nube derecha
cv.circle(img, (700, 150), 70, (255, 255, 255), -1)
cv.circle(img, (760, 140), 80, (255, 255, 255), -1)
cv.circle(img, (830, 130), 60, (255, 255, 255), -1)

# Rayos del sol
cv.line(img, (10, 220), (10, 300), (0, 220, 255), 5)
cv.line(img, (70, 210), (90, 270), (0, 220, 255), 5)
cv.line(img, (130, 190), (180, 250), (0, 220, 255), 5)
cv.line(img, (180, 170), (250, 220), (0, 220, 255), 5)
cv.line(img, (210, 130), (290, 180), (0, 220, 255), 5)
cv.line(img, (230, 70), (310, 90), (0, 220, 255), 5)   
cv.line(img, (240, 10), (330, 10), (0, 220, 255), 5)    

# Pasto
cv.rectangle(img, (0, 450), (900, 900), (0, 180, 0), -1) # Coordenada, tamañó, color, grosor de la línea

# Casita
cv.rectangle(img, (520, 400), (780, 550), (0, 64, 128), -1) # Cuerpo
cv.rectangle(img, (620, 470), (670, 550), (0, 20, 100), -1) # Puerta
cv.circle(img, (630, 510), 5, (0, 0, 0), -1)                # Cerrojo
cv.rectangle(img, (540, 430), (600, 510), (230, 216, 200), -1) # Ventana izquierda
cv.line(img, (550, 435), (580, 480), (0, 0, 0), 3)           # Reflejo en ventana 
cv.line(img, (565, 445), (595, 490), (0, 0, 0), 3)           # Reflejo en ventana 
cv.rectangle(img, (690, 430), (760, 510), (230, 216, 200), -1) # Ventana derecha
cv.line(img, (700, 435), (740, 480), (0, 0, 0), 3)           # Reflejo en ventana 
cv.line(img, (720, 445), (755, 490), (0, 0, 0), 3)           # Reflejo en ventana 
pts = np.array([[520, 400], [780, 400], [650, 300]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.fillPoly(img, [pts], (82, 181, 255)) # Dibujar el triángulo (techo) sobre la figura

# Vaca
cv.rectangle(img, (200, 470), (300, 520), (255, 255, 255), -1) # Cuerpo
cv.line(img, (180, 520), (200, 475), (255, 255, 255), 5)       # Cola
cv.rectangle(img, (200, 520), (220, 550), (255, 255, 255), -1) # Pata atrás
cv.rectangle(img, (280, 520), (300, 550), (255, 255, 255), -1) # Pata delantera
cv.circle(img, (310, 470), 23, (255, 255, 255), -1)            # Cabeza
cv.circle(img, (220, 480), 10, (0, 0, 0), -1)            # Mancha
cv.circle(img, (230, 510), 10, (0, 0, 0), -1)            # Mancha
cv.circle(img, (240, 495), 5, (0, 0, 0), -1)             # Mancha
cv.circle(img, (260, 490), 15, (0, 0, 0), -1)            # Mancha
cv.circle(img, (280, 485), 12, (0, 0, 0), -1)            # Mancha
cv.circle(img, (302, 465), 5, (0, 0, 0), -1)             # Ojo izquierdo
cv.circle(img, (318, 465), 5, (0, 0, 0), -1)             # Ojo izquierdo
cv.line(img, (308, 475), (312, 475), (0, 0, 0), 2)       # Boca

cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows