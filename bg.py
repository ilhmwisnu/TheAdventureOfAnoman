from sys import flags, float_repr_style
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from bg import *
import math

def background():
    glPushMatrix()
    glColor3ub(135, 206, 235)
    glBegin(GL_POLYGON)
    glVertex2f(-300,300) 
    glVertex2f(300, 300)
    glVertex2f(300,-300)
    glVertex2f(-300,-300)
    glEnd()
    glPopMatrix()

def gunung1():
    glPushMatrix()
    glColor3ub(140, 170, 220)
    glBegin(GL_POLYGON)
    glVertex2f(-59, 30)
    glVertex2f(120, 100)
    glVertex2f(300,-10)
    glVertex2f(300,-50)
    glVertex2f(-300,-50)
    glVertex2f(-300,100) 
    glEnd()
    glPopMatrix()

def gunung2():
    glPushMatrix()
    glColor3ub(95, 140, 200)
    glBegin(GL_POLYGON)
    glVertex2f(200, 10)
    glVertex2f(300, 50)
    glVertex2f(300, -50)
    glVertex2f(-300,-50)
    glVertex2f(-300, 20) 
    glVertex2f(-80, 70)
    glEnd()
    glPopMatrix()

def tanah(): #Tampilan tanah
    glPushMatrix()
    glColor3ub(161, 89, 2)
    glBegin(GL_QUADS)
    glVertex2f(-300,-300) 
    glVertex2f(300,-300)
    glVertex2f(300,-50)
    glVertex2f(-300,-50)
    glEnd()
    glPopMatrix()


def rumput(): #Tampilan tanah
    glPushMatrix()
    glColor3ub(0, 191, 0)
    glBegin(GL_QUADS)
    glVertex2f(-300,-80) 
    glVertex2f(300,-80)
    glVertex2f(300,-50)
    glVertex2f(-300,-50)
    glEnd()
    glPopMatrix()


def matahari():
    posx, posy = 0,0    
    sides = 32    
    radius = 25   
    glPushMatrix()
    glTranslated(30,250,0) 
    glColor3ub(249, 215, 28)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()