from window.menuscreens.screen import Screen
from window.menuscreens.buttons import *

class Helpscreen(Screen):

    def __init__(self):
        Screen.__init__(self, Backbutton())


    def displayscreen(self, surface, mousehoverposition):
        self.drawText("HOW TO PLAY", 450, 50, surface, 36)
        self.drawText('''move around using wasd, eat stuff''', 450, 120, surface, 28)
        for button in self.buttonlist:
            button.displaybutton(surface, mousehoverposition)