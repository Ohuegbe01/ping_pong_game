# create a paddle class inheriting the turtle class
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        self.position = position
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(1, 4)
        self.setheading(90)
        self.penup()
        self.goto(position)

    def move_up(self):
        self.setheading(90)
        self.forward(10)

    def move_down(self):
        self.backward(10)

