from window.menuscreens.screen import Screen
from window.menuscreens.buttons import *

class Gameoverscreen(Screen):

    def __init__(self):
        Screen.__init__(self, Homebutton())


    def displayscreen(self, surface, mousehoverposition):
        self.drawText("GAME OVER", 450, 30, surface, 48)
        for button in self.buttonlist:
            button.displaybutton(surface, mousehoverposition)