import turtle 

class Window:
    def __init__(self, width, height):
        self.screen = turtle.Screen()
        self.screen.title("OOP Snake")
        self.screen.bgcolor("blue")
        self.screen.setup(width, height)
        self.screen.tracer(0)
