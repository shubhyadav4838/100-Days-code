from turtle import Turtle
import random

class Snake_Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5,stretch_wid=.5)
        self.color("Blue")
        self.speed("fastest")
        self.refresh() 
         
        
    def refresh(self):
        random_x  = random.randint(-270, 270)
        random_y  = random.randint(-270, 270)
        self.goto(random_x, random_y)
        
    

      
    