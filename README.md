##
The code for the four PowerPoints is in the three seperate Python Files, followed exactly as said (when correct). If the PowerPoints remove a section of code and rewrite it (for example, the sections upon snake death) 
then the old code has been commented and new code placed in. 

Following the PowerPoints exactly doesn't seem to produce a working program, so follow the tips outlined below if things aren't working. You may not get some of these issues, but if you do then the solutions are here. 

The fourth PowerPoint outlines two things to fix at the end, these are labelled as Problem 1 and 2 below and have ##PROBLEM X## above them in the code to identify where they are. 
## 

Tips to follow the PowerPoint

- Read the PowerPoint. Tempting to just copy code, but saves so much time and effort if you just follow the PowerPoint. 
- First PowerPoint has the completed code in the last slide. When they get to a point where the code you've written is correct, but nothing runs, check these and find the section that actually runs the code in the World file at bottom of Game class. It doesn't tell you to include it. 
- The OOP structure at the start of each PowerPoint is a golden ticket to understanding. It shows exactly where every function you write is meant to go. It sometimes isn't clear.
- PowerPoint two, you need to put  the snake_body array in the Snake class, under __innit__ function. 
- penup() is a turtle command meaning lift the pen up, i.e. when the turtle moves it won't draw behind it. Removing this line of code will leave a line behind anything when it moves. 
- If HUD does not spawn in upon window launching, and only happens after first points scored you need to make sure you actually include self.window.drawHUD(score=0, highScore=0) in your Game class __init__ (high score section only applicable after following powerpoint and hints all the way through)
- To update score each time food is eaten, rewrite the HUD after every time the score increases by 10, under self.player_score += 10 in the world_update() function
- In Food class __init__ set self.move to True and on the next line run self.relocate() if every time you spawn in the food is in the middle, and collision with it kills the snake. Do not ask how this fixes the issue, but it does. Will randomly place the food somewhere on map and it does not act as a part of the snake. 
- To stop a body part appearing in middle of screen have def __init__ in Food class contain self.item = turtle.Turtle() and self.InitialiseFood, and then a new function containing the code. 
along with placing: 
        for i in range(len(self.snake_body)-1, 0, -1):
            x = self.snake_body[i - 1].xcor()
            y = self.snake_body[i - 1].ycor()

            self.snake_body[i].goto(x, y)
at bottom of def grow() in snake class. The body part still appears in centre of screen on the first eat, but otherwise works. 

If anyone ever fixes this properly ^^ or finds better solutions, get in touch: 16nethertonj@student.cleeveschool.net


PROBLEMS SOLVED (end of ppt 4)

(##PROBLEM 1##) 1- To reset the score to zero whenever user dies, put self.player_score = 0 and redraw the hud, setting score perameter to self.player_score (line of code should be: self.window.drawHUD(self.player_score)) in both conditions of death function.


(##PROBLEM 2##) 2- FROM:  self.hud.write(("Score:  %d High Score: 0" %(score), align="center", font=("Courier", 22, "normal")) ---->> TO:  self.hud.write(("Score:  %d High Score: %d" %(score, highScore)), align="center", font=("Courier", 22, "normal")) in Window class
- if self.player_score > self.high_score:
    self.high_score = self.player_score 
    self.window.drawHUD(score=self.player_score, highScore=self.high_score)
  else:
    self.window.drawHUD(score=self.player_score, highScore=self.high_score) 

^^^ in world_update() function in Game class. If the players score is higher than the highscore, set the high score to that value, if it isn't then don't change the high score.
You do not need to reset this score to 0 at any point, i.e. after death, as it is the high score so far, including previous rounds. 
this one was tricky ^^ (blessed be github code pilot)
MAKE SURE THAT EVERY TIME YOU WRITE THE HUD, YOU INCLUDE highScore IN THE PERAMETER LIST
