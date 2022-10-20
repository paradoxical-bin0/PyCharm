import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
lost_message = Turtle()
lost_message.hideturtle()
FONT = ("Courier", 24, "normal")
kachu = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()
screen.onkey(fun=kachu.up, key='Up')
score = Scoreboard()
car_manager = CarManager()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    if kachu.ycor() == 280:
        kachu.level_up_player()
        score.level_up_score()
        car_manager.speed_up()
    for car in car_manager.all_cars:
        if kachu.distance(car) < 20:
            lost_message.penup()
            lost_message.color('red')
            lost_message.write(arg=f"Oh No! You've crashed!", align="center", font=FONT)
            score.game_over()
            game_is_on = False


screen.exitonclick()
