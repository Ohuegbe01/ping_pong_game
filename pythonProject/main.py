# TODO 1. Create Screen
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong😎')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
# paddle = Turtle()
# paddle.shape('square')
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.color('white')
# paddle.penup()
# paddle.goto(350, 0)
#
screen.listen()


screen.onkey(r_paddle.up, key='Up')
screen.onkey(r_paddle.down, key='Down')
screen.onkey(l_paddle.up, key='w')
screen.onkey(l_paddle.down, key='s')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y_axis()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x_axis()
        print('made contact')
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()