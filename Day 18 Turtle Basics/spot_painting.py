import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


screen = t.Screen()
t.setup(width=800,height=800)
left_x = -370
left_y = 370


for _ in range(15):
    tim.penup()
    tim.goto(left_x,left_y)
    tim.pendown()

    for _ in range(15): 
        tim.dot(20,randomColor())
        tim.penup()
        tim.forward(50)
        tim.pendown()

    left_y -= 50


screen.exitonclick()