from sys import flags, float_repr_style
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GLUT.freeglut import *
from bg import *
import math


print("spasi => mulai")
print("'s' => stop")



"""Code gambar Karakter - Start"""

def batu():
    glPushMatrix()
    glColor3ub(64,64,64)
    glTranslated(deltaX - 35,0,0)
    # glTranslated(-60, 100,0)
    glBegin(GL_POLYGON)
    glVertex2f(310, -50)
    glVertex2f(311, -48)
    glVertex2f(311, -43)
    glVertex2f(311, -42)
    glVertex2f(313, -38) #S
    glVertex2f(313, -36)
    glVertex2f(314, -32) #U
    glVertex2f(314, -30)
    glVertex2f(315, -27)
    glVertex2f(314, -23)
    glVertex2f(315, -18)
    glVertex2f(314, -15)
    glVertex2f(316, -13)
    glVertex2f(317, -12)
    glVertex2f(319, -10)
    glVertex2f(325, -10)
    glVertex2f(327, -9)
    glVertex2f(333, -10)
    glVertex2f(338, -14)
    glVertex2f(340, -20)
    glVertex2f(339, -24)
    glVertex2f(341, -26)
    glVertex2f(340, -30)
    glVertex2f(342, -35)
    glVertex2f(344, -36)
    glVertex2f(344, -39)
    glVertex2f(346, -41)
    glVertex2f(347, -47)
    glVertex2f(343, -50)
    glEnd()
    glPopMatrix()

