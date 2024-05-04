# Task is to draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon .All the shapes are in different colors
from turtle import Turtle,Screen
tim = Turtle()
tim.shape("turtle")
colors = ["red", "orange","yellow", "green","blue","purple", "pink", "black"]
sides = 3
total_angle = 360


draw = True
while draw:
    per_angle = total_angle/sides
    for line in range(sides):
        tim.color(colors[sides-3])
        tim.forward(100)
        tim.right(per_angle)
    sides+=1
    if sides==10:
        draw = False
    

screen = Screen()
screen.exitonclick()

