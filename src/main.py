import pygame, sys

from pygame.locals import *
from assets import *
from window import *
from eventhandlers import *

CLOCK = pygame.time.Clock()

player1 = Player()
cam = Camera()
cam.initCamera()
surf = Surface()

foodhandler = Foodhandler(surf)
enemycontroller = Enemycontroller(surf)

previousscreen = surf.mainmenuscreen
currentscreen = surf.mainmenuscreen

def runmenu():
    global previousscreen
    global currentscreen
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
            elif nextscreen == "help":
                previousscreen = currentscreen
                currentscreen = surf.helpscreen
            elif nextscreen == "back":
                currentscreen = previousscreen
            elif nextscreen == "home":
                currentscreen = surf.mainmenuscreen

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
        gamestate = enemycontroller.run(player1, cam)

        player1.move()
        cam.shouldMove(player1.position)

        player1.draw(surf, cam)

        pygame.display.update()
        CLOCK.tick(40)

        if gamestate == "gameover":
            cam.initCamera()
            surf.resetScreen()
            player1.resetPlayer()
            currentscreen = surf.gameoverscreen
            return


if __name__ == "__main__":
    while True:
        runmenu()