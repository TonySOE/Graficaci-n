import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt
import sys

camera_x, camera_y, camera_z = 10, 8, 15
look_at_x, look_at_y, look_at_z = 0, 0, 0
speed = 0.5

def init():
    """Configuración inicial de OpenGL"""
    glClearColor(0.5, 0.8, 1.0, 1.0)  # Fondo azul cielo
    glEnable(GL_DEPTH_TEST)           # Activar prueba de profundidad

    # Configuración de la perspectiva
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1, 6, 100.0)  # Campo de visión más amplio
    glMatrixMode(GL_MODELVIEW)

def draw_cube():
    """Dibuja el cubo (base de la casa)"""
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.5, 0.2)  # Marrón para todas las caras

    # Frente
    glVertex3f(-1, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 5, 1)
    glVertex3f(-1, 5, 1)

    # Atrás     X  Y   Z
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 5, -1)
    glVertex3f(-1, 5, -1)

    # Izquierda
    glVertex3f(-1, 0, -1)
    glVertex3f(-1, 0, 1)
    glVertex3f(-1, 5, 1)
    glVertex3f(-1, 5, -1)

    # Derecha
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 5, 1)
    glVertex3f(1, 5, -1)

    # Arriba
    glColor3f(0.9, 0.6, 0.3)  # Color diferente para el techo
    glVertex3f(-1, 5, -1)
    glVertex3f(1, 5, -1)
    glVertex3f(1, 5, 1)
    glVertex3f(-1, 5, 1)

    # Abajo
    glColor3f(0.6, 0.4, 0.2)  # Suelo más oscuro
    glVertex3f(-1,0 , -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(-1, 0, 1)
    glEnd()

def draw_roof():
    """Dibuja el techo (pirámide)"""
    glBegin(GL_TRIANGLES)
    glColor3f(0.9, 0.1, 0.1)  # Rojo brillante

    # Frente
    glVertex3f(-1, 5, 1)
    glVertex3f(1, 5, 1)
    glVertex3f(0, 9, 0)

    # Atrás     x  y   z 
    glVertex3f(-1, 5, -1)
    glVertex3f(1, 5, -1)
    glVertex3f(0, 9, 0)

    # Izquierda
    glVertex3f(-1, 5, -1)
    glVertex3f(-1, 5, 1)
    glVertex3f(0, 9, 0)

    # Derecha
    glVertex3f(1, 5, -1)
    glVertex3f(1, 5, 1)
    glVertex3f(0, 9, 0)
    glEnd()

def draw_ground():
    """Dibuja un plano para representar el suelo o calle"""
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.3, 0.3)  # Gris oscuro para la calle

    # Coordenadas del plano
    glVertex3f(-20, 0, 20)
    glVertex3f(20, 0, 20)
    glVertex3f(20, 0, -20)
    glVertex3f(-20, 0, -20)
    glEnd()

def draw_house():
    """Dibuja una casa (base + techo)"""
    draw_cube()  # Base de la casa
    draw_roof()  # Techos   

def key_callback(window, key, scancode, action, mods):
    """Procesa las entradas de teclado para mover la cámara"""
    global camera_x, camera_y, camera_z, speed

    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP:
            camera_y += speed  # Mover la cámara hacia arriba
        elif key == glfw.KEY_DOWN:
            camera_y -= speed  # Mover la cámara hacia abajo
        elif key == glfw.KEY_LEFT:
            camera_x -= speed  # Mover la cámara a la izquierda
        elif key == glfw.KEY_RIGHT:
            camera_x += speed  # Mover la cámara a la derecha
        elif key == glfw.KEY_W:
            camera_z -= speed  # Acercar la cámara (adelante)
        elif key == glfw.KEY_S:
            camera_z += speed  # Alejar la cámara (atrás)

def draw_scene():
    """Dibuja toda la escena con 4 casas"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    gluLookAt(camera_x, camera_y, camera_z,  # Posición de la cámara
              look_at_x, look_at_y, look_at_z,  # Punto al que mira
              0, 1, 0)  # Vector hacia arriba

    # Dibujar el suelo
    draw_ground()

    # Dibujar las casas en diferentes posiciones
    positions = [
        (-5, 0, -5),  # Casa 1
        (5, 0, -5),   # Casa 2
        (-5, 0, 5),   # Casa 3
        (5, 0, 5),
        (0, 0, 0),
        
    ]
    for pos in positions:
        glPushMatrix()
        glTranslatef(*pos)  # Mover la casa a la posición actual
        draw_house()        # Dibujar la casa
        glPopMatrix()

    glfw.swap_buffers(window)

def main():
    global window

    # Inicializar GLFW
    if not glfw.init():
        sys.exit()
    
    # Crear ventana de GLFW
    width, height = 800, 600
    window = glfw.create_window(width, height, "Escena con 4 casas", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)  # Registrar el callback de teclado
    glViewport(0, 0, width, height)
    init()

    # Bucle principal
    while not glfw.window_should_close(window):
        draw_scene()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
