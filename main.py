
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

x_awan = 0.0


def awan():
    glScale(3,3,0)
    glTranslated(210,170,0) 
    glTranslate(x_awan,0,0)
    glBegin(GL_QUADS)
    glVertex2f(-5,-5) 
    glVertex2f(5,-5)
    glVertex2f(5,5)
    glVertex2f(-5,5)
    glEnd()

def timerAwan(value) :
    global x_awan
    if x_awan < -220 :
        x_awan = 0
    x_awan -= 1 
    glutTimerFunc(100,timerAwan,0)
    
def iterate():
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    awan()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(1280//4, 0)
wind = glutCreateWindow("The Adventure of Anoman")
timerAwan(0)
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

