from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def level_up_player(self):
        self.goto(STARTING_POSITION)



