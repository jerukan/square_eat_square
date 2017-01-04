import pygame, random

from copy import deepcopy
from util import Colors, Constants


class Food:


    def __init__(self, xpos, ypos, surfposx, surfposy):
        self.SIZE = random.randint(Constants.FOODMINSIZE, Constants.FOODMAXSIZE)
        self.position = (xpos, ypos)
        self.model = pygame.Rect((surfposx, surfposy), (self.SIZE, self.SIZE))
        self.scaledmodel = deepcopy(self.model)
        self.COLOR = Colors.foodcolorlist[random.choice(list(Colors.foodcolorlist.keys()))]


    def scalemodel(self, value):
        self.scaledmodel = deepcopy(self.model)
        self.scaledmodel.width *= value
        self.scaledmodel.height *= value