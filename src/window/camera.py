import math

from util import Functions, Constants

class Camera:

    position = [0, 0]

    xrange = Constants.WINDOWWIDTH
    yrange = Constants.WINDOWHEIGHT

    scale = 1

    moving = False


    def move(self, xgoal, ygoal):

        xDist = xgoal - self.position[0]
        yDist = ygoal - self.position[1]

        disttopoint = math.sqrt(xDist**2 + yDist**2)

        xSpeed = int(Constants.CAMERAMOVESPEED * xDist / disttopoint)
        ySpeed = int(Constants.CAMERAMOVESPEED * yDist / disttopoint)

        self.position[0] += xSpeed
        self.position[1] += ySpeed


    def shouldMove(self, playerpos):

        distance = Functions().getdistance((self.position[0], self.position[1]), playerpos)

        if distance > Constants.CAMERASLACK:
            self.moving = True
            self.move(playerpos[0], playerpos[1])

        if self.moving:
            if distance > 4:
                self.move(playerpos[0], playerpos[1])
            else:
                self.moving = False

        print('camera position: ' + str(self.position))


    def extendrange(self, value):
        self.xrange = int(self.xrange * value)
        self.yrange = int(self.yrange * value)
        self.scale = Constants.WINDOWWIDTH / self.xrange
