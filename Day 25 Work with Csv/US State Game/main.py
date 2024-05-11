import turtle
import pandas as pd
from states import States


image ="100 Days code/Day 25 Work with Csv/US State Game/blank_states_img.gif"
screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(image)
turtle.shape(image)
screen.setup(740,515)



state = States()

ask_questions = True

while ask_questions:
    answer_state = screen.textinput(title = f"{state.score_in_game}/50 States Correct", prompt = "What's another state name")
    if state.check_the_input(answer_state):
        state.get_cordinates(answer_state)
        state.write_the_name(answer_state)
        
        
    state.check_repeat(answer_state)
        
        
    if state.score_in_game == 50:
        ask_questions = False


