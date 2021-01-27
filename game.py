# Joeri Lock - 0879801

# Draws a cube and turns it with an angle of 30 degrees
# Has Animated function cause looks cool. Can be turnend of by changes ANIMATED boolean (line 15)
#

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from cube import Cube
#from positionHandler import PositionHandler
import time
import numpy
from copy import deepcopy

DEBUG = False
ANIMATED = True

class Game:

    controls = ""

    SPEED = 0.05

    keyCache = "";
    cubes = []

    # def __init__(self):
    #     self.cube.append(Cube())
    #     # basic config to create window
    #     glutInit()
    #     glutInitDisplayMode(GLUT_MULTISAMPLE | GLUT_DOUBLE | GLUT_DEPTH)
    #     glutInitWindowSize(500, 500)
    #     glutCreateWindow("Perspective view".encode("ascii"))
    #     glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    #     glEnable(GL_BLEND)
    #     glEnable(GL_LINE_SMOOTH)
    #     glEnable(GL_DEPTH_TEST)
    #     glMatrixMode(GL_PROJECTION) # lichtbronnen moeten niet geprojecteerd worden, dus om onderscheid te kunnen maken moet de projectiematrix in een andere "matrix modus"
    #     glMatrixMode(GL_MODELVIEW) # schakel terug naar de "model/view transformatiematrix modus"
    #     glEnable(GL_LIGHTING) # belichting
    #     glEnable(GL_RESCALE_NORMAL) # zorgt voor correcte belichting van geschaalde objecten
    #     glEnable(GL_LIGHT0) # een lichtbron
    #     glLight(GL_LIGHT0, GL_POSITION, [-3, 4, 5]) # positie lichtbron
    #     glLight(GL_LIGHT0, GL_DIFFUSE, [1, 0, 1]) # kleur lichtbron (paars)
    #     glLight(GL_LIGHT0, GL_AMBIENT, [1, 0, 1]) # kleur ambient licht (paars)
    #     # what to draw each frame
    #     #glutDisplayFunc(self.showScreen) #init drawing
    #     glutIdleFunc(self.showScreen)
    #     glutKeyboardFunc(self.keyPressed)
    #     glutMouseFunc(self.mouseAction)
    #     glutMainLoop()
    def __init__(self):
        self.createCubes()
        # basic config to create window
        glutInit()
        glutInitDisplayMode(GLUT_MULTISAMPLE | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(500, 500)
        glutCreateWindow("Rubcis cube".encode("ascii"))
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_DEPTH_TEST)
        glLineWidth(5)
        # what to draw each frame
        #glutDisplayFunc(self.showScreen) #init drawing
        glutIdleFunc(self.showScreen)
        glutKeyboardFunc(self.keyPressed)
        glutMouseFunc(self.mouseAction)
        glutMainLoop()


    def createCubes(self):
        for depth in range(-1,2):
            for ver in range(-1,2):
                for hor in range(-1,2):
                    cube = Cube(hor,ver,depth)
                    self.cubes.append(cube)


    # Draw all that is need
    def showScreen(self):
        #print("game".self.controls.getInput())
        phi = 0.02 * glutGet(GLUT_ELAPSED_TIME)
        glViewport(0, -0, 500, 500) #Draw area (x,y, width, height)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear screen
        glLoadIdentity() # wis de huidige matrix
        glFrustum(-1, 1, -1.0, 1.0,1, 20) # 3d matrix warin in dingen kan neer zetten

        glTranslate(0, 0, -8) # translatie (beweeg een beetje naar achter)

        glRotatef(33, *self.getDirection()); # rotates whole object
        # draws rubik
        #glTranslate(0.5,0.5, 0)
        #self.cubes[0].setRotate(phi,0, 0, 1)

        #PositionHandler.rotateSide()w
        #for i in range(2,27,3):
        self.cubes[18].setRotate(0.2,1,0,0)
        #for i in range(18,27):
    #        self.cubes[i].setRotate(90,0,0,1)
        for cube in self.cubes:
            cube.draw()

        glutSwapBuffers()




    def mouseAction(self, *args):
        print(args)

    def keyPressed(self,*args):
        #print(args)
        if args[0] == '\x08':
            self.keyCache = self.keyCache[:-1]
        elif args[0] == b'\x1b':
            glutDestroyWindow("Rubcis cube")
        else:
            self.keyCache = args[0]

    def getDirection(self):

        if(self.keyCache == ' '):
            return (0,0,0)

        if self.keyCache == b'w':
            return (1,0,0)
        elif self.keyCache == b'd':
            return (0,-1,0)
        elif self.keyCache == b'a':
            return (0,1,0)
        elif self.keyCache == b's':
            return (-1,0,0)
        elif self.keyCache == b'1':
            print(self.cubes[18].cubePos)
            self.keyCache = ''
        return (0,0,0)

Game()
