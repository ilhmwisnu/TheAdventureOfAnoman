from sys import flags, float_repr_style
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

"""Code gambar Karakter - Start"""

def anoman1() : #Gambar Karakter Anoman frame 1 (ada animasi geraknya)
    glPushMatrix()
    glColor3ub(250, 185, 135)
    glTranslated(0,jump_height,0)
    glBegin(GL_QUADS)
    glVertex2f(anomanX1+2,anomanY1+2) 
    glVertex2f(anomanX1+2,anomanY2-2)
    glVertex2f(anomanX2-2,anomanY2-2)
    glVertex2f(anomanX2-2,anomanY1+2)
    glEnd()
    glPopMatrix()


def anoman2() : #Gambar Karakter Anoman frame 2
    glPushMatrix()
    glColor3ub(175, 235, 96)
    glTranslated(0,jump_height,0)
    glBegin(GL_QUADS)
    glVertex2f(anomanX1+2,anomanY1+2) 
    glVertex2f(anomanX1+2,anomanY2-2)
    glVertex2f(anomanX2-2,anomanY2-2)
    glVertex2f(anomanX2-2,anomanY1+2)
    glEnd()
    glPopMatrix()

def anoman3() : #Gambar Karakter Anoman frame 3
    glPushMatrix()
    glColor3ub(43, 76, 92)
    glTranslated(0,jump_height,0)
    glBegin(GL_QUADS)
    glVertex2f(anomanX1+2,anomanY1+2) 
    glVertex2f(anomanX1+2,anomanY2-2)
    glVertex2f(anomanX2-2,anomanY2-2)
    glVertex2f(anomanX2-2,anomanY1+2)
    glEnd()
    glPopMatrix()

def anomanFrame() : #anomanFrame buat collision
    glPushMatrix()
    glColor3ub(255,255,255)
    glTranslated(0,jump_height,0)
    glBegin(GL_QUADS)
    glVertex2f(anomanX1,anomanY1) 
    glVertex2f(anomanX1,anomanY2)
    glVertex2f(anomanX2,anomanY2)
    glVertex2f(anomanX2,anomanY1)
    glEnd()
    glPopMatrix()

def semakFrame() : #buat collision semak2nya
    glPushMatrix()
    glColor3ub(255,255,255)
    glTranslated(deltaX,0,0)
    glBegin(GL_QUADS)
    glVertex2f(semakX1,semakY1) 
    glVertex2f(semakX1,semakY2)
    glVertex2f(semakX2,semakY2)
    glVertex2f(semakX2,semakY1)
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

def awan(): #Tampilan awan
    glPushMatrix()
    glScale(3.5,3.5,0)
    glTranslated(50,60,0) 
    glTranslate(0,0,0)
    glColor3ub(255,255,255)
    glBegin(GL_QUADS)
    glVertex2f(-7,-5) 
    glVertex2f(7,-5)
    glVertex2f(7,5)
    glVertex2f(-7,5)
    glEnd()
    glPopMatrix()
"""Code gambar Karakter - end"""


"""Timer buat animasi - Start"""
def anomanAnimate(value): #buat ganti frame anomannya
    global anoman_index,isPlaying
    if isPlaying == False:
        return
    if anoman_index == 2:
        anoman_index = 0
    else :
        anoman_index +=1
    glutTimerFunc(1000, anomanAnimate,0)

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

def semak_timer(value) : #timer semak berjalan
    global deltaX,speed_semak,isPlaying,score
    deltaX -= 2
    if isPlaying == False:
        print('selesai')
        return
    if deltaX < -610:
        deltaX = 0
        score += 1
        print(score)
        
    glutTimerFunc(speed_semak,semak_timer,0)
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
    global isPlaying ,score,deltaX
       
    if key == b' ' and isPlaying == False :
        print("play")
        isPlaying = True
        score = 0
        deltaX = 0
        anomanAnimate(0)
        semak_timer(0)
    if key == b's' :
        isPlaying = False
        print('end')
"""Input keyboard - End"""

"""Variables - Start"""
jump_height = 0
isJumping = False
anomanX1 = -160
anomanX2 = -120
anomanY1 = -50 + jump_height
anomanY2 = 0 + jump_height

deltaX = 0
semakX1 = 270 - deltaX
semakX2 = 300 - deltaX
semakY1 = -50 
semakY2 = -10 
speed_semak = 10

anoman_version = [anoman1,anoman2,anoman3]
anoman_index = 0

isPlaying = False
score = 0
"""Variables - End"""

"""Fungsi Utama - Star"""
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
    glClearColor(0.7, 0.7, 1,1)
    iterate()
    awan()
    tanah()
    anomanFrame()
    semakFrame()
    anoman_version[anoman_index]()
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