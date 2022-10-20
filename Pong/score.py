from turtle import Turtle


class ScoreBoard(Turtle):

    def vis(self):
        super().__init__()
        self.color('yellow')
        self.speed('fastest')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER!', align="center", font=("Times New Roman", 17, 'normal'))


