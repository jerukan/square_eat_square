import pygame

from util import Colors, Constants


class Surface:

    pygame.init()

    CAMERARECT = pygame.Rect(0, 0, Constants.WINDOWWIDTH, Constants.WINDOWHEIGHT)

    foods = []

    DISPLAYSURFACE = pygame.display.set_mode((Constants.WINDOWWIDTH, Constants.WINDOWHEIGHT))

    pygame.display.set_caption('SQUARE EAT SQUARE')


    def fillSurface(self):

        self.DISPLAYSURFACE.fill(Colors.colorlist['white'])


    def converttoscreencoords(self, xpos_ypos, cam):

        x, y = xpos_ypos

        '''x *= cam.scale
        y *= cam.scale'''

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


    def drawPlayer(self, player, cam):

        playerx, playery = self.converttoscreencoords(player.position, cam)

        player.model.center = (playerx, playery)

        player.scaledmodel.center = player.model.center

        pygame.draw.rect(self.DISPLAYSURFACE, Colors.colorlist['black'], player.scaledmodel)

        self.drawText(Constants.PLAYERNAME, player.scaledmodel.center[0], player.scaledmodel.center[1], int(player.scaledmodel.width / 3))


    def drawText(self, text, x, y, fontsize):
        font = pygame.font.SysFont(None, fontsize)
        textObj = font.render(text, True, Colors.colorlist['white'])
        textRect = textObj.get_rect()
        textRect.center = (x, y)
        self.DISPLAYSURFACE.blit(textObj, textRect)


