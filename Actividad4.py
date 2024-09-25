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
    cv2.imshow("Parametric Animation", img)
    
    # Incrementar el ángulo
    theta += theta_increment
    
    # Pausar para ver la animación
    if cv2.waitKey(30) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
        break

# Cerrar la ventana al finalizar
cv2.destroyAllWindows()
