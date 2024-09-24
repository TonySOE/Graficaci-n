import numpy as np
import cv2

# Función para generar un solo punto de la elipse en función del parámetro t
def generar_punto_elipse(a, b, t, desplazamiento_x, desplazamiento_y):
    x = int(a * np.cos(t) + desplazamiento_x)  # Desplazamiento para centrar
    y = int(b * np.sin(t) + desplazamiento_y)
    return (x, y)

# Dimensiones de la imagen
img_width, img_height = 1000, 900

# Crear una imagen en blanco
imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)

# Parámetros de las elipses (semieje mayor, semieje menor, desplazamiento en x, desplazamiento en y)
elipses = [
    (0, 0, 500, 450),      # Elipse 1 (centro)
    (150, 100, 500, 450),  # Elipse 2 (intercambiados)
    (200, 150, 500, 450),  # Elipse 3 (intercambiados)
    (250, 200, 500, 450),  # Elipse 4 (intercambiados)
    (300, 250, 500, 450),  # Elipse 5 (intercambiados)
    (350, 300, 500, 450),  # Elipse 6 (intercambiados)
    (400, 350, 500, 450),  # Elipse 7 (intercambiados)
    (450, 400, 500, 450),  # Elipse 8 (intercambiados)
    (500, 450, 500, 450)   # Elipse 9 (intercambiados)
]

# Definir los colores para cada círculo (en formato BGR)
colores = [
    (0, 255, 255),   # Amarillo para el centro (Elipse 1)
    (42, 42, 165),   # Café para Elipse 2
    (0, 0, 255),     # Rojo para Elipse 3
    (0, 255, 0),     # Verde para Elipse 4
    (42, 42, 165),   # Café para Elipse 5
    (200, 190, 140), # Café claro para Elipse 6
    (200, 190, 140), # Café claro para Elipse 7
    (255, 0, 0),     # Azul para Elipse 8
    (255, 0, 0)      # Azul para Elipse 9
]

# Tamaños de los círculos
tamanos = [
    40,  # Grande para el círculo amarillo (centro)
    10,  # Pequeño para Elipse 2
    17,  # Mediano para Elipse 3
    18,  # Mediano para Elipse 4
    12,  # Mediano para Elipse 5
    25,  # Grande para Elipse 6
    23,  # Grande para Elipse 7
    18,  # Mediano para Elipse 8
    17   # Mediano para Elipse 9
]

num_puntos = 1000

# Crear los valores del parámetro t para la animación
t_vals = np.linspace(0, 2 * np.pi, num_puntos)

# Bucle de animación
for t in t_vals:
    # Crear una nueva imagen en blanco en cada iteración
    imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)

    # Dibujar las trayectorias de todas las elipses (opcional, si quieres verlas completas)
    for a, b, despl_x, despl_y in elipses:
        for t_tray in t_vals:
            pt_tray = generar_punto_elipse(a, b, t_tray, despl_x, despl_y)
            cv2.circle(imagen, pt_tray, radius=1, color=(255, 255, 255), thickness=-1)

    # Dibujar el punto en movimiento para cada elipse con su color
    for i, (a, b, despl_x, despl_y) in enumerate(elipses):
        punto = generar_punto_elipse(a, b, t, despl_x, despl_y)
        cv2.circle(imagen, punto, radius=tamanos[i], color=colores[i], thickness=-1)

    # Mostrar la imagen con los puntos en movimiento
    cv2.imshow('img', imagen)

    # Controlar la velocidad de la animación (en milisegundos)
    cv2.waitKey(10)

# Cerrar la ventana después de la animación
cv2.destroyAllWindows()