from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('pong game')
screen.tracer(0)

Lpaddle = Paddle(-350)
Rpaddle = Paddle(350)

ball = Ball()






screen.listen()
screen.onkey(Rpaddle.go_up, 'Up')
screen.onkey(Rpaddle.go_down, 'Down')
screen.onkey(Lpaddle.go_up, 'w')
screen.onkey(Lpaddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce back
        ball.bounce()



        
screen.exitonclick()
