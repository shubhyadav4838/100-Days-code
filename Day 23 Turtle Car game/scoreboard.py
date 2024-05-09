from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 1
        self.goto(-225,260)
        self.write(f"Level:{self.score}", align = "center", font=FONT)
        self.color("black")

    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f"Level:{self.score}", align = "center", font=FONT)
        