
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def kotak():
    glScale(0.5,0.5,0.5)
    glBegin(GL_QUADS)
    glVertex2f(-5,-5)
    glVertex2f(5,-5)
    glVertex2f(5,5)
    glVertex2f(-5,5)
    glEnd()
    
def iterate():
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 30, 0.0, 30, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(2, 0.3, 2)
    kotak()    
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(1280//4, 0)
wind = glutCreateWindow("The Adventure of Anoman")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

