from sys import flags, float_repr_style
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from bg import *
import math



# def test():
#     glPushMatrix()
#     glColor3ub(0,255,25)
#     glBegin(GL_POLYGON)
#     glVertex2f(-150, -53)
#     glVertex2f(-147, -59)
#     glVertex2f(-144, -64)
#     glVertex2f(-140, -70)
#     glVertex2f(-134, -75)
#     glVertex2f(-130, -78)
#     glVertex2f(-125, -81)
#     glVertex2f(-118, -82)
#     glVertex2f(-122, -90)
#     glVertex2f(-123, -92)
#     glVertex2f(-122, -95)
#     glVertex2f(-125, -99)
#     glVertex2f(-125, -102)
#     glVertex2f(-120, -106)
#     glVertex2f(-114, -103)
#     glVertex2f(-116, -98)
#     glVertex2f(-113, -91)
#     glVertex2f(-113, -99)
#     glVertex2f(-112, -102)
#     glVertex2f(-111, -104)
#     glVertex2f(-109, -105)
#     glVertex2f(-110, -113)
#     glVertex2f(-111, -118)
#     glVertex2f(-110, -120)
#     glVertex2f(-99, -120)
#     glVertex2f(-99, -116)
#     glVertex2f(-100, -114)
#     glVertex2f(-102, -113)
#     glVertex2f(-103, -110)
#     glVertex2f(-104, -106)
#     glEnd()
#     glPopMatrix()

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


# def awan(): #Tampilan awan
#     glPushMatrix()
#     glScale(3.5,3.5,0)
#     glTranslated(10,60,0) 
#     glTranslate(0,0,0)
#     glColor3ub(255,255,255)
#     glBegin(GL_QUADS)
#     glVertex2f(-7,-5) 
#     glVertex2f(7,-5)
#     glVertex2f(7,5)
#     glVertex2f(-7,5)
#     glEnd()
#     glPopMatrix()

def awan_1 ():
    glPushMatrix()
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(185, 210) #J
    glVertex2f(182, 214) #I
    glVertex2f(183, 218) #H
    glVertex2f(185, 221) #G
    glVertex2f(190, 224) #F
    glVertex2f(194, 223) #E 
    glVertex2f(196, 226) #D
    glVertex2f(200, 228) #C
    glVertex2f(205, 228) #B
    glVertex2f(208, 232) #A 
    glVertex2f(213, 234) #Z
    glVertex2f(218, 234) #W
    glVertex2f(223, 232) #V
    glVertex2f(227, 229) #U
    glVertex2f(229, 225) #T
    glVertex2f(234, 226) #S
    glVertex2f(238, 223) #R
    glVertex2f(240, 220) #Q
    glVertex2f(241, 216) #P
    glVertex2f(238, 210) #O
    glVertex2f(233, 208) #N
    glVertex2f(211, 208) #K
    glVertex2f(189, 208) #M
    glEnd()
    glPopMatrix()


def awan_2 ():
    glPushMatrix()
    glTranslated(-160,10,0) 
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(185, 210) #J
    glVertex2f(182, 214) #I
    glVertex2f(183, 218) #H
    glVertex2f(185, 221) #G
    glVertex2f(190, 224) #F
    glVertex2f(194, 223) #E 
    glVertex2f(196, 226) #D
    glVertex2f(200, 228) #C
    glVertex2f(205, 228) #B
    glVertex2f(208, 232) #A 
    glVertex2f(213, 234) #Z
    glVertex2f(218, 234) #W
    glVertex2f(223, 232) #V
    glVertex2f(227, 229) #U
    glVertex2f(229, 225) #T
    glVertex2f(234, 226) #S
    glVertex2f(238, 223) #R
    glVertex2f(240, 220) #Q
    glVertex2f(241, 216) #P
    glVertex2f(238, 210) #O
    glVertex2f(233, 208) #N
    glVertex2f(211, 208) #K
    glVertex2f(189, 208) #M
    glEnd()
    glPopMatrix()

def awan_3 ():
    glPushMatrix()
    glTranslated(-310,0,0) 
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(185, 210) #J
    glVertex2f(182, 214) #I
    glVertex2f(183, 218) #H
    glVertex2f(185, 221) #G
    glVertex2f(190, 224) #F
    glVertex2f(194, 223) #E 
    glVertex2f(196, 226) #D
    glVertex2f(200, 228) #C
    glVertex2f(205, 228) #B
    glVertex2f(208, 232) #A 
    glVertex2f(213, 234) #Z
    glVertex2f(218, 234) #W
    glVertex2f(223, 232) #V
    glVertex2f(227, 229) #U
    glVertex2f(229, 225) #T
    glVertex2f(234, 226) #S
    glVertex2f(238, 223) #R
    glVertex2f(240, 220) #Q
    glVertex2f(241, 216) #P
    glVertex2f(238, 210) #O
    glVertex2f(233, 208) #N
    glVertex2f(211, 208) #K
    glVertex2f(189, 208) #M
    glEnd()
    glPopMatrix()

def awan_4 ():
    glPushMatrix()
    glTranslated(-430,30,0) 
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(185, 210) #J
    glVertex2f(182, 214) #I
    glVertex2f(183, 218) #H
    glVertex2f(185, 221) #G
    glVertex2f(190, 224) #F
    glVertex2f(194, 223) #E 
    glVertex2f(196, 226) #D
    glVertex2f(200, 228) #C
    glVertex2f(205, 228) #B
    glVertex2f(208, 232) #A 
    glVertex2f(213, 234) #Z
    glVertex2f(218, 234) #W
    glVertex2f(223, 232) #V
    glVertex2f(227, 229) #U
    glVertex2f(229, 225) #T
    glVertex2f(234, 226) #S
    glVertex2f(238, 223) #R
    glVertex2f(240, 220) #Q
    glVertex2f(241, 216) #P
    glVertex2f(238, 210) #O
    glVertex2f(233, 208) #N
    glVertex2f(211, 208) #K
    glVertex2f(189, 208) #M
    glEnd()
    glPopMatrix()