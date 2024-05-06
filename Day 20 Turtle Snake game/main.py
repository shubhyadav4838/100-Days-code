from turtle import Screen , Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width = 600 , height = 600) # width and height of the screen in pixels 
screen.bgcolor("black") # background color of the screen
screen.title("My Snake Game")
screen.tracer(0) 

snake = Snake()
screen.listen() # To listen for key strokes
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
   
game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    
    snake.move()
    
screen.exitonclick()