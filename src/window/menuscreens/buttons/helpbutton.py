from window.menuscreens.buttons.button import Button

class Helpbutton(Button):

    def __init__(self):
        Button.__init__(self, 30, 300, 200, 160, "help")


    def onClick(self, mouseclickposition):
        if self.isclicked(mouseclickposition):
            return "help"
        return None