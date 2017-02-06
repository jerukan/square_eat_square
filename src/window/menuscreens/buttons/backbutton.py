from window.menuscreens.buttons.button import Button

class Backbutton(Button):

    def __init__(self):
        Button.__init__(self, 30, 700, 200, 90, "back")


    def onClick(self, mouseclickposition):
        if self.isclicked(mouseclickposition):
            return "back"
        return None