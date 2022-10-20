from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.speed_up = 0.1

    def vis(self):
        super().__init__()
        self.shape('circle')
        self.speed('fastest')
        self.color('red')
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.speed_up *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.speed_up = 0.1
        self.bounce_x()


