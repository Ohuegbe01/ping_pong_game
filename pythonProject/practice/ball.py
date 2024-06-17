# import random
from turtle import Turtle
import random

random_x = [-380, 380]
random_y = random. randint(-280, 280)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.shape('circle')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_x(self):
        self.penup()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # self.penup()
        self.y_move *= -1

    def bounce_x(self):
        # self.penup()
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed -= 0.01
        self.bounce_x()

