from turtle import Turtle, Screen
import time
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
Starting_Pos = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segment = []
        #self.head = self.segment[0]

    def make_a_snake(self):
        for position in Starting_Pos:
            self.add_segment(position)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.make_a_snake()


    def add_segment(self, position):
        kachu = Turtle()
        kachu.shape('square')
        kachu.color('white')
        kachu.penup()
        kachu.goto(position)
        self.segment.append(kachu)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def forward(self):
        Screen().update()
        time.sleep(0.1)
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.segment[0].forward(20)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(90)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(270)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(0)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(180)
