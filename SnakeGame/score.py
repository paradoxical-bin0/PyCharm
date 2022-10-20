from turtle import Turtle


class ScoreBoard(Turtle):
    # def __init__(self):
    #     super().__init__()
    #     with open("data.txt") as data:
    #         self.high_score = int(data.read())

    def vis(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)


    #def reset(self):
        #if score_total > self.high_score:
         #   self.high_score = score_total


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg='GAME OVER!', align="center", font=("Times New Roman", 12, 'normal'))