def batuGrad():
    glPushMatrix()
    glColor3ub(170,170,170)
    glTranslated(deltaX - 35,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(319, -10)
    glVertex2f(325, -10)
    glVertex2f(327, -9)
    glVertex2f(333, -10)
    glVertex2f(338, -14)
    glVertex2f(340, -20)
    glVertex2f(339, -24)
    glVertex2f(341, -26)
    glVertex2f(340, -30)
    glVertex2f(342, -35)
    glVertex2f(344, -36)
    glVertex2f(344, -39)
    glVertex2f(346, -41)
    glVertex2f(347, -47)
    glVertex2f(343, -50)
    glVertex2f(334, -50)
    glVertex2f(332, -46)
    glVertex2f(333, -42)
    glVertex2f(332, -39)
    glVertex2f(328, -40)
    glVertex2f(329, -36)
    glVertex2f(327, -35)
    glVertex2f(329, -31)
    glVertex2f(330, -27)
    glVertex2f(327, -25)
    glVertex2f(330, -21) 
    glVertex2f(327, -18)
    glVertex2f(327, -14)
    glVertex2f(322, -14)
    glEnd()
    glPopMatrix()


def awan_1 ():
    glPushMatrix()
    glColor3ub(255, 255, 255)
    glTranslated(deltaX_awan,0,0) 
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
    glTranslated(deltaX_awan,0,0) 
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
    glTranslated(deltaX_awan,0,0) 
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
    glTranslated(deltaX_awan,0,0) 
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



def anoman1():
    #muka1
    glPushMatrix()
    glColor3ub(255,255,255)
    glTranslated(10,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-160, 10)
    glVertex2f(-140, 11)
    glVertex2f(-131, 10)
    glVertex2f(-123, 4)
    glVertex2f(-120, -1)
    glVertex2f(-120, -7)
    glVertex2f(-124, -16)
    glVertex2f(-123, -19)
    glVertex2f(-125, -22)
    glVertex2f(-135, -26)
    glVertex2f(-143, -26)
    glVertex2f(-147, -24)
    glVertex2f(-149, -22)
    glVertex2f(-152, -21)
    glVertex2f(-156, -18)
    glVertex2f(-156, -14)
    glVertex2f(-158, -9)
    glVertex2f(-158, 1)
    glVertex2f(-160, 6)
    glVertex2f(-158, 5)
    glEnd()
    glPopMatrix()

    #Muka2
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(10,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-141, -2)
    glVertex2f(-136, -3)
    glVertex2f(-130, -8)
    glVertex2f(-128, -4)
    glVertex2f(-124, -3)
    glVertex2f(-122, -7)
    glVertex2f(-124, -14)
    glVertex2f(-126, -16)
    glVertex2f(-124, -18)
    glVertex2f(-125, -21)
    glVertex2f(-127, -23)
    glVertex2f(-135, -25)
    glVertex2f(-140, -25)
    glVertex2f(-144, -22)
    glVertex2f(-145, -19)
    glVertex2f(-143, -17)
    glVertex2f(-146, -14)
    glVertex2f(-147, -8)
    glVertex2f(-144, -4)
    glEnd()
    glPopMatrix()

    #Telinga
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(10,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-154, -13)
    glVertex2f(-151, -12)
    glVertex2f(-149, -13)
    glVertex2f(-148, -20)
    glVertex2f(-150, -21)
    glVertex2f(-154, -20)
    glVertex2f(-156, -17)
    glEnd()
    glPopMatrix()

    #mata1a
    posx, posy = 0,0    
    sides = 32    
    radius = 4   
    glPushMatrix()
    glTranslated(-125,jump_height,0) 
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

    #mata2a
    posx, posy = 0,0    
    sides = 32    
    radius = 2  
    glPushMatrix()
    glTranslated(-125,jump_height,0) 
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

    #mata1b
    posx, posy = 0,0    
    sides = 32    
    radius = 3   
    glPushMatrix()
    glTranslated(-117,jump_height,0) 
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

    #mata2b
    posx, posy = 0,0    
    sides = 32    
    radius = 1  
    glPushMatrix()
    glTranslated(-117,jump_height,0) 
    glColor3ub(0, 0, 28)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

    #badan
    glPushMatrix()
    glColor3ub(250,250,250)
    glTranslated(10,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-143, -25)
    glVertex2f(-139, -26)
    glVertex2f(-140, -26)
    glVertex2f(-134, -29)
    glVertex2f(-133, -33)
    glVertex2f(-133, -37)
    glVertex2f(-136, -44)
    glVertex2f(-135, -47)
    glVertex2f(-136, -50)
    glVertex2f(-138, -53)
    glVertex2f(-135, -55)
    glVertex2f(-134, -57)
    glVertex2f(-136, -59)
    glVertex2f(-140, -60)
    glVertex2f(-146, -58)
    glVertex2f(-147, -56)
    glVertex2f(-144, -51)
    glVertex2f(-146, -49)
    glVertex2f(-151, -46)
    glVertex2f(-155, -43)
    glVertex2f(-156, -40)
    glEnd()
    glPopMatrix()

    #kaki
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(10,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-153, -44)
    glVertex2f(-151, -46)
    glVertex2f(-145, -49)
    glVertex2f(-144, -51)
    glVertex2f(-146, -52)
    glVertex2f(-149, -53)
    glVertex2f(-152, -52)
    glVertex2f(-150, -55)
    glVertex2f(-153, -57) #F
    glVertex2f(-156, -55)
    glVertex2f(-159, -51)
    glVertex2f(-158, -48)
    glVertex2f(-157, -46)
    glEnd()
    glPopMatrix()
    
    #tangan
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(10,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-133, -35)
    glVertex2f(-130, -37)
    glVertex2f(-129, -38)
    glVertex2f(-129, -40)
    glVertex2f(-131, -42)
    glVertex2f(-133, -43)
    glVertex2f(-135, -42)
    glVertex2f(-134, -41)
    glVertex2f(-133, -37)
    glEnd()
    glPopMatrix()

    #tangan depan
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(10,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-149, -27)
    glVertex2f(-145, -26)
    glVertex2f(-140, -28)
    glVertex2f(-139, -31)
    glVertex2f(-141, -32)
    glVertex2f(-146, -34)
    glVertex2f(-148, -35)
    glVertex2f(-151, -39)
    glVertex2f(-153, -40)
    glVertex2f(-156, -40)
    glVertex2f(-158, -40)
    glVertex2f(-157, -33)
    glVertex2f(-154, -29)
    glEnd()
    glPopMatrix()

    #ekor
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(10,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-165, -34)
    glVertex2f(-160, -38)
    glVertex2f(-155, -41)
    glVertex2f(-155, -43)
    glVertex2f(-162, -41)
    glVertex2f(-168, -36)
    glEnd()
    glPopMatrix()


def anoman2():
    #muka1
    glPushMatrix()
    glColor3ub(255,255,255)
    glTranslated(15,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-160, 10)
    glVertex2f(-140, 11)
    glVertex2f(-131, 10)
    glVertex2f(-123, 4)
    glVertex2f(-120, -1)
    glVertex2f(-120, -7)
    glVertex2f(-124, -16)
    glVertex2f(-123, -19)
    glVertex2f(-125, -22)
    glVertex2f(-135, -26)
    glVertex2f(-143, -26)
    glVertex2f(-147, -24)
    glVertex2f(-149, -22)
    glVertex2f(-152, -21)
    glVertex2f(-156, -18)
    glVertex2f(-156, -14)
    glVertex2f(-158, -9)
    glVertex2f(-158, 1)
    glVertex2f(-160, 6)
    glVertex2f(-158, 5)
    glEnd()
    glPopMatrix()

    #Muka2
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(15,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-141, -2)
    glVertex2f(-136, -3)
    glVertex2f(-130, -8)
    glVertex2f(-128, -4)
    glVertex2f(-124, -3)
    glVertex2f(-122, -7)
    glVertex2f(-124, -14)
    glVertex2f(-126, -16)
    glVertex2f(-124, -18)
    glVertex2f(-125, -21)
    glVertex2f(-127, -23)
    glVertex2f(-135, -25)
    glVertex2f(-140, -25)
    glVertex2f(-144, -22)
    glVertex2f(-145, -19)
    glVertex2f(-143, -17)
    glVertex2f(-146, -14)
    glVertex2f(-147, -8)
    glVertex2f(-144, -4)
    glEnd()
    glPopMatrix()

    #Telinga
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(15,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-154, -13)
    glVertex2f(-151, -12)
    glVertex2f(-149, -13)
    glVertex2f(-148, -20)
    glVertex2f(-150, -21)
    glVertex2f(-154, -20)
    glVertex2f(-156, -17)
    glEnd()
    glPopMatrix()

    #mata1a
    posx, posy = 0,0    
    sides = 32    
    radius = 4   
    glPushMatrix()
    glTranslated(-120,jump_height,0) 
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

    #mata2a
    posx, posy = 0,0    
    sides = 32    
    radius = 2  
    glPushMatrix()
    glTranslated(-120,jump_height,0) 
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

    #mata1b
    posx, posy = 0,0    
    sides = 32    
    radius = 3   
    glPushMatrix()
    glTranslated(-112,jump_height,0) 
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

    #mata2b
    posx, posy = 0,0    
    sides = 32    
    radius = 1  
    glPushMatrix()
    glTranslated(-112,jump_height,0) 
    glColor3ub(0, 0, 28)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()


    #badan
    glPushMatrix()
    glColor3ub(250,250,250)
    glTranslated(-15,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-109, -26)
    glVertex2f(-103, -26)
    glVertex2f(-100, -31)
    glVertex2f(-101, -38)
    glVertex2f(-103, -42)
    glVertex2f(-104, -44)
    glVertex2f(-109, -48)
    glVertex2f(-111, -52)
    glVertex2f(-115, -55)
    glVertex2f(-113, -56)
    glVertex2f(-113, -58)
    glVertex2f(-120, -60)
    glVertex2f(-124, -58)
    glVertex2f(-125, -54)
    glVertex2f(-119, -49)
    glVertex2f(-123, -45)
    glVertex2f(-124, -39)
    glVertex2f(-123, -36)
    glEnd()
    glPopMatrix()

    #tangan
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(-15,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-118, -28)
    glVertex2f(-113, -26)
    glVertex2f(-107, -28)
    glVertex2f(-108, -30)
    glVertex2f(-113, -33)
    glVertex2f(-115, -35)
    glVertex2f(-110, -35)
    glVertex2f(-108, -37)
    glVertex2f(-114, -43)
    glVertex2f(-120, -41)
    glVertex2f(-122, -32)
    glVertex2f(-123, -37)
    glEnd()
    glPopMatrix()
    
    #KAKI
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(-15,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-109, -42)
    glVertex2f(-101, -44)
    glVertex2f(-101, -47)
    glVertex2f(-103, -50)
    glVertex2f(-101, -51)
    glVertex2f(-100, -53)
    glVertex2f(-102, -55)
    glVertex2f(-105, -56)
    glVertex2f(-107, -55)
    glVertex2f(-112, -53)
    glVertex2f(-110, -49)
    glVertex2f(-109, -48)
    glVertex2f(-104, -44)
    glEnd()
    glPopMatrix()

    #ekor
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(20,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-165, -34)
    glVertex2f(-160, -38)
    glVertex2f(-155, -41)
    glVertex2f(-155, -43)
    glVertex2f(-162, -41)
    glVertex2f(-168, -36)
    glEnd()
    glPopMatrix()


def anoman3():
    #muka1
    glPushMatrix()
    glColor3ub(255,255,255)
    glTranslated(25,8+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-160, 10)
    glVertex2f(-140, 11)
    glVertex2f(-131, 10)
    glVertex2f(-123, 4)
    glVertex2f(-120, -1)
    glVertex2f(-120, -7)
    glVertex2f(-124, -16)
    glVertex2f(-123, -19)
    glVertex2f(-125, -22)
    glVertex2f(-135, -26)
    glVertex2f(-143, -26)
    glVertex2f(-147, -24)
    glVertex2f(-149, -22)
    glVertex2f(-152, -21)
    glVertex2f(-156, -18)
    glVertex2f(-156, -14)
    glVertex2f(-158, -9)
    glVertex2f(-158, 1)
    glVertex2f(-160, 6)
    glVertex2f(-158, 5)
    glEnd()
    glPopMatrix()

    #Muka2
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(25,8+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-141, -2)
    glVertex2f(-136, -3)
    glVertex2f(-130, -8)
    glVertex2f(-128, -4)
    glVertex2f(-124, -3)
    glVertex2f(-122, -7)
    glVertex2f(-124, -14)
    glVertex2f(-126, -16)
    glVertex2f(-124, -18)
    glVertex2f(-125, -21)
    glVertex2f(-127, -23)
    glVertex2f(-135, -25)
    glVertex2f(-140, -25)
    glVertex2f(-144, -22)
    glVertex2f(-145, -19)
    glVertex2f(-143, -17)
    glVertex2f(-146, -14)
    glVertex2f(-147, -8)
    glVertex2f(-144, -4)
    glEnd()
    glPopMatrix()

    #Telinga
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(25,8+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-154, -13)
    glVertex2f(-151, -12)
    glVertex2f(-149, -13)
    glVertex2f(-148, -20)
    glVertex2f(-150, -21)
    glVertex2f(-154, -20)
    glVertex2f(-156, -17)
    glEnd()
    glPopMatrix()

    #mata1a
    posx, posy = 0,0    
    sides = 32    
    radius = 4   
    glPushMatrix()
    glTranslated(-113,jump_height-2,0) 
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

    #mata2a
    posx, posy = 0,0    
    sides = 32    
    radius = 2  
    glPushMatrix()
    glTranslated(-113,jump_height-2,0) 
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

    #mata1b
    posx, posy = 0,0    
    sides = 32    
    radius = 3   
    glPushMatrix()
    glTranslated(-105,jump_height-2,0) 
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

    #mata2b
    posx, posy = 0,0    
    sides = 32    
    radius = 1  
    glPushMatrix()
    glTranslated(-105,jump_height-2,0) 
    glColor3ub(0, 0, 28)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()



    #badan
    glPushMatrix()
    glColor3ub(250,250,250)
    glTranslated(-50,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-72, -28)
    glVertex2f(-62, -29)
    glVertex2f(-61, -35)
    glVertex2f(-61, -42)
    glVertex2f(-64, -48)
    glVertex2f(-68, -50)
    glVertex2f(-72, -51)
    glVertex2f(-74, -52)
    glVertex2f(-78, -52)
    glVertex2f(-77, -57)
    glVertex2f(-80, -59)
    glVertex2f(-84, -58)
    glVertex2f(-86, -55)
    glVertex2f(-85, -51)
    glVertex2f(-83, -47)
    glVertex2f(-82, -42)
    glVertex2f(-82, -38)
    glVertex2f(-79, -33)
    glEnd()
    glPopMatrix()

    #tangan
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(-50,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-72, -30)
    glVertex2f(-70, -30)
    glVertex2f(-65, -36)
    glVertex2f(-61, -35)
    glVertex2f(-58, -36)
    glVertex2f(-57, -39)
    glVertex2f(-61, -43)
    glVertex2f(-71, -40)
    glVertex2f(-75, -36)
    glVertex2f(-74, -32)
    glEnd()
    glPopMatrix()
    
    #KAKI
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(-50,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-61, -43)
    glVertex2f(-58, -45)
    glVertex2f(-58, -49)
    glVertex2f(-61, -51)
    glVertex2f(-57, -53)
    glVertex2f(-59, -57)
    glVertex2f(-64, -58)
    glVertex2f(-68, -56)
    glVertex2f(-69, -53)
    glVertex2f(-67, -50)
    glVertex2f(-64, -48)
    glEnd()
    glPopMatrix()

    #ekor
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(25,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-165, -34)
    glVertex2f(-160, -38)
    glVertex2f(-155, -41)
    glVertex2f(-155, -43)
    glVertex2f(-162, -41)
    glVertex2f(-168, -36)
    glEnd()
    glPopMatrix()


def anoman4():
    #muka1
    glPushMatrix()
    glColor3ub(255,255,255)
    glTranslated(15,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-160, 10)
    glVertex2f(-140, 11)
    glVertex2f(-131, 10)
    glVertex2f(-123, 4)
    glVertex2f(-120, -1)
    glVertex2f(-120, -7)
    glVertex2f(-124, -16)
    glVertex2f(-123, -19)
    glVertex2f(-125, -22)
    glVertex2f(-135, -26)
    glVertex2f(-143, -26)
    glVertex2f(-147, -24)
    glVertex2f(-149, -22)
    glVertex2f(-152, -21)
    glVertex2f(-156, -18)
    glVertex2f(-156, -14)
    glVertex2f(-158, -9)
    glVertex2f(-158, 1)
    glVertex2f(-160, 6)
    glVertex2f(-158, 5)
    glEnd()
    glPopMatrix()

    #Muka2
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(15,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-141, -2)
    glVertex2f(-136, -3)
    glVertex2f(-130, -8)
    glVertex2f(-128, -4)
    glVertex2f(-124, -3)
    glVertex2f(-122, -7)
    glVertex2f(-124, -14)
    glVertex2f(-126, -16)
    glVertex2f(-124, -18)
    glVertex2f(-125, -21)
    glVertex2f(-127, -23)
    glVertex2f(-135, -25)
    glVertex2f(-140, -25)
    glVertex2f(-144, -22)
    glVertex2f(-145, -19)
    glVertex2f(-143, -17)
    glVertex2f(-146, -14)
    glVertex2f(-147, -8)
    glVertex2f(-144, -4)
    glEnd()
    glPopMatrix()

    #Telinga
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(15,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-154, -13)
    glVertex2f(-151, -12)
    glVertex2f(-149, -13)
    glVertex2f(-148, -20)
    glVertex2f(-150, -21)
    glVertex2f(-154, -20)
    glVertex2f(-156, -17)
    glEnd()
    glPopMatrix()

    
    #mata1a
    posx, posy = 0,0    
    sides = 32    
    radius = 4   
    glPushMatrix()
    glTranslated(-120,jump_height,0) 
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

    #mata2a
    posx, posy = 0,0    
    sides = 32    
    radius = 2  
    glPushMatrix()
    glTranslated(-120,jump_height,0) 
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

    #mata1b
    posx, posy = 0,0    
    sides = 32    
    radius = 3   
    glPushMatrix()
    glTranslated(-112,jump_height,0) 
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

    #mata2b
    posx, posy = 0,0    
    sides = 32    
    radius = 1  
    glPushMatrix()
    glTranslated(-112,jump_height,0) 
    glColor3ub(0, 0, 28)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()


    #badan
    glPushMatrix()
    glColor3ub(250,250,250)
    glTranslated(-15,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-109, -26)
    glVertex2f(-103, -26)
    glVertex2f(-100, -31)
    glVertex2f(-101, -38)
    glVertex2f(-103, -42)
    glVertex2f(-104, -44)
    glVertex2f(-109, -48)
    glVertex2f(-111, -52)
    glVertex2f(-115, -55)
    glVertex2f(-113, -56)
    glVertex2f(-113, -58)
    glVertex2f(-120, -60)
    glVertex2f(-124, -58)
    glVertex2f(-125, -54)
    glVertex2f(-119, -49)
    glVertex2f(-123, -45)
    glVertex2f(-124, -39)
    glVertex2f(-123, -36)
    glEnd()
    glPopMatrix()

    

    #tangan
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(-15,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-118, -28)
    glVertex2f(-113, -26)
    glVertex2f(-107, -28)
    glVertex2f(-108, -30)
    glVertex2f(-113, -33)
    glVertex2f(-115, -35)
    glVertex2f(-110, -35)
    glVertex2f(-108, -37)
    glVertex2f(-114, -43)
    glVertex2f(-120, -41)
    glVertex2f(-122, -32)
    glVertex2f(-123, -37)
    glEnd()
    glPopMatrix()
    
    #KAKI
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(-15,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-109, -42)
    glVertex2f(-101, -44)
    glVertex2f(-101, -47)
    glVertex2f(-103, -50)
    glVertex2f(-101, -51)
    glVertex2f(-100, -53)
    glVertex2f(-102, -55)
    glVertex2f(-105, -56)
    glVertex2f(-107, -55)
    glVertex2f(-112, -53)
    glVertex2f(-110, -49)
    glVertex2f(-109, -48)
    glVertex2f(-104, -44)
    glEnd()
    glPopMatrix()

    #ekor
    glPushMatrix()
    glColor3ub(230,230,230)
    glTranslated(20,10+jump_height,0)
    glBegin(GL_POLYGON)
    glVertex2f(-165, -34)
    glVertex2f(-160, -38)
    glVertex2f(-155, -41)
    glVertex2f(-155, -43)
    glVertex2f(-162, -41)
    glVertex2f(-168, -36)
    glEnd()
    glPopMatrix()

def skor_display(skor):
    
    glColor3f(0,0,0)
    glRasterPos( 250,270)
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(240, 293)
    glVertex2f(280, 293)
    glVertex2f(280, 264)
    glVertex2f(240, 264)
    glEnd()
    for i in str(skor):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(i))
    # glEnd()


