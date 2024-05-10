from turtle import Turtle 
ALIGNMENT = "center"
FONT = ("Arial",24,"normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.goto(0,265)
        self.high_score = 0
        self.read_the_file()
        self.penup()
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)
        self.hideturtle()
    
    
    
    def  update_scoreboard(self):
        self.clear()
        self.read_the_file()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)
        
        
        
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
        


    def reset(self):
        if self.score > self.high_score:
            with open("100 Days code/Day 24 Highscore addition/Snake Game/data.txt","w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()
    
    def read_the_file(self):
        with open("100 Days code/Day 24 Highscore addition/Snake Game/data.txt","r") as file:
            self.high_score= int(file.read())  
    