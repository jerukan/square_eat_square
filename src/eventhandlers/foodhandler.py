import pygame, random

from assets import Food
from util import Constants
from copy import deepcopy

class Foodhandler:

    def __init__(self, surface):

        self.surface = surface


    def runEvents(self, player, camera):
        self.removeThings(camera)
        self.addThingsRandomly(camera)
        self.checkPlayerCollision(player, camera)
        self.drawFood(camera)


    def createStartingThings(self, cam, player):
        for i in range(0, Constants.STARTINGFOODS):
            posx = random.randint(int(-Constants.WINDOWWIDTH/2), int(Constants.WINDOWWIDTH/2))
            posy = random.randint(int(-Constants.WINDOWHEIGHT/2), int(Constants.WINDOWHEIGHT/2))
            surfx, surfy = self.surface.converttoscreencoords((posx, posy), cam)
            thingcreated = Food(posx, posy, surfx, surfy, cam.scale)
            if not self.collidewithotherthings(thingcreated.model):
                if not thingcreated.model.colliderect(player.model):
                    self.surface.foods.append(thingcreated)
                    print('created object at (' + str(thingcreated.position[0]) + ', ' + str(thingcreated.position[1]) + ')')


    def updatefoodposition(self, cam):

        for t in self.surface.foods:
            thingx, thingy = self.surface.converttoscreencoords(t.position, cam)

            t.model.topleft = (thingx, thingy)


    def updatefoodscale(self, cam):

        for t in self.surface.foods:
            t.model.width *= cam.scale
            t.model.height *= cam.scale


    def checkPlayerCollision(self, player, camera):
        for thing in self.surface.foods:
            if player.scaledmodel.colliderect(thing.model):
                self.surface.foods.remove(thing)
                player.model = player.model.inflate(Constants.PLAYERINFLATION, Constants.PLAYERINFLATION)
                camera.extendrange(1.01)
                player.scaleplayer(camera.scale)


    def collidewithotherthings(self, rect):
        for obj in self.surface.foods:
            if rect.colliderect(obj.model):
                return True
        return False


    def randomOffCameraPos(self, camera):

        randx = random.randint(camera.position[0] - camera.xrange, camera.position[0] + camera.xrange)
        randy = random.randint(camera.position[1] - camera.yrange, camera.position[1] + camera.yrange)

        return randx, randy


    def addThingsRandomly(self, cam):

        self.updatefoodposition(cam)

        while len(self.surface.foods) <= Constants.MAXFOODQUANTITY:
            x, y = self.randomOffCameraPos(cam)
            surfx, surfy = self.surface.converttoscreencoords((x, y), cam)
            tempfood = Food(x, y, surfx, surfy, cam.scale)
            if not self.collidewithotherthings(tempfood.model):
                if not tempfood.model.colliderect(self.surface.CAMERARECT):
                    print('created object at (' + str(x) + ', ' + str(y) + ')')
                    self.surface.foods.append(tempfood)
                else:
                    print('no object created at (' + str(x) + ', ' + str(y) + ')')
            else:
                print('object collided with another, could not create')



    def removeThings(self, cam):

        camx, camy = self.surface.converttoscreencoords(cam.position, cam)

        thingrectrange = pygame.Rect((camx - Constants.WINDOWWIDTH, camy - Constants.WINDOWHEIGHT), (Constants.WINDOWWIDTH*2, Constants.WINDOWHEIGHT*2))

        for obj in self.surface.foods:
            objx, objy = self.surface.converttoscreencoords(obj.position, cam)
            if not thingrectrange.collidepoint((objx, objy)):
                self.surface.foods.remove(obj)


    def drawFood(self, cam):

        for t in self.surface.foods:
            self.updatefoodposition(cam)

            scaledmodel = deepcopy(t.model)

            scaledmodel.width *= cam.scale
            scaledmodel.height *= cam.scale

            pygame.draw.rect(self.surface.DISPLAYSURFACE, t.COLOR, scaledmodel)
