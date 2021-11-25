
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def anoman1():
    glPushMatrix()
    glScale(3,3,0)
    glTranslated(50,50,0) 
    glColor3ub(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(-5,-5) 
    glVertex2f(5,-5)
    glVertex2f(5,5)
    glVertex2f(-5,5)
    glEnd()
    glPopMatrix()

def anoman2():
    glPushMatrix()
    glScale(3,3,0)
    glTranslated(50,50,0) 
    glColor3ub(45,255,155)
    glBegin(GL_QUADS)
    glVertex2f(-5,-5) 
    glVertex2f(5,-5)
    glVertex2f(5,5)
    glVertex2f(-5,5)
    glEnd()
    glPopMatrix()

def anoman3():
    glPushMatrix()
    glScale(3,3,0)
    glTranslated(50,50,0) 
    glColor3ub(155,255,15)
    glBegin(GL_QUADS)
    glVertex2f(-5,-5) 
    glVertex2f(5,-5)
    glVertex2f(5,5)
    glVertex2f(-5,5)
    glEnd()
    glPopMatrix()

def awan():
    glPushMatrix()
    glScale(4,4,0)
    glTranslated(160,130,0) 
    glTranslate(x_awan,0,0)
    glColor3ub(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(-5,-5) 
    glVertex2f(5,-5)
    glVertex2f(5,5)
    glVertex2f(-5,5)
    glEnd()
    glPopMatrix()

def anomanAnimate(value):
    global anoman_index

    if anoman_index == 2:
        anoman_index = 0
    else :
        anoman_index +=1

    glutTimerFunc(1000, anomanAnimate,0)


def timerAwan(value) :
    global x_awan
    if x_awan < -220 :
        x_awan = 0
    x_awan -= 1 
    glutTimerFunc(80,timerAwan,0)
    
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
    anomanVer[anoman_index]()
    glutSwapBuffers()


x_awan = 0
anoman_index = 0
anomanVer = (anoman1, anoman2, anoman3)


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(1280//4, 0)
wind = glutCreateWindow("The Adventure of Anoman")
timerAwan(0)
anomanAnimate(0)
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

