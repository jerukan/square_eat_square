import pygame, sys

from pygame.locals import *
from assets import *
from window import *
from eventhandlers import *


def main():

    CLOCK = pygame.time.Clock()

    player1 = Player()
    cam = Camera()
    surf = Surface()

    surfacehandler = Foodhandler(surf)

    surfacehandler.createStartingThings(cam, player1)

    while True:

        surf.fillSurface()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            player1.getInput(event)

        surfacehandler.runEvents(player1, cam)

        player1.move()
        cam.shouldMove(player1.position)

        surf.drawPlayer(player1, cam)

        pygame.display.update()
        CLOCK.tick(40)


if __name__ == "__main__":
    main()