# Actividad 6

## Instrucciones

Programar al menos 10 ecuaciones paramétricas y modificar 1 vez la ecuación.

No se insertarán todos los códigos, debido a que es lo mismo, solo se dirá qué valor de K se utilizó para cada imagen.  

**Código base para las demás imágenes**  

```python
import numpy as np
import cv2


# Definir los parámetros iniciales
width, height = 1000, 1000  # Ampliar la ventana para ver toda la figura
img = np.ones((height, width, 3), dtype=np.uint8)*255

# Parámetros de la curva de Limacon
a, b = 150, 100  # Reducir los valores de a y b para que la curva se ajuste mejor
k = 10# Constante de multiplicación del ángulo
theta_increment = 0.05  # Incremento del ángulo
max_theta = 2 * np.pi  # Un ciclo completo

# Centro de la imagen
center_x, center_y = width // 2, height // 2

theta = 0  # Ángulo inicial

while True:  # Bucle infinito
    # Limpiar la imagen
    img = np.ones((width, height, 3), dtype=np.uint8) * 255
    
    # Dibujar la curva completa desde 0 hasta theta
    for t in np.arange(0, theta, theta_increment):
        # Calcular las coordenadas paramétricas (x, y) para la curva de Limacon
        r = a + b * np.cos(k * t)
        x = int(center_x + r * np.cos(t))
        y = int(center_y + r * np.sin(t))
        
        # Dibujar un círculo en la posición calculada
        cv2.circle(img, (x, y), 1, (0, 234, 0), 1)  # Color rojo
        cv2.circle(img, (x-2, y-2), 1, (0, 0, 0), 1)  # Color rojo
    
    # Mostrar la constante k en la imagen
    #cv2.putText(img, f"k = {k:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Mostrar la imagen
    cv2.imshow("Parametric Animation", img)
    img = np.ones((width, height, 3), dtype=np.uint8) * 255
    
    # Incrementar el ángulo
    theta += theta_increment
    
    # Reiniciar theta si alcanza su valor máximo
    #if theta >= max_theta:
    #    theta = 0  # Reinicia la animación para que se repita

    # Pausar para ver la animación
    if cv2.waitKey(30) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
        break

# Cerrar la ventana al finalizar
cv2.destroyAllWindows()
```

**Ecuación 1**  

K = 0.7  

![k=0.7](Imagenes/k%20=%200.7.png)  

**Ecuación 2**  

K = 1  

![k=1](Imagenes/K%20=%201.png)  

**Ecuación 3**  

K = 2.5  

![k=2.5](Imagenes/k%20=%202.5.png)  

**Ecuación 4**  

K = 3.75  

![k=3.75](Imagenes/k%20=%203.75.png)  

**Ecuación 5**  

K = 5.25  

![k=5.25](Imagenes/k%20=%205.25.png)  

**Ecuación 6**  

K = 6.5  

![k=6.5](Imagenes/k%20=%206.5.png)

**Ecuación 7**  

K = 7  

![k=7](Imagenes/k%20=%207.png)  

**Ecuación 8**  

K = 10  

![k=10](Imagenes/k%20=%2010.png)  

**Ecuación 9**  

K = 13.5  

![k=13.5](Imagenes/k%20=%2013.5.png)  

**Ecuación 10**  

K = 25  

![k=25](Imagenes/k%20=%2025.png)  

**Ecuación modificada: Espiral de Arquímedes**  

```python
import numpy as np
import cv2

# Definir los parámetros iniciales
width, height = 1000, 1000  # Ampliar la ventana para ver toda la figura
img = np.ones((height, width, 3), dtype=np.uint8)*255

# Parámetros de la espiral de Arquímedes
a, b = 5, 5  # Constantes de la espiral
theta_increment = 0.05  # Incremento del ángulo
max_theta = 12 * np.pi  # Aumentar el ciclo completo para más vueltas

# Centro de la imagen
center_x, center_y = width // 2, height // 2

theta = 0  # Ángulo inicial

while True:  # Bucle infinito
    # Limpiar la imagen
    img = np.ones((width, height, 3), dtype=np.uint8) * 255
    
    # Dibujar la espiral completa desde 0 hasta theta
    for t in np.arange(0, theta, theta_increment):
        # Calcular las coordenadas paramétricas (x, y) para la espiral de Arquímedes
        r = a + b * t
        x = int(center_x + r * np.cos(t))
        y = int(center_y + r * np.sin(t))
        
        # Dibujar un círculo en la posición calculada
        cv2.circle(img, (x, y), 2, (0, 234, 0), 2)  # Color verde
        
    # Mostrar la imagen
    cv2.imshow("Arquimedes", img)
    
    # Incrementar el ángulo
    theta += theta_increment
    
    # Pausar para ver la animación
    if cv2.waitKey(30) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
        break

# Cerrar la ventana al finalizar
cv2.destroyAllWindows()
```
![Espiral de Arquímedes](Imagenes/Espiral%20de%20Arquímedes.png)  
