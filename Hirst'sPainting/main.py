import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
colour_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
               (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
               (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
               (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
               (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
kachu = Turtle()
kachu.shape('turtle')
kachu.pensize(10)
kachu.hideturtle()
kachu.speed('fastest')
Screen().screensize(1600, 1600)


def row():
    for i in range(0, 10):
        colour = random.choice(colour_list)
        kachu.dot(20, colour)
        kachu.penup()
        kachu.forward(50)
        kachu.pendown()


def up_left():
    kachu.penup()
    kachu.left(90)
    kachu.forward(50)
    kachu.left(90)
    kachu.forward(50)


def up_right():
    kachu.penup()
    kachu.right(90)
    kachu.forward(50)
    kachu.right(90)
    kachu.forward(50)


for i in range(5):
    row()
    up_left()
    row()
    up_right()

Screen().exitonclick()


