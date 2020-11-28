from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Input your choice")
colors = ['red', 'orange', 'pink', 'green', 'black', 'blue', 'grey']
y_pos = [-70, -40, -10, 20, 50, 80]

all_turtle = []

for turtle_index in range(len(colors) - 1):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True
import random

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! . Winning color {winning_color}")

            else:
                print(f"Winning color is {winning_color}")

        rand_dist = random.randint(0, 18)
        turtle.forward(rand_dist)

screen.exitonclick()
