from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color('black')
# timmy.forward(200)
# timmy.backward(100)
# timmy.left(90)
# timmy.forward(182)
# timmy.right(20)
# timmy.forward(227)


# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
#
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
import random

# sides = [3, 4, 5, 6, 7, 8, 9,10,11]
# colors = ['blue','red','green','pink','black']
# for side in sides:
#     Angle = (180 * (side - 2)) / side
#     for _ in range(side):
#         tim.forward(100)
#         tim.left(180 - Angle)
direction = [0, 90, 180, 270,360 ]
tim.pensize(15)
tim.speed(100)
for _ in range(200):
    tim.forward(100)
    tim.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
