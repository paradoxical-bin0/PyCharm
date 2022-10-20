import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)


def spiro():
    for i in range(0, 361):
        kachu.left(i)
        change_colour()
        kachu.circle(50, 360, None)


def change_colour():
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    colour_tuple = (r, g, b)
    kachu.pencolor(colour_tuple)
# colours = ["black", "navy", "dark green", "maroon", "indigo", "deep pink", "gold", "cyan", "coral", "orange red"
#     , "light steel blue", "pale green", "indian red", "spring green", "light slate gray", "dodger blue",
#       "teal", "thistle", "rosy brown", "saddle brown"]


degree = [0, 90, 180, 270, 360]


def random_walk():
    for _ in range(0, 50):
        change_colour()
        kachu.forward(random.randint(0, 51))
        kachu.setheading(random.choice(degree))


def turn_left():
    kachu.left(90.0)
    kachu.forward(100)
    # kachu.forward(10), kachu.back(10), kachu.left(float((random.randint(0,360))),
    # kachu.right(float(random.randint(0, 360)))


def square():
    kachu.forward(100)
    turn_left()
    turn_left()
    turn_left()


def dashed_line():
    kachu.forward(10)
    kachu.penup()
    kachu.forward(10)
    kachu.pendown()


def shape(side):
    turn_angle = 360/side
    kachu.forward(100)
    for i in range(side-1):
        kachu.left(turn_angle)
        kachu.forward(100)
    kachu.left(turn_angle)


kachu = Turtle()
kachu.shape("turtle")
kachu.color("dark slate blue")
kachu.speed("fastest")
#kachu.pensize(10)
spiro()
Screen().exitonclick()





