from turtle import Turtle
import pandas as pd
ALIGNMENT = "center"
FONT = ("Arial",10,"normal")

FILE_PATH = "100 Days code/Day 25 Work with Csv/US State Game/50_states.csv"

class States(Turtle):
    
    def __init__(self):
        super().__init__()
        self.data = pd.read_csv(FILE_PATH)
        self.x_cor = 0
        self.y_cor = 0
        self.state_name = self.data["state"]
        self.score_in_game = 0
        self.input_names = []
        
        
        
        
    def get_cordinates(self,input_name):
        
        for name in self.state_name:
            if name==input_name.capitalize():
                state_data = self.data[self.data["state"] == input_name.capitalize()]
                self.x_cor = state_data.x
                self.y_cor = state_data.y
     
    def check_the_input(self, answer):
        for name in self.state_name:
            if name==answer.capitalize():
                self.input_names.append(name)
                return True 
            
    def write_the_name(self,input_name):
        self.penup()
        self.hideturtle()
        self.goto(int(self.x_cor), int(self.y_cor))
        self.color("Black")
        self.write(f"{input_name.capitalize()}", align = ALIGNMENT, font = FONT)
    
        
    def check_repeat(self,answer):
        num = self.input_names.count(answer.capitalize())
        if num==1:
           self.score_in_game +=1
        