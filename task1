import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

background_color = 0.0
rain_direction = 0.0
raindrops = [{"x": random.uniform(-1.0, 1.0), "y": random.uniform(-1.0, 1.0)} for _ in range(100)]  # Initial raindrops

def draw_house():
    #roof
    glColor3f(1, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, 0.2)
    glVertex2f(0.5, 0.2)
    glVertex2f(0.0, 0.8)
    glEnd()
    #wall
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.2)
    glVertex2f(-0.5, 0.2)
    glEnd()
    #window
    glColor3f(0.1, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(-0.25, -0.25)
    glVertex2f(0.25, -0.25)
    glVertex2f(0.25, 0.1)
    glVertex2f(-0.25, 0.1)
    glEnd()
    #window pieces
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex2f(-0.24, -0.24)
    glVertex2f(0, 0)
    glVertex2f(0, 0)
    glVertex2f(0.24, -0.24)
    glEnd()
    
def draw_rain():
    glColor3f(0.0, 0.0, 1.0) 
    glBegin(GL_POINTS)
    for drop in raindrops:
        glVertex2f(drop["x"], drop["y"])
    glEnd()

def update_rain():
    global raindrops
    for drop in raindrops:
        drop["y"] -= 0.01 
        drop["x"] += rain_direction * 0.002
        if drop["y"] < -1.0:
            drop["y"] = 1.0
            drop["x"] = random.uniform(-1.0, 1.0)

    glutPostRedisplay()

def change_background_color(direction):
    global background_color
    if direction == 1: 
        background_color = min(1.0, background_color + 0.01)
    elif direction == -1: 
        background_color = max(0.0, background_color - 0.01)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(background_color, background_color, background_color, 1.0)

    draw_house()
    draw_rain()

    glutSwapBuffers()

def keyboard(key, x, y):
    global rain_direction
    if key == b'\x1b': 
        glutLeaveMainLoop()
    elif key == b'd': 
        change_background_color(1)
    elif key == b'n': 
        change_background_color(-1)
    elif key == GLUT_KEY_LEFT:
        rain_direction -= 0.05
    elif key == GLUT_KEY_RIGHT: 
        rain_direction += 0.05

def timer(value):
    update_rain()
    glutTimerFunc(16, timer, 0) 

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"House in Rainfall")

    glPointSize(7.0) 
    glLoadIdentity()

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(keyboard)
    glutTimerFunc(16, timer, 0) 

    glutMainLoop()

if __name__ == "__main__":
    main()
