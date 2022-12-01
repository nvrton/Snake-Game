import turtle 
from Window import *
from Objects import *
import time

HEIGHT = WIDTH = 800

class Game:
    def __init__(self):
        self.window = Window(WIDTH, HEIGHT)
        self.snake = Snake()
        self.food = Food()

    def RunGame(self):
        while True:
            self.window.screen.update()
            self.keyboardlistener()
            self.snake.move()
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
        
game = Game()
game.RunGame()
