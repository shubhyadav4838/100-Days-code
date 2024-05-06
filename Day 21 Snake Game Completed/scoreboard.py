from turtle import Turtle 
ALIGNMENT = "center"
FONT = ("Arial",24,"normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.goto(0,265)
        self.penup()
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)
        self.hideturtle()
        
    def game_over(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)
        self.goto(0,0)
        self.write(f"Game Over!", align = ALIGNMENT, font = FONT)
    
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)


