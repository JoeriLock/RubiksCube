

class CubeHandler:

    def __init__(self, cubes):
        self.cubes = cubes

    def getX(self,i):
        list = []
        for cube in self.cubes:
            if cube.cubePos[0] == i:
                list.append(cube)
        return list

    def getY(self,i):
        list = []
        for cube in self.cubes:
            if cube.cubePos[1] == i:
                list.append(cube)
        return list




    def getTestCube(self):
        return self.cubes[18]
