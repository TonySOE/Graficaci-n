import numpy as np
import cv2 as cv

def inicializar_lienzo(ancho, alto):
    """Crea un lienzo blanco y devuelve sus parámetros iniciales."""
    lienzo = np.ones((alto, ancho, 3), dtype=np.uint8) * 255
    centro = np.array([ancho // 3, alto // 4], dtype=np.float32)
    tamanio = 100
    angulo = 0
    return lienzo, centro, tamanio, angulo

def definir_puntos_iniciales(centro):
    """Define los puntos iniciales del triángulo en relación al centro."""
    return np.array([
        [centro[0] - 200, centro[1]],
        [centro[0], centro[1]],
        [centro[0] + 200, centro[1]]
    ], dtype=np.float32)

def dibujar_triangulo(lienzo, centro, tamanio, angulo):
    """Dibuja un triángulo equilátero en el lienzo."""
    mitad_tamanio = tamanio // 2
    altura = int(np.sqrt(tamanio**2 - mitad_tamanio**2))
    puntos = np.array([
        [-mitad_tamanio, altura // 2],
        [mitad_tamanio, altura // 2],
        [0, -altura // 2]
    ], dtype=np.float32)

    matriz_rotacion = cv.getRotationMatrix2D((0, 0), angulo, 1)
    puntos_rotados = np.dot(puntos, matriz_rotacion[:, :2].T)
    puntos_trasladados = puntos_rotados + centro
    puntos_trasladados = puntos_trasladados.astype(int)

    cv.fillPoly(lienzo, [puntos_trasladados], color=(0, 255, 0))

def configurar_camara():
    """Configura la cámara y devuelve el primer cuadro en escala de grises."""
    camara = cv.VideoCapture(0)
    _, cuadro_inicial = camara.read()
    gris_inicial = cv.cvtColor(cuadro_inicial, cv.COLOR_BGR2GRAY)
    return camara, gris_inicial

def ajustar_parametros_opticos():
    """Devuelve los parámetros para el cálculo del flujo óptico."""
    return dict(winSize=(15, 15), maxLevel=2,
                criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

def procesar_movimiento(puntos_actuales, puntos_seguimiento, puntos_iniciales, centro, tamanio, angulo, parametros):
    """Actualiza las propiedades del triángulo según el movimiento detectado."""
    umbral_seguimiento, umbral_reset, umbral_movimiento, paso_escala, paso_rotacion = parametros
    multiplicar = 1.5
    for i, (nuevo, viejo) in enumerate(zip(puntos_actuales, puntos_seguimiento)):
        a, b = (int(x) for x in nuevo.ravel())
        c, d = (int(x) for x in viejo.ravel())
        distancia_origen = np.linalg.norm(nuevo.ravel() - puntos_iniciales[i])
        distancia_movimiento = np.linalg.norm(nuevo.ravel() - viejo.ravel())

        if distancia_movimiento >= umbral_movimiento and distancia_origen <= umbral_seguimiento:
            if i == 0:  # Escalar
                tamanio += (paso_escala * multiplicar) if nuevo.ravel()[0] < viejo.ravel()[0] else -paso_escala
                tamanio = max(paso_escala, tamanio)
            elif i == 1:  # Mover
                centro += (nuevo.ravel() - viejo.ravel()) * 0.5
            elif i == 2:  # Rotar
                angulo += (paso_rotacion * multiplicar) if nuevo.ravel()[0] > viejo.ravel()[0] else -paso_rotacion

        if distancia_origen > umbral_reset:
            puntos_seguimiento[i] = puntos_iniciales[i]
    return centro, tamanio, angulo

# Configuración inicial
ancho, alto = 1000, 1000
lienzo, centro, tamanio, angulo = inicializar_lienzo(ancho, alto)
puntos_iniciales = definir_puntos_iniciales(centro)
camara, gris_inicial = configurar_camara()
parametros_opticos = ajustar_parametros_opticos()
puntos_seguimiento = puntos_iniciales[:, np.newaxis, :]
parametros_control = (150, 200, 5, 2, 1)

while True:
    lienzo[:] = 255
    _, cuadro_actual = camara.read()
    
    cuadro_actual = cv.flip(cuadro_actual, 1)

    gris_actual = cv.cvtColor(cuadro_actual, cv.COLOR_BGR2GRAY)

    for px, py in puntos_iniciales:
        cuadro_actual = cv.circle(cuadro_actual, (int(px), int(py)), 5, (0, 0, 0), -1)

    puntos_actuales, estado, error = cv.calcOpticalFlowPyrLK(
        gris_inicial, gris_actual, puntos_seguimiento, None, **parametros_opticos
    )

    if puntos_actuales is not None and estado is not None:
        centro, tamanio, angulo = procesar_movimiento(
            puntos_actuales, puntos_seguimiento, puntos_iniciales, centro, tamanio, angulo, parametros_control
        )
        for i, (nuevo, viejo) in enumerate(zip(puntos_actuales, puntos_seguimiento)):
            a, b = (int(x) for x in nuevo.ravel())
            c, d = (int(x) for x in viejo.ravel())
            cuadro_actual = cv.circle(cuadro_actual, (a, b), 3, (0, 0, 255), -1)
            cuadro_actual = cv.line(cuadro_actual, (c, d), (a, b), (0, 0, 0), 2)

    dibujar_triangulo(lienzo, centro, tamanio, angulo)

    cv.imshow("Camara", cuadro_actual)
    cv.imshow("Triángulo", lienzo)

    gris_inicial = gris_actual.copy()

    if cv.waitKey(1) & 0xFF == 27:
        break

camara.release()
cv.destroyAllWindows()
