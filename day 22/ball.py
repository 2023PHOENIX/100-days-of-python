from turtle import Turtle, Screen


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('blue')
        self.shape('circle')
        self.penup()
        self.xmove = 10
        self.ymove = 10


    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)


    def bounce(self):
        self.ymove *= -1

