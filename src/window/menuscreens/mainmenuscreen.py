from window.menuscreens.screen import Screen
from window.menuscreens.buttons import *

class Mainmenuscreen(Screen):

    def __init__(self):
        Screen.__init__(self, Playbutton())


    def displayscreen(self, surface, mousehoverposition):
        self.drawText("SQUARE EAT SQUARE", 450, 20, surface)
        for button in self.buttonlist:
            button.displaybutton(surface, mousehoverposition)