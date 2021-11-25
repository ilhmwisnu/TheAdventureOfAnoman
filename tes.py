

from sys import flags
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def anoman1():
    glPushMatrix()
    glScale(3,3,0)
    glTranslated(50,50,0) 
    glTranslated(0,jump_height,0) 
    glColor3ub(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(-5,-5) 
    glVertex2f(5,-5)
    glVertex2f(5,5)
    glVertex2f(-5,5)
    glEnd()
    glPopMatrix()


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
    anoman1()
    glutSwapBuffers()

# def jump(key,x,y) : 
#     global jump_height
#     if key == GLUT_KEY_UP :
#         # glTranslated(0,20,0)
#         # anoman1()
#         jump_height += 10

def jump(key,x,y) : 
    global isJumping    
    if key == GLUT_KEY_UP and isJumping is not True :
        isJumping = True
        jump_timer(0)
    if key == GLUT_KEY_UP and isJumping is True :
        pass

def jump_timer(value) :
    global jump_height
    if jump_height < 50  :
        jump_height += 1
    else : 
        return down_timer(0)
    glutTimerFunc(15,jump_timer,0)

def down_timer(value) :
    global isJumping
    global jump_height
    if jump_height != 0  :
        jump_height -= 1
    else : 
        isJumping = False
        return 
    glutTimerFunc(15,down_timer,0)

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

jump_height = 0
isJumping = False

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(1280//4, 0)
wind = glutCreateWindow("The Adventure of Anoman")
glutDisplayFunc(showScreen)

# if isJump :
#     jump_timer(0)
glutIdleFunc(showScreen)
glutSpecialFunc(jump)
# glutTimerFunc(10,update,0)
glutMainLoop()

