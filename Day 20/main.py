import time
from turtle import Turtle, Screen
import random

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake game")

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)
        time.sleep(0.1)