"""Code gambar Karakter - end"""

"""Timer buat animasi - Start"""
def anomanAnimate(value): #buat ganti frame anomannya
    global anoman_index,isPlaying
    if isPlaying == False:
        return
    if anoman_index == 3:
        anoman_index = 0
    else :
        anoman_index +=1
    glutTimerFunc(200, anomanAnimate,0)

def jump_timer(value) : #timer loncat keatas
    global jump_height
    if jump_height < 100  :
        jump_height += 2
    else : 
        return down_timer(0)
    glutTimerFunc(10,jump_timer,0)

def down_timer(value) : #timer jatuh abis loncat
    global isJumping
    global jump_height
    if jump_height != 0  :
        jump_height -= 2
    else : 
        isJumping = False
        return 
    glutTimerFunc(10,down_timer,0)

def batu_timer(value) : #timer semak berjalan
    global speed_batu,isPlaying,score,deltaX,deltaXlevel2
    deltaX -= 2 - deltaXlevel2
    if isPlaying == False:
        print('selesai')
        return
    if deltaX < -610:
        deltaX = 0
        score += 1
        if score % 3 == 0 and score < 25 :
            speed_batu -= 1
        elif score % 6 == 0 and score > 24 :
            deltaXlevel2 += 1
        print(score)
        
    glutTimerFunc(speed_batu,batu_timer,0)

