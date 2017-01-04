import math


class Functions:
    def getdistance(self, startx_starty, endx_endy):
        sx, sy = startx_starty
        ex, ey = endx_endy

        return math.sqrt((sx - ex) ** 2 + (sy - ey) ** 2)


    def closestobjectfromlist(self, object, thinglist):

        prevdistance = 0
        output = 0
        for thing in thinglist:
            if object == thing:
                pass
            dist = self.getdistance(object.position, thing.position)
            prevdistance = dist
            if thinglist.index(thing) == 0:
                output = thing
            elif dist < prevdistance:
                output = thing
        return output
