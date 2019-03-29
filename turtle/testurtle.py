import turtle

class animate(object):
    def __init__(self):
        self.window = turtle.Screen()
        self.window.bgcolor("light grey")
        self.window.title("Turtle")

    def showWindow(self):
        skk = turtle.Turtle()
        skk.forward(100)
        turtle.done()

an = animate()
an.showWindow()
#turtle.done()