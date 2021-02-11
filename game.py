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

DEBUG = False
ANIMATED = True

class Game:

    SPEED = 0.05

    def __init__(self):
        self.cubes = self.createCubes()
        self.keyCache = "";
        self.cubeHandler = CubeHandler(self.cubes)
        self.cameraAngle = {"ver":0, "hor":0, "up":0, "down":0}
        self.startTime = 0;
        self.mouseStatus = (0,2,0,0);
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
        glEnable(GL_TEXTURE_2D) # zet textuur aan
        glLineWidth(5)


        # what to draw each frame
        glutDisplayFunc(self.showScreen) #init drawing
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



    def updateCamera(self):
        if(self.mouseStatus[1] == 0):
            timeDif = glutGet(GLUT_ELAPSED_TIME) - self.startTime
            self.cameraAngle["up"] += (self.cameraAngle["ver"] * timeDif * 0.02)
            self.cameraAngle["down"] += (self.cameraAngle["hor"] * timeDif * 0.02)
    # Draw all that is need
    def showScreen(self):
        phi = 0.02 * (glutGet(GLUT_ELAPSED_TIME) - self.startTime)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear screen
        glLoadIdentity() # wis de huidige matrix
        glViewport(0, -0, 500, 500) #Draw area (x,y, width, height)
        glFrustum(-1, 1, -1.0, 1.0,1, 20) # 3d matrix warin in dingen kan neer zetten
        glTranslate(0, 0, -8) # translatie (beweeg een beetje naar achter)
        self.updateCamera()
        glRotatef(self.cameraAngle["down"],0,1,0);


        glRotatef(self.cameraAngle["up"],1,0,0); # Changes view on key press
        # for cube in self.cubeHandler.getX(0):
        #     cube.setRotate(1,1,0,0) #move down
        i = self.getRow()
        if(1 <= i <= 3):
            self.cubeHandler.getX(i-2)
        if(4 <= i <= 6):
            self.cubeHandler.getY(i -5)
        if(i == 9):
            self.cubeHandler.rotateSelected()

        for cube in self.cubes:
            cube.draw()

        glutSwapBuffers()



    def mouseAction(self, *args):
        self.mouseStatus = args
        self.startTime = glutGet(GLUT_ELAPSED_TIME);

        if(args[2] <= 333):
            self.cameraAngle["hor"] = 0
        if(args[2] <= 166):
            self.cameraAngle["hor"] += -1
        if(args[2] > 333):
            self.cameraAngle["hor"] = 1

        if(args[3] <= 333):
            self.cameraAngle["ver"] = 0
        if(args[3] <= 166):
            self.cameraAngle["ver"] = -1
        if(args[3] > 333):
            self.cameraAngle["ver"] = 1

    def keyPressed(self,*args):
        if args[0] == '\x08':
            self.keyCache = self.keyCache[:-1]
        elif args[0] == b'\x1b':
            glutDestroyWindow("Rubcis cube")
        else:
            self.keyCache = args[0]

    def getRow(self):
        key = self.keyCache
        if(key.isdigit()):
            self.keyCache = ''
            return int(key)


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
