import pygame, random, sys

from assets.enemyai import Enemy
from util import Colors, Constants

class Enemycontroller:


    def __init__(self, surface):
        self.surface = surface


    def run(self, player, cam):
        self.removeenemies(cam)
        self.generateenemy(player, cam)
        self.moveenemies(player)
        self.checkcollisions(player, cam)
        self.updateenemyposition(cam)
        self.drawenemies()


    def collidewithotherthings(self, rect):
        for obj in self.surface.foods:
            if rect.colliderect(obj.model):
                return True
        for obj in self.surface.enemies:
            if rect.colliderect(obj.model):
                return True
        return False

    #to do actual actions on collision, not just to check
    #food collisions done in foodhandler.py
    def checkcollisions(self, player, camera):
        for obj in self.surface.enemies:
            if obj.scaledmodel.colliderect(player.scaledmodel):

                #the player collision
                if player.model.width >= obj.model.width:
                    self.surface.enemies.remove(obj)
                    player.model = player.model.inflate(Constants.PLAYERINFLATION, Constants.PLAYERINFLATION)
                    camera.extendrange(1.01)
                    self.surface.scaleassets(camera, player)
                '''else:
                    sys.exit()'''

            else:
                enemyit = iter(self.surface.enemies)
                for otherobj in enemyit:
                    if otherobj == obj:
                        next(enemyit, None)
                    elif obj.scaledmodel.colliderect(otherobj.scaledmodel):

                        if otherobj.model.width >= obj.model.width:
                            try:
                                self.surface.enemies.remove(obj)
                            except ValueError:
                                pass
                            otherobj.model = otherobj.model.inflate(Constants.PLAYERINFLATION, Constants.PLAYERINFLATION)
                            otherobj.scaledmodel = otherobj.model
                        else:
                            self.surface.enemies.remove(otherobj)
                            obj.model = obj.model.inflate(Constants.PLAYERINFLATION, Constants.PLAYERINFLATION)
                            obj.scaledmodel = obj.model


    def generateenemy(self, player, cam):
        while len(self.surface.enemies) <= Constants.MAXENEMIES:
            x, y = self.randomOffCameraPos(cam)
            surfx, surfy = self.surface.converttoscreencoords((x, y), cam)
            tempenemy = Enemy(player.model.width, x, y, surfx, surfy)
            if not self.collidewithotherthings(tempenemy.model):
                if not tempenemy.model.colliderect(self.surface.CAMERARECT):
                    print('created enemy at (' + str(x) + ', ' + str(y) + ')')
                    self.surface.enemies.append(tempenemy)
                else:
                    print('no enemy created at (' + str(x) + ', ' + str(y) + ')')
            else:
                print('enemy collided with something, could not create')


    def removeenemies(self, cam):

        camx, camy = self.surface.converttoscreencoords(cam.position, cam)

        thingrectrange = pygame.Rect((camx - cam.xrange*2, camy - cam.yrange*2), (cam.xrange * 6, cam.yrange * 6))

        for obj in self.surface.enemies:
            if not thingrectrange.colliderect(obj.model):
                self.surface.enemies.remove(obj)


    def drawenemies(self):
        for enemy in self.surface.enemies:
            pygame.draw.rect(self.surface.DISPLAYSURFACE, Colors.enemycolorlist['red'], enemy.scaledmodel)


    def moveenemies(self, player):
        for enemy in self.surface.enemies:
            enemy.searchandmove(player, self.surface.enemies, self.surface.foods)
            enemy.move()


    def updateenemyposition(self, cam):
        for enemy in self.surface.enemies:
            x, y = self.surface.converttoscreencoords(enemy.position, cam)
            enemy.model.center = (x, y)
            enemy.scaledmodel.center = enemy.model.center


    def randomOffCameraPos(self, camera):

        randx = random.randint(camera.position[0] - camera.xrange, camera.position[0] + camera.xrange)
        randy = random.randint(camera.position[1] - camera.yrange, camera.position[1] + camera.yrange)

        return randx, randy