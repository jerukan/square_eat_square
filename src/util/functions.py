import math

class Functions:

    def getdistance(self, startx_starty, endx_endy):
        sx, sy = startx_starty
        ex, ey = endx_endy

        return math.sqrt((sx-ex)**2 + (sy-ey)**2)