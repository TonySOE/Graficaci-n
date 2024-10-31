import cv2
import numpy as np

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 800

# Dimensiones del prisma (largo, ancho, alto)
LARGO = 1.5
ANCHO = 1.0
ALTO = 2.0

# Vértices del prisma en coordenadas 3D (diferentes dimensiones para formar un prisma)
vertices = np.array([
    [-LARGO, -ANCHO, -ALTO],
    [LARGO, -ANCHO, -ALTO],
    [LARGO, ANCHO, -ALTO],
    [-LARGO, ANCHO, -ALTO],
    [-LARGO, -ANCHO, ALTO],
    [LARGO, -ANCHO, ALTO],
    [LARGO, ANCHO, ALTO],
    [-LARGO, ANCHO, ALTO]
])

# Conexiones de los vértices para formar las aristas del prisma
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Base inferior        
    (4, 5), (5, 6), (6, 7), (7, 4),  # Base superior
    (0, 4), (1, 5), (2, 6), (3, 7)   # Conexiones entre bases
]

def project_isometric(vertex):
    """Función para proyectar un punto 3D a 2D con proyección isométrica"""
    x, y, z = vertex
    x2D = x - z
    y2D = (x + 2 * y + z) / 2
    return int(x2D * 100 + WIDTH / 2), int(-y2D * 100 + HEIGHT / 2)

# Crear ventana
cv2.namedWindow("Prisma Rectangular Isométrico")

while True:
    # Crear imagen negra para el fondo
    frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    # Dibujar aristas del prisma
    for edge in edges:
        pt1 = project_isometric(vertices[edge[0]])
        pt2 = project_isometric(vertices[edge[1]])
        cv2.line(frame, pt1, pt2, (255, 255, 255), 2)

    # Mostrar imagen
    cv2.imshow("Prisma Rectangular Isométrico", frame)

    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
