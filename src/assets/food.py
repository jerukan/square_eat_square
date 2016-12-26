import pygame, random

from util import Colors, Constants


class Food:


    def __init__(self, xpos, ypos, surfposx, surfposy, scale):
        self.SIZE = random.randint(Constants.FOODMINSIZE, Constants.FOODMAXSIZE)
        self.position = (xpos, ypos)
        self.model = pygame.Rect((surfposx, surfposy), (self.SIZE * scale, self.SIZE * scale))
        self.COLOR = Colors.enemycolorlist[random.choice(list(Colors.enemycolorlist.keys()))]
