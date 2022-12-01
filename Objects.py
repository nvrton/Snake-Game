import turtle 
import random

class Snake:

    def __init__(self):
        self.snake_head = turtle.Turtle()
        self.snake_body = []
        self.InitialiseSnake()

    def InitialiseSnake(self):
        self.snake_head.speed(0)
        self.snake_head.shape("square")
        self.snake_head.color("black")
        self.snake_head.penup()
        self.snake_head.goto(0, 100)
        self.snake_head.direction = "stop"

    def move(self):
        for i in range(len(self.snake_body)-1, 0, -1):
            x = self.snake_body[i-1].xcor()
            y = self.snake_body[i-1].ycor()
            self.snake_body[i].goto(x, y)
        
        if self.snake_body != []:
            x = self.snake_head.xcor()
            y = self.snake_head.ycor()
            self.snake_body[0].goto(x, y)
            
        if self.snake_head.direction == "up":
            y = self.snake_head.ycor()
            self.snake_head.sety(y+20)
        if self.snake_head.direction == "down":
            y = self.snake_head.ycor()
            self.snake_head.sety(y-20)
        if self.snake_head.direction == "right":
            x = self.snake_head.xcor()
            self.snake_head.setx(x+20)
        if self.snake_head.direction == "left":
            x = self.snake_head.xcor()
            self.snake_head.setx(x-20)
            
    def go_up(self):
        if self.snake_head.direction != "down":
            self.snake_head.direction = "up"
    def go_down(self):
        if self.snake_head.direction != "up":
            self.snake_head.direction = "down"
    def go_right(self):
        if self.snake_head.direction != "left":
            self.snake_head.direction = "right"
    def go_left(self):
        if self.snake_head.direction != "right":
            self.snake_head.direction = "left"

    def grow(self):
        part = turtle.Turtle()
        part.speed(0)
        part.shape("square")
        part.color("black")
        part.penup()
        self.snake_body.append(part)

    def update(self):
        self.move()
    
    # def clear_body(self):
    #     for part in self.snake_body:
    #         part.goto(1000, 1000)
    #     self.snake_body = []

    def snake_die(self):
        self.snake_head.goto(0, 100)
        self.snake_head.direction = "stop"
        for part in self.snake_body:
            part.hideturtle()
        self.snake_body = []
        
    def head_and_body_coll_check(self):
        for part in self.snake_body:
            if part.distance(self.snake_head) < 20:
                print("head and body collision")
                return True

class Food:

    def __init__(self):
        self.item = turtle.Turtle()
        self.item.speed(0)
        self.item.shape("circle")
        self.item.color("red")
        self.item.penup()
        self.item.shapesize(0.50, 0.50)
        self.item.goto(0, 0)
        self.move = False

    def set_move(self, decision):
        self.move = decision

    def relocate(self):
        if self.move == True:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            self.item.goto(x,y)

            self.set_move(False)

    def update(self):
        self.relocate()
