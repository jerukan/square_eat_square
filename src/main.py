import pygame, sys

from pygame.locals import *
from assets import *
from window import *
from eventhandlers import *

CLOCK = pygame.time.Clock()

player1 = Player()
cam = Camera()
surf = Surface()

foodhandler = Foodhandler(surf)
enemycontroller = Enemycontroller(surf)

def runmenus():
    previousscreen = surf.mainmenuscreen
    currentscreen = surf.mainmenuscreen
    while True:
        surf.fillSurface()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouseclickposition = pygame.mouse.get_pos()
            else:
                mouseclickposition = None
            mousehoverposition = pygame.mouse.get_pos()
        currentscreen.displayscreen(surf.DISPLAYSURFACE, mousehoverposition)
        if mouseclickposition is not None:
            nextscreen = currentscreen.checkbuttonclicks(mouseclickposition)

            if nextscreen == "game":
                rungame()

        pygame.display.update()


def rungame():

    foodhandler.createStartingThings(cam, player1)

    while True:

        surf.fillSurface()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            player1.getInput(event)

        foodhandler.runEvents(player1, cam)
        enemycontroller.run(player1, cam)

        player1.move()
        cam.shouldMove(player1.position)

        player1.draw(surf, cam)

        pygame.display.update()
        CLOCK.tick(40)


if __name__ == "__main__":
    runmenus()