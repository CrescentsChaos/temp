import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

points = [] 
speeds = 0.01 
frozen = False 
blinking = False  
boundary = 1.0  

class Point:
    def __init__(self, x, y, color, direction):
        self.x = x
        self.y = y
        self.color = color
        self.direction = direction  
        self.blink = False
        self.visible = True

    def move(self):
        if not frozen:
            self.x += self.direction[0] * speeds
            self.y += self.direction[1] * speeds
            if self.x > boundary or self.x < -boundary:
                self.direction = (-self.direction[0], self.direction[1])
            if self.y > boundary or self.y < -boundary:
                self.direction = (self.direction[0], -self.direction[1])

    def toggle_visibility(self):
        self.visible = not self.visible

    def draw(self):
        if self.visible:
            glColor3fv(self.color)
            glBegin(GL_POINTS)
            glVertex2f(self.x, self.y)
            glEnd()

def random_color():
    return random.random(), random.random(), random.random()

def random_direction():
    dx = random.choice([-1, 1])
    dy = random.choice([-1, 1])
    return dx, dy

def right_click(x, y):
    nx = (x - 400) / 400
    ny = (300 - y) / 300
    point = Point(nx, ny, random_color(), random_direction())
    points.append(point)

def update_points(value):
    global blinking

    if not frozen:
        for point in points:
            point.move()

    if blinking:
        for point in points:
            point.toggle_visibility()

    glutPostRedisplay()
    glutTimerFunc(100, update_points, 0)

def keyboard(key, x, y):
    global speeds, frozen, blinking
    if key == b'\x1b':  
        glutLeaveMainLoop()
    elif key == b' ': 
        frozen = not frozen
    elif key == GLUT_KEY_UP and not frozen: 
        speeds += 0.01
    elif key == GLUT_KEY_DOWN and not frozen and speeds > 0.01: 
        speeds -= 0.01

def mouse(button, state, x, y):
    global blinking
    if state == GLUT_DOWN:
        if button == GLUT_RIGHT_BUTTON: 
            right_click(x, y)
        elif button == GLUT_LEFT_BUTTON: 
            blinking = not blinking

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.0, 0.0, 0.0, 1.0)  

    for point in points:
        point.draw()

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Amazing Box")

    glPointSize(10.0) 
    glLoadIdentity()

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(keyboard)
    glutMouseFunc(mouse)
    glutTimerFunc(100, update_points, 0)

    glutMainLoop()

if __name__ == "__main__":
    main()
