import pygame

from util import Colors, Constants
from window.menuscreens import *


class Surface:

    pygame.init()

    CAMERARECT = pygame.Rect(0, 0, Constants.WINDOWWIDTH, Constants.WINDOWHEIGHT)

    foods = []

    enemies = []

    DISPLAYSURFACE = pygame.display.set_mode((Constants.WINDOWWIDTH, Constants.WINDOWHEIGHT))

    pygame.display.set_caption('SQUARE EAT SQUARE')


    def __init__(self):
        self.initScreens()


    def resetScreen(self):
        self.foods = []
        self.enemies = []


    def fillSurface(self):

        self.DISPLAYSURFACE.fill(Colors.colorlist['white'])


    def scaleassets(self, camera, player):
        player.scalemodel(camera.scale)
        for food in self.foods:
            food.scalemodel(camera.scale)
        for enemy in self.enemies:
            enemy.scalemodel(camera.scale)


    def converttoscreencoords(self, xpos_ypos, cam):

        x, y = xpos_ypos

        screenx = x - cam.position[0]
        screeny = y - cam.position[1]

        screenx += Constants.WINDOWCENTER[0]
        screeny = Constants.WINDOWCENTER[1] - screeny

        if screenx >= Constants.WINDOWCENTER[0]:
            screenx -= Constants.WINDOWCENTER[0]
            screenx *= cam.scale
            screenx += Constants.WINDOWCENTER[0]
        else:
            screenx = Constants.WINDOWCENTER[0] - screenx
            screenx *= cam.scale
            screenx = Constants.WINDOWCENTER[0] - screenx
        if screeny >= Constants.WINDOWCENTER[1]:
            screeny -= Constants.WINDOWCENTER[1]
            screeny *= cam.scale
            screeny += Constants.WINDOWCENTER[1]
        else:
            screeny = Constants.WINDOWCENTER[1] - screeny
            screeny *= cam.scale
            screeny = Constants.WINDOWCENTER[1] - screeny

        return screenx, screeny


    def drawText(self, text, x, y, fontsize):
        font = pygame.font.SysFont(None, fontsize)
        textObj = font.render(text, True, Colors.colorlist['white'])
        textRect = textObj.get_rect()
        textRect.center = (x, y)
        self.DISPLAYSURFACE.blit(textObj, textRect)


    def initScreens(self):
        self.mainmenuscreen = Mainmenuscreen()
        self.helpscreen = Helpscreen()
        self.gameoverscreen = Gameoverscreen()