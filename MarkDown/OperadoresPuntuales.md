# Actividad 2

## Instrucciones

Generar al menos cinco operadores puntuales utilizando la imagen generada o una imagen previamente cargada.

**Imagen Original**
![Serpiente](Imagenes/mandala.png)

**Primer Operador**
```python
import cv2 as cv

img = cv.imread('mandala.png', 0)
cv.imshow('salida', img)
x,y=img.shape
for i in range(x):
        for j in range(y):
                if(img[i,j]<100):
                        img[i,j]=25
                else:
                        img[i,j]=170

cv.imshow('OP1', img)
print( img.shape, x , y)
cv.waitKey(0)
cv.destroyAllWindows()
```

**Imagen en blanco y negro**
![Imagen en blanco y negro](Imagenes/BYN.png)

**Imagen 1: Negavita**
![Operador 1](Imagenes/OP1.png)

**Segundo Operador**
```python
import cv2 as cv

img = cv.imread('mandala.png', 0)
cv.imshow('salida', img)
x,y=img.shape
for i in range(x):
        for j in range(y):
                if(img[i,j]<150):
                        img[i,j]=255
                else:
                        img[i,j]=0

cv.imshow('OP2', img)
print( img.shape, x , y)
cv.waitKey(0)
cv.destroyAllWindows()
```
**Imagen 2**
![Operador 2](Imagenes/OP2.png)

**Tercer Operador**
```python
import cv2 as cv

img = cv.imread('mandala.png', 0)
cv.imshow('salida', img)
x,y=img.shape
for i in range(x):
        for j in range(y):
                if(img[i,j]<50):
                        img[i,j]=255
                else:
                        img[i,j]=50

cv.imshow('OP3', img)
print( img.shape, x , y)
cv.waitKey(0)
cv.destroyAllWindows()
```
**Imagen 3**
![Operador 3](Imagenes/OP3.png)

**Cuarto Operador**
```python
import cv2 as cv

img = cv.imread('mandala.png', 0)
cv.imshow('salida', img)
x,y=img.shape
for i in range(x):
        for j in range(y):
                if(img[i,j]>50):
                        img[i,j]=255
                else:
                        img[i,j]=0

cv.imshow('OP4', img)
print( img.shape, x , y)
cv.waitKey(0)
cv.destroyAllWindows()
```
**Imagen 4**
![Operador 4](Imagenes/OP4.png)

**Quinto Operador**
```python
import cv2 as cv

img = cv.imread('mandala.png', 0)
cv.imshow('salida', img)
x,y=img.shape
for i in range(x):
        for j in range(y):
                if(img[i,j]>100):
                        img[i,j]=255
                else:
                        img[i,j]=150

cv.imshow('OP5', img)
print( img.shape, x , y)
cv.waitKey(0)
cv.destroyAllWindows()
```
**Imagen 5**
![Operador 5](Imagenes/OP5.png)

**Operador extra: Imagen negativa**
```python
import cv2 as cv

img = cv.imread('mandala.png', 0)
cv.imshow('salida', img)
x,y=img.shape
for i in range(x):
        for j in range(y):
                if(img[i,j]>150):
                        img[i,j]=255
                else:
                        img[i,j]=0

cv.imshow('negativo', img)
print( img.shape, x , y)
cv.waitKey(0)
cv.destroyAllWindows()
```

**Imagen extra: Negavita**
![Operador Extra Negativo](Imagenes/OPExtra.png)