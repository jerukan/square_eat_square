import random, pygame

from copy import deepcopy
from util import Constants, Functions

class Enemy:

    ENEMYCOLOR = (255, 0, 0)
    vector = [0, 0]


    def __init__(self, playersize, xpos, ypos, surfx, surfy):
        maxenemysize = int(playersize * 1.5)
        minenemysize = int(playersize / 2)
        self.SIZE = random.randint(minenemysize, maxenemysize)

        self.position = [xpos, ypos]

        self.model = pygame.Rect((surfx, surfy), (self.SIZE, self.SIZE))
        self.scaledmodel = deepcopy(self.model)

        self.MAXSPEED = minenemysize * (0.955 ** (self.SIZE-65))


    def scalemodel(self, value):
        self.scaledmodel = deepcopy(self.model)
        self.scaledmodel.width *= value
        self.scaledmodel.height *= value


    def move(self):
        self.position[0] += self.vector[0]
        self.position[1] += self.vector[1]


    def searchandmove(self, player, otherenemies, foods):

        fleeing = False

        distancetoplayer = Functions().getdistance(self.position, player.position)


        try:
            vectortoplayer = [(self.position[0] - player.position[0]) / distancetoplayer * self.MAXSPEED, (self.position[1] - player.position[1]) / distancetoplayer * self.MAXSPEED]
        except ZeroDivisionError:
            vectortoplayer = [0, 0]


        closestfood = Functions().closestobjectfromlist(self, foods)
        distancetofood = Functions().getdistance(self.position, closestfood.position)
        try:
            vectortofood = [(self.position[0] - closestfood.position[0]) / distancetofood * self.MAXSPEED,
                            (self.position[1] - closestfood.position[1]) / distancetofood * self.MAXSPEED]
        except ZeroDivisionError:
            vectortofood = [0, 0]


        closestenemy = Functions().closestobjectfromlist(self, otherenemies)
        distancetoenemy = Functions().getdistance(self.position, closestenemy.position)
        try:
            vectortoenemy = [(self.position[0] - closestenemy.position[0]) / distancetoenemy * self.MAXSPEED, (self.position[1] - closestenemy.position[1]) / distancetoenemy * self.MAXSPEED]
        except ZeroDivisionError:
            vectortoenemy = [0, 0]


        if player.model.width > self.model.width or closestenemy.model.width > self.model.width:
            if distancetoenemy < Constants.HUNTINGRANGE or distancetoplayer < Constants.HUNTINGRANGE:
                fleeing = True

        if fleeing:
            self.vector = [(vectortoenemy[0] + vectortoplayer[0]) / 2, (vectortoenemy[1] + vectortoplayer[1]) / 2]

        else:
            if distancetoplayer < Constants.HUNTINGRANGE:
                self.vector[0] = -vectortoplayer[0]
                self.vector[1] = -vectortoplayer[1]
            else:
                self.vector[0] = -vectortofood[0]
                self.vector[1] = -vectortofood[1]
