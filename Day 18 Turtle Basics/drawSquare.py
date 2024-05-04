# Task is to create a square using the turtle module and the screen module.
from turtle import Turtle , Screen

myTurtle = Turtle()
myTurtle.shape("turtle")
myTurtle.color('green')

for i in range(4):
    myTurtle.forward(100)
    myTurtle.right(90)


screen = Screen()
screen.exitonclick()