def timerAwan(value) :
    global deltaX_awan,isPlaying
    if isPlaying == False :
        return
    if deltaX_awan < -220 :
        deltaX_awan = 0
    deltaX_awan -= 0.3 
    glutTimerFunc(30,timerAwan,0)

def collision(value) :
    global anomanX1,anomanX2,anomanY1,anomanY2,jump_height
    global batuX1,batuX2,batuY1,batuY2,deltaX,isPlaying 
    if anomanX2  >= batuX1 + deltaX and anomanX1 <= batuX2 + deltaX and anomanY2 + jump_height >= batuY1 and anomanY1 + jump_height <= batuY2 : 
        isPlaying = False
        print("selesai")
        return
    glutTimerFunc(30,collision,0)

"""Timer buat animasi - End"""

"""Input keyboard - Start"""
def jump_button(key,x,y) : #Fungsi Input Keyboard loncat
    global isJumping,isPlaying  
 
    if key == GLUT_KEY_UP and isJumping is not True :
        isJumping = True
        jump_timer(0)
        print("loncat")
    if key == GLUT_KEY_UP and isJumping is True :
        pass

def play_button(key,x,y) : #Fungsi input keyboard play
    global isPlaying ,score,deltaX, speed_batu
    if key == b' ' and isPlaying == False :
        print("play")
        isPlaying = True
        score = 0
        deltaX = 0
        speed_batu = 10
        anomanAnimate(0)
        batu_timer(0)
        timerAwan(0)
        collision(0)
    if key == b's' :
        isPlaying = False
        print('end')
"""Input keyboard - End"""

"""Variables - Start"""
jump_height = 0
isJumping = False
anomanX1 = -150
anomanX2 = -120
anomanY1 = -50 + jump_height
anomanY2 = 0 + jump_height

deltaX = 0
deltaXlevel2 = 0
batuX1 = 270 - deltaX
batuX2 = 300 - deltaX
batuY1 = -50 
batuY2 = -10 
speed_batu = 10

anoman_version = [anoman1,anoman2,anoman3,anoman4]
anoman_index = 0

isPlaying = False
score = 0
deltaX_awan = 0
"""Variables - End"""
def iterate():
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-300, 300,-300, 300, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(1,1,1,1)
    iterate()
    # awan()
    background()
    gunung1()
    gunung2()
    tanah()
    rumput()
    matahari()
    awan_1()
    awan_2() 
    awan_3()
    awan_4()
    batu()
    batuGrad()
    anoman_version[anoman_index]()
    skor_display(score)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(1280//4, 0)
wind = glutCreateWindow("The Adventure of Anoman")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutKeyboardFunc(play_button)
glutSpecialFunc(jump_button)
glutMainLoop()
"""Fungsi Utama - End"""