import pygame
from util.colors import Colors

class Button:

    def __init__(self, x, y, width, height, text):
        self.position = [x, y]
        self.width = width
        self.height = height
        self.text = text

        self.buttonrect = pygame.Rect(x, y, self.width, self.height)


    def drawText(self, text, x, y, surface):
        font = pygame.font.SysFont(None, 60)
        textObj = font.render(text, True, Colors.colorlist['black'])
        textRect = textObj.get_rect()
        textRect.center = (x, y)
        surface.blit(textObj, textRect)


    def isHoveredOver(self, mousehoverposition):
        if self.buttonrect.collidepoint(mousehoverposition[0], mousehoverposition[1]):
            return True
        return False


    def highlightbutton(self, mousehoverposition, surface):
        if self.isHoveredOver(mousehoverposition):
            highlightSurface = pygame.Surface((self.buttonrect.width, self.buttonrect.height))
            highlightSurface = highlightSurface.convert_alpha()
            highlightSurface.fill(Colors.colorlist['transparentgreen'])
            surface.blit(highlightSurface, self.buttonrect.topleft)


    def displaybutton(self, surface, mousehoverposition):
        pygame.draw.rect(surface, Colors.colorlist['black'], self.buttonrect, 2)
        self.drawText(self.text, self.buttonrect.centerx, self.buttonrect.centery, surface)
        self.highlightbutton(mousehoverposition, surface)


    def isclicked(self, mouseclickposition):
        if self.isHoveredOver(mouseclickposition):
            return True
        return False


    def onClick(self, mouseclickposition):
        pass