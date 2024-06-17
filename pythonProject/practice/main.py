# import the required items
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


screen = Screen()
screen.setup(width=800, height=600)

screen.tracer(0)
# game_still_on = True


# create two more turtles
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
time.sleep(0.01)
# ball.move_x()
score = Score()

# move objects
screen.listen()
screen.onkey(fun=l_paddle.move_up, key='w')
screen.onkey(fun=l_paddle.move_down, key='s')
screen.onkey(fun=r_paddle.move_up, key='Up')
screen.onkey(fun=r_paddle.move_down, key='Down')

screen.bgcolor('black')

game_still_on = True
while game_still_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_x()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    if ball.xcor() > 380:
        score.l_score()
        ball.reset_position()
    if ball.xcor() < -380:
        score.r_score()
        ball.reset_position()
screen.exitonclick()
