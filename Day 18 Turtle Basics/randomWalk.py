import turtle as t
import random
tim = t.Turtle()
tim.shape("turtle")
t.colormode(255) # it is used to use the RGB color model

tim.width(5)
# colors = ["red", "orange","yellow", "green","blue","purple", "pink", "black"]
direction = [0,90,180,270]

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return  tim.pencolor(r,g,b)

def walk():
    randomColor()
    tim.setheading(random.choice(direction)) 
    tim.forward(25)
    

draw = True   
while draw:
    walk()
    

screen = t.Screen()
screen.exitonclick()