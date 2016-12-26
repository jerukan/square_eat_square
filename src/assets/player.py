import pygame

from copy import deepcopy
from util import Constants
from pygame.locals import *

class Player:


    position = [0, 0]

    model = pygame.Rect((Constants.WINDOWCENTER[0] - int(Constants.PLAYERWIDTH/2), Constants.WINDOWCENTER[1] - int(Constants.PLAYERHEIGHT/2)), (Constants.PLAYERWIDTH, Constants.PLAYERHEIGHT))

    scaledmodel = deepcopy(model)

    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False

    def getInput(self, event):
        if event.type == KEYDOWN:
            if event.key == K_a:
                self.moveRight = False
                self.moveLeft = True
            if event.key == K_d:
                self.moveRight = True
                self.moveLeft = False
            if event.key == K_w:
                self.moveUp = True
                self.moveDown = False
            if event.key == K_s:
                self.moveUp = False
                self.moveDown = True

        if event.type == KEYUP:
            if event.key == K_a:
                self.moveLeft = False
            if event.key == K_d:
                self.moveRight = False
            if event.key == K_w:
                self.moveUp = False
            if event.key == K_s:
                self.moveDown = False


    def move(self):
        if self.moveLeft:
            self.position[0] -= Constants.PLAYERMOVESPEED
        if self.moveRight:
            self.position[0] += Constants.PLAYERMOVESPEED
        if self.moveDown:
            self.position[1] -= Constants.PLAYERMOVESPEED
        if self.moveUp:
            self.position[1] += Constants.PLAYERMOVESPEED

        print('player position: ' + str(self.position))
        print('player surf position: ' + str(self.scaledmodel.center))


    def scaleplayer(self, value):
        self.scaledmodel = deepcopy(self.model)
        self.scaledmodel.width *= value
        self.scaledmodel.height *= value
