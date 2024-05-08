from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time




screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0)) 
ball = Ball()
score = Scoreboard() 
    

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # Detect collision with ball
    if ball.ycor() >285 or ball.ycor()< -285:
        ball.bounce_y()
        
    # To Detect collision with r_paddle
    if ball.distance(r_paddle) <60 and ball.xcor() >320 or ball.distance(l_paddle) <60 and ball.xcor() <-320:
        ball.bounce_x()
    
    # Detect R paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()
    
    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
    
    



screen.exitonclick()