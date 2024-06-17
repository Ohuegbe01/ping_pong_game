import random
from turtle import Turtle
x_random = random.randint(-400, 400)
y_random = random.randint(-300, 300)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        # self.goto(350, 270)
        # self.move_ball()

    def move_ball(self):
        # self.goto(x_random, y_random)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y_axis(self):
        # self.x_move *= -1
        self.y_move *= -1

    def bounce_x_axis(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        # self.y_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x_axis()
