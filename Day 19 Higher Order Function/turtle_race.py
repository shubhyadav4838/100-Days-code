from turtle import Turtle , Screen 
import random

is_race_on = False
screen = Screen()
screen.setup(width = 600 , height = 500)
user_bet = screen.textinput(title = "Make a bet", prompt = "which turtle is going to will the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
cordinate_y = -140

all_turtle = []

for turtle_index in range(6):
    new_turtle = Turtle(shape = 'turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-290,cordinate_y)
    all_turtle.append(new_turtle)
    cordinate_y+=60
    
if user_bet:
    is_race_on = True
    
while is_race_on:
        
    for turtle in all_turtle:
        if turtle.xcor() >270:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet.lower():
                print("Hurray! You won the race")
            else:
                print(f"You LOSS! {winning_color} is the winner of this race")
            break
        turtle.forward(random.randint(0,10))
        
screen.exitonclick() 
    
    


