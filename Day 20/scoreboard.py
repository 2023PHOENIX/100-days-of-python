from turtle import Turtle

Aligment = 'center'
Font = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)

        self.hideturtle()

    def update_score(self):
        self.write(f"score: {self.score}", align=Aligment, font=Font)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=Aligment, font=Font)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
