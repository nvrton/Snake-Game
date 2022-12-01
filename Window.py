import turtle 

class Window:
    def __init__(self, width, height):
        self.screen = turtle.Screen()
        self.screen.title("OOP Snake")
        self.screen.bgcolor("green")
        self.screen.setup(width, height)
        self.screen.tracer(0)

        self.hud = turtle.Turtle()

    def drawHUD(self, score):
        self.hud.clear()
        self.hud.color("white")
        self.hud.penup()
        self.hud.hideturtle()
        self.hud.goto(0, 260)

        self.hud.write("Score: %d High Score: 0" %(score), align="center", font=("Courier", 22, "normal"))