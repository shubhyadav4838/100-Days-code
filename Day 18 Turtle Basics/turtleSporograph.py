import turtle as t
import random
tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)
tim.speed("fastest")

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
    

for _ in range(int(360/7)):
    tim.color(randomColor())
    tim.circle(100)
    tim.right(7)



screen = t.Screen()
screen.exitonclick()