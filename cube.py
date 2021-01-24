from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy




class Cube:
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

    rotate = (0, 0, 0, 0)
    position = (0,0,0)


    def draw(self, x, y ,z):
        glPushMatrix()
        glRotate(*self.rotate)
        glBegin(GL_QUADS)
        i = 0
        for surface in self.surfaces:
            glColor3fv(self.colors[i])
            i+=1
            for vertex in surface:
                glVertex3fv(numpy.add((x,y,z),self.verticies[vertex]))
        glEnd()

        glBegin(GL_LINES)
        glColor3fv((0,0,0))
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(numpy.add((x,y,z),self.verticies[vertex]))
        glEnd()
        glPopMatrix()

    def setRotate(self,_rotate, x, y, z):
        self.rotate = (_rotate, x, y, z)
