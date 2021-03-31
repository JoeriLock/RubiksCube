

class CubeHandler:

    def __init__(self, cubes):
        self.cubes = cubes
        self.direction = ''

    def getX(self,i):
        list = []
        self.direction = 'x'
        for cube in self.cubes:
            cube.setCheck(0)
            if cube.cubePos[0] == i:
                cube.setCheck(1)
                list.append(cube)
        return list

    def getY(self,i):
        list = []
        self.direction = 'y'
        for cube in self.cubes:
            cube.setCheck(0)
            if cube.cubePos[1] == i:
                cube.setCheck(1)
                list.append(cube)
        return list

    def rotateSelected(self,dir):
        if(self.direction == 'x'):
            for cube in self.cubes:
                if cube.check:
                    cube.setRotate(1,dir,0,0)
        if(self.direction == 'y'):
            for cube in self.cubes:
                if cube.check:
                    cube.setRotate(1,0,dir,0)



    def getTestCube(self):
        return self.cubes[18]
