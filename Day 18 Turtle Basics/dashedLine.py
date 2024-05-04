# Task is to create the dashed line 
from turtle import Turtle , Screen

tim = Turtle()
tim.shape("turtle")
tim.color('red')
for _ in range(10):
     tim.forward(10)
     tim.penup() # This is so that the pen doesn't go down every time we move forward.
     tim.forward(10)
     tim.pendown()


screen = Screen()
screen.exitonclick()