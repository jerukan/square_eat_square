import pygame

from copy import deepcopy
from util import Constants, Colors
from pygame.locals import *

class Player:


    position = [0, 0]

    model = pygame.Rect((Constants.WINDOWCENTER[0] - int(Constants.PLAYERSIZE/2), Constants.WINDOWCENTER[1] - int(Constants.PLAYERSIZE/2)), (Constants.PLAYERSIZE, Constants.PLAYERSIZE))

    scaledmodel = deepcopy(model)

    speed = [0, 0]

    def getInput(self, event):
        if event.type == KEYDOWN:
            if event.key == K_a:
                self.speed[0] = -Constants.PLAYERMOVESPEED
            if event.key == K_d:
                self.speed[0] = Constants.PLAYERMOVESPEED
            if event.key == K_w:
                self.speed[1] = Constants.PLAYERMOVESPEED
            if event.key == K_s:
                self.speed[1] = -Constants.PLAYERMOVESPEED
            if event.key == K_f:
                self.position = [0, 0]

        if event.type == KEYUP:
            if event.key == K_a or event.key == K_d:
                self.speed[0] = 0
            if event.key == K_w or event.key == K_s:
                self.speed[1] = 0


    def move(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]



    def scalemodel(self, value):
        self.scaledmodel = deepcopy(self.model)
        self.scaledmodel.width *= value
        self.scaledmodel.height *= value


    def draw(self, surface, camera):

        playerx, playery = surface.converttoscreencoords(self.position, camera)

        self.model.center = (playerx, playery)
        self.scaledmodel.center = self.model.center

        pygame.draw.rect(surface.DISPLAYSURFACE, Colors.colorlist['black'], self.scaledmodel)

        surface.drawText(Constants.PLAYERNAME, self.scaledmodel.center[0], self.scaledmodel.center[1], int(self.scaledmodel.width / 3))
