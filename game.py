# Joeri Lock - 0879801

# Draws a cube and turns it with an angle of 30 degrees
# Has Animated function cause looks cool. Can be turnend of by changes ANIMATED boolean (line 15)
# Shaders
# textures
# lightsource
# animation

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from cube import Cube
from cubeHandler import CubeHandler
import time
import numpy
from copy import deepcopy
from PIL import Image # voor plaatjes

DEBUG = False
ANIMATED = True

class Game:

    SPEED = 0.05

    def __init__(self):
        self.cubes = self.createCubes()
        self.keyCache = "";
        self.cubeHandler = CubeHandler(self.cubes)
        #self.cubeHanlder = CubeHandler()
        # basic config to create window
        glutInit()
        glutInitDisplayMode(GLUT_MULTISAMPLE | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(500, 500)
        glutCreateWindow("Rubcis cube".encode("ascii"))
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_GEN_S) # zet het automatisch genereren van horizontale textuur-coordinaten aan
        glEnable(GL_TEXTURE_GEN_T)
        glLineWidth(5)

        img = Image.open("Wouter_vierkant.png")
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1) # voor plaatjes met oneven aantal pixels
        texture = glGenTextures(1) # maak een ID voor 1 textuur
        glBindTexture(GL_TEXTURE_2D, texture) # gebruik de ID
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) # specificeer hoe de textuur geschaald moet worden
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img.tobytes()) # laad het plaatje
        glEnable(GL_TEXTURE_2D) # zet textuur aan
        glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR) # mode voor genereren van horizontale textuur-coordinaten
        glTexGenfv(GL_S, GL_OBJECT_PLANE, [2, 0, 0, 0]) # vlak x = 0 (yz-vlak)
        glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR) # mode voor genereren van verticale textuur-coordinaten
        glTexGenfv(GL_T, GL_OBJECT_PLANE, [0, -2, 0, 0]) # vlak y = 0 (xz-vlak)

        # what to draw each frame
        #glutDisplayFunc(self.showScreen) #init drawing
        glutIdleFunc(self.showScreen)
        glutKeyboardFunc(self.keyPressed)
        glutMouseFunc(self.mouseAction)
        glutMainLoop()


    def createCubes(self):
        cubes = []
        for depth in range(-1,2):
            for ver in range(-1,2):
                for hor in range(-1,2):
                    cube = Cube(hor,ver,depth)
                    cubes.append(cube)
        return cubes

    # Draw all that is need
    def showScreen(self):
        phi = 0.02 * glutGet(GLUT_ELAPSED_TIME)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear screen
        glLoadIdentity() # wis de huidige matrix
        glViewport(0, -0, 500, 500) #Draw area (x,y, width, height)
        glFrustum(-1, 1, -1.0, 1.0,1, 20) # 3d matrix warin in dingen kan neer zetten
        glTranslate(0, 0, -8) # translatie (beweeg een beetje naar achter)




        glRotatef(33, *self.getDirection()); # Changes view on key press
        # for cube in self.cubeHandler.getX(0):
        #     cube.setRotate(1,1,0,0) #move down
        i = self.getRow()
        if(i == 1):
            print("got here")
            for cube in self.cubeHandler.getX(0):
              cube.setRotate(1,1,0,0) #move right
        if(i == 2):
            print("moe y")
            for cube in self.cubeHandler.getY(0):
                cube.setRotate(1,0,1,0) #move right
        # for cube in self.cubeHandler.getX(-1):
        #     cube.setRotate(1,1,0,0)
        #self.cubeHandler.getTestCube().setRotate(0.2,0,1,0)
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

    def getRow(self):
        if self.keyCache == b'1':
            print('1')
            self.keyCache = ''
            return 1
        if self.keyCache == b'2':
            self.keyCache = ''
            return 2
        return 0

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
        return (0,0,0)

Game()
