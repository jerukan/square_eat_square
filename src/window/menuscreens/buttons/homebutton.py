from window.menuscreens.buttons.button import Button

class Homebutton(Button):

    def __init__(self):
        Button.__init__(self, 300, 300, 200, 160, "main menu")


    def onClick(self, mouseclickposition):
        if self.isclicked(mouseclickposition):
            return "home"
        return None