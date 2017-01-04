class Constants:

#sizes are basically the width/height of the square

#window stuff
    WINDOWHEIGHT = 900
    WINDOWWIDTH = 900

    STARTINGFOODS = int((WINDOWHEIGHT * WINDOWWIDTH) / 130000)

    WINDOWCENTER = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))

#player stuff
    PLAYERSIZE = 100

    PLAYERMOVESPEED = 10

    PLAYERINFLATION = 10

    PLAYERNAME = 'kappa'

#enemy stuff
    MAXENEMIES = 3
    HUNTINGRANGE = 1000

#camera stuff
    CAMERASLACK = 280
    CAMERAMOVESPEED = 8

    PLAYERCAMSIZE = 100

#food stuff
    FOODMAXSIZE = int(PLAYERSIZE / 3)
    FOODMINSIZE = int(PLAYERSIZE / 6)

    MAXFOODQUANTITY = 20