from turtle import Turtle

ALIGNMENT="center"
FONT=("Arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=0
        self.color("white")    
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Your score is : {self.score} High score : {self.highscore}",align=ALIGNMENT,font=FONT)
    def reset(self):
        if self.score>self.highscore:
            self.highscore = self.score
        self.score=0

    #def game_over(self):
      #  self.goto(0,0)
       # self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

        


        
        

    
