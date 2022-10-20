from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-190, 255)
        self.color('white')
        self.write(arg=f"Level : {self.level}", align="center", font=FONT)

    def level_up_score(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level : {self.level}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(-150, 255)
        self.color('blue')
        self.write(arg=f"Final Level : {self.level}", align="center", font=FONT)




