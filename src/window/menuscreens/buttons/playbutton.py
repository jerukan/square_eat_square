from window.menuscreens.buttons.button import Button

class Playbutton(Button):

    def __init__(self):
        Button.__init__(self, 30, 100, 200, 160, "PLAY")


    def onClick(self, mouseclickposition):
        if self.isclicked(mouseclickposition):
            return "game"
        return None

