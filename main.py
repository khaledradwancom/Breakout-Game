import time
from turtle import Screen
from turtle import Turtle,mainloop,listen,onkeypress,tracer,Vec2D,bgcolor
import paddle
from ball import Ball
from paddle import Paddle
from target import Target
from GAME import Game
from score import Scoreboard

score = Scoreboard()
tx, ty = -250, 300
target = Target(tx, ty)

screen = Screen()
screen.tracer(0)
screen.screensize(600, 600)
screen.bgcolor('black')
screen.title('breakout game')
ball = Ball()
c_padle = Paddle((0, -350))

game = Game()

screen.listen()
screen.onkey(c_padle.a, 'Left')
screen.onkey(c_padle.d, 'Right')
khaled = True
while khaled:

    time.sleep(ball.faster)
    screen.update()
    ball.ball_move()

    if ball.ycor() > 380:
        ball.byounce()
    elif ball.xcor() < -440 or ball.xcor() > 440:
        ball.by2()

    elif ball.distance(c_padle) < 50:
        ball.byounce()
    elif ball.ycor() >= 100:
        for target in game.targets:
            if ball.ycor() >= target.ycor() - 25:
                if ball.xcor() >= target.xcor() - 25:
                    if ball.xcor() <= target.xcor() + 25:
                        ball.byounce()
                        target.color('black')
                        score.new_score()
                        target.white = True
                        break
    elif ball.ycor() < -450:
        khaled = False





screen.exitonclick()