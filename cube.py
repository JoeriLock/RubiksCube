from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy


class Cube:

    cubeDist = 2.1
    # vertices = corners (8 tot)
    # (x, y, z)
    verticies = (
        (1, -1, -1), #a
        (1, 1, -1), #b
        (-1, 1, -1), #c
        (-1, -1, -1),#d
        (1, -1, 1), #e
        (1, 1, 1), #f
        (-1, -1, 1),#g
        (-1, 1, 1) #h
        )
    # where edges connect to
    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (6, 3),
        (6, 4),
        (6, 7),
        (5, 1),
        (5, 4),
        (5, 7)
        )

    surfaces = (
        (0,1,2,3),
        (3,2,7,6),
        (6,7,5,4),
        (4,5,1,0),
        (1,5,7,2),
        (4,0,3,6)
        )

    colors = (
        (1,0,0), #red
        (0,1,0), #green
        (0,0,1), #blue
        (1,1,1), #white
        (1,0.5,0), #orange
        (1,1,0) #yellow
        )

    rotateX = (0, 0, 0, 0)
    rotateY = (0, 0, 0, 0)
    cubePos = [0,0,0]

    # test(*numpy.multiply(2,[1,2,3]))
    # def test(a,b,c):
    #     return a + b +c

    def __init__(self, x, y, z):
        self.position = numpy.multiply(self.cubeDist,[x, y ,z])
        self.cubePos = [x,y,z]
        self.x = 0
        self.y = 0
        self.rotationOrder = []
        self.check = 0

    def setCheck(self, check):
        self.check = check

    def draw(self):
        glPushMatrix()

        for axis in self.rotationOrder[::-1]:
            if(axis == 'x'):
                glRotate(90,1,0,0)
            else:
                glRotate(-90,0,1,0)

        glBegin(GL_QUADS)
        i = 0
        for surface in self.surfaces:
            glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [*self.colors[i], 1]) # geel materiaal, let op alpha
            glMaterial(GL_FRONT_AND_BACK, GL_SPECULAR, [1, 1, 1]) # witte reflectie
            glMaterial(GL_FRONT_AND_BACK, GL_SHININESS, 50) # groote van glimvlek
            i+=1
            for vertex in surface:
                glVertex3fv(numpy.add(self.position,self.verticies[vertex]))
        glEnd()

        glBegin(GL_LINES)
        if(self.check):
            glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [1,1,1, 1]) # geel materiaal, let op alpha
        else:
            glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [0,0,0,1]) # geel materiaal, let op alpha
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(numpy.add(self.position,self.verticies[vertex]))
        glEnd()
        glPopMatrix()

    def setRotate(self,direction, x, y, z):
        if(x != 0):
            self.cubePos[2],self.cubePos[1] = self.cubePos[1],(self.cubePos[2]*x)
            self.rotationOrder.append('x')
            if(x == -1):
                self.rotationOrder.append('x')
                self.rotationOrder.append('x')
        if(y == 1):
            self.cubePos[2],self.cubePos[0] = self.cubePos[0],(self.cubePos[2]*y)
            self.rotationOrder.append('y')
            if(y == -1):
                self.rotationOrder.append('y')
                self.rotationOrder.append('y')
