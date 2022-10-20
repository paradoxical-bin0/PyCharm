from turtle import Turtle, Screen
from paddle import Paddle
from score import ScoreBoard
from ball import Ball
import time
Screen().setup(width=800, height=600)
Screen().bgcolor('black')
Screen().title("3.14Pong")
Screen().listen()
Screen().tracer(0)
score1 = 0
score2 = 0
mid_line = Turtle()
mid_line.penup()
mid_line.goto(x=0, y=-300)
mid_line.left(90)
mid_line.color('white')
mid_line.hideturtle()
mid_line.speed('fastest')
while mid_line.ycor() < 270:
    mid_line.pendown()
    mid_line.forward(20)
    mid_line.penup()
    mid_line.forward(20)

paddle1 = Paddle()
paddle1.make_a_paddle(position=(370, 0))
paddle2 = Paddle()
paddle2.make_a_paddle(position=(-370, 0))
score = ScoreBoard()
score.vis()
score.write(arg=f"{score1}:{score2}", align="center", font=("Times New Roman", 15, 'normal'))
ball = Ball()
ball.vis()


Screen().onkey(fun=paddle1.up, key='Up')
Screen().onkey(fun=paddle1.down, key='Down')
Screen().onkey(fun=paddle2.up, key='U')
Screen().onkey(fun=paddle2.down, key='D')
game_is_on = True
while game_is_on:
    time.sleep(ball.speed_up)
    Screen().update()
    ball.move()
    # Detect collision with walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() < -420:
        ball.reset()
        ball.change_dir()
        score1 += 1
        score.clear()
        score.write(arg=f"{score2}:{score1}", align="center", font=("Times New Roman", 15, 'normal'))
    elif ball.xcor() > 420:
        ball.reset()
        score2 += 1
        score.clear()
        score.write(arg=f"{score2}:{score1}", align="center", font=("Times New Roman", 15, 'normal'))

Screen().exitonclick()
