import pygame
from util.colors import Colors

class Screen:

    #takes in buttons as arguments
    def __init__(self, *args):
        self.buttonlist = []
        for button in args:
            self.buttonlist.append(button)


    def drawText(self, text, x, y, surface, fontsize):
        font = pygame.font.SysFont(None, fontsize)
        textObj = font.render(text, True, Colors.colorlist['black'])
        textRect = textObj.get_rect()
        textRect.center = (x, y)
        surface.blit(textObj, textRect)


    def checkbuttonclicks(self, mouseclickposition):
        for button in self.buttonlist:
            nextscreen = button.onClick(mouseclickposition)
            if nextscreen is not None:
                return nextscreen
        return None


    def displayscreen(self, surface, mousehoverposition):
        pass