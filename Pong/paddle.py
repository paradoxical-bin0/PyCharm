from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()

    def make_a_paddle(self, position):
        self.shape('square')
        self.speed('fastest')
        self.hideturtle()
        self.color('coral')
        self.shapesize(stretch_wid=1, stretch_len=5, outline=None)
        self.penup()
        self.goto(position)
        self.left(90)
        self.showturtle()

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)






