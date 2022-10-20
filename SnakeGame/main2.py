from turtle import Screen
from score import ScoreBoard
from food import Food
from snake import Snake
Screen().setup(width=600, height=600)
Screen().bgcolor('black')
Screen().tracer(0)
Screen().title("Python's Python")
Screen().listen()

score_total = 0
snake = Snake()
snake.make_a_snake()
food = Food()
score = ScoreBoard()
score.vis()

Screen().onkey(fun=snake.up, key='Up')
Screen().onkey(fun=snake.down, key='Down')
Screen().onkey(fun=snake.left, key='Left')
Screen().onkey(fun=snake.right, key='Right')

with open("data.txt") as data:
    high_score = int(data.read())

is_game_on = True
score.write(arg=f"Score: {score_total}  High Score: {high_score}", align="center", font=("Times New Roman", 12, 'normal'))

while is_game_on:
    snake.forward()

    if snake.segment[0].distance(food) < 15:
        score_total += 1
        score.clear()
        score.write(arg=f"Score: {score_total}  High Score: {high_score}", align="center", font=("Times New Roman", 12, 'normal'))
        snake.extend()
        food.refresh()
    if snake.segment[0].xcor() > 290 or snake.segment[0].xcor() < -290 or snake.segment[0].ycor() > 290 or snake.segment[0].ycor() < -290:
        # is_game_on = False
        #score.reset()
        if score_total > high_score:
            high_score = score_total
            with open("data.txt", mode='w') as data:
                data.write(f"{score_total}")
        snake.reset()
        score_total = 0
        score.clear()
        score.write(arg=f"Score: {score_total}  High Score: {high_score}", align="center",
                    font=("Times New Roman", 12, 'normal'))
    new_list = snake.segment[1:]
    for segment in new_list:
        if snake.segment[0].distance(segment) < 10:
            # is_game_on = False
            #score.reset()
            if score_total > high_score:
                high_score = score_total
                with open("data.txt", mode='w') as data:
                    data.write(f"{score_total}")
            snake.reset()
            score_total = 0
            score.clear()
            score.write(arg=f"Score: {score_total}  High Score: {high_score}", align="center",
                        font=("Times New Roman", 12, 'normal'))
Screen().exitonclick()


