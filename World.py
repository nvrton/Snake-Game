from Window import *
from Objects import *
import time

HEIGHT = WIDTH = 800
LEFT = WIDTH * -0.5
RIGHT = WIDTH * 0.5
TOP = HEIGHT * 0.5
BOTTOM = HEIGHT * -0.5

class Game:
    def __init__(self):
        self.window = Window(WIDTH, HEIGHT)
        self.snake = Snake()
        self.food = Food()
        self.window.drawHUD(score=0, highScore=0)
        self.player_score = 0
        self.high_score = 0

    def RunGame(self):
        while True:
            self.window.screen.update()
            self.keyboardlistener()
            self.snake.update()

            self.food.update()

            self.world_update()

            time.sleep(0.1)
            
    def keyboardlistener(self):
        self.window.screen.listen()
        self.window.screen.onkey(self.snake.go_up, "Up")
        self.window.screen.onkey(self.snake.go_down, "Down")
        self.window.screen.onkey(self.snake.go_right, "Right")
        self.window.screen.onkey(self.snake.go_left, "Left")
        
    def world_update(self):
        if self.snake.snake_head.distance(self.food.item) < 15:
            self.food.set_move(True)
            self.snake.grow()
            self.player_score += 10
            ## PROBLEM 2 ##
            if self.player_score > self.high_score:
                self.high_score = self.player_score 
                self.window.drawHUD(score=self.player_score, highScore=self.high_score)
            else:
                self.window.drawHUD(score=self.player_score, highScore=self.high_score) 
            

        condition1 = self.snake.snake_head.xcor() > RIGHT
        condition2 = self.snake.snake_head.xcor() < LEFT
        condition3 = self.snake.snake_head.ycor() > TOP
        condition4 = self.snake.snake_head.ycor() < BOTTOM

        if condition1 or condition2 or condition3 or condition4:
            time.sleep(1)
            self.snake.snake_die()
            # self.snake.snake_head.goto(0, 0)
            # self.snake.snake_head.direction = "stop"
            # self.snake.clear_body()
            ## PROBLEM 1 ##
            self.player_score = 0 
            self.window.drawHUD(self.player_score, self.high_score) 
        if self.snake.head_and_body_coll_check() == True:
            time.sleep(1)
            self.snake.snake_die()
            # self.snake.snake_head.goto(0, 0)
            # self.snake.snake_head.direction = "stop"
            # self.snake.clear_body()
            ## PROBLEM 1 ##
            self.player_score = 0 
            self.window.drawHUD(self.player_score, self.high_score) 
game = Game()
game.RunGame()
