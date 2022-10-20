import random
from turtle import Turtle, Screen
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
is_race_on = False
turtle_squad = []
y = -120
Screen().setup(width=500, height=400)
user_input = Screen().textinput(title="Make your Bet!🏁", prompt="Which turtle🐢 will win the race? Enter a colour: ")
for colour in colours:
    colour_kachu = Turtle(shape='turtle')
    colour_kachu.color(colour)
    colour_kachu.penup()
    colour_kachu.goto(x=-230, y=y)
    colour_kachu.speed('fastest')
    turtle_squad.append(colour_kachu)
    y += 45
if user_input:
    is_race_on = True
while is_race_on:
    for turtles in turtle_squad:
        if turtles.xcor() > 230:
            win_colour = turtles.pencolor()
            is_race_on = False
            if user_input == win_colour:
                print(f"You Win! The {win_colour} turtle won the race.")
            else:
                print(f"You lost! The {win_colour} turtle won the race.")
        random_dist = random.randint(0, 10)
        turtles.forward(random_dist)

Screen().exitonclick()

