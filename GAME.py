import turtle
from turtle import Turtle,mainloop,listen,onkeypress,tracer,Vec2D,bgcolor,Screen
from random import choice,randint


from paddle import Paddle
from ball import Ball
from target import Target
class Game:
    tx, ty = -250, 300
    dy = 1
    dx = choice([-.5, .5])
    targets = []

    def __init__(self):
        tracer(0)
        for _ in range(8):
            for _ in range(10):
                target = Target(self.tx, self.ty)
                self.targets.append(target)
                self.tx += 55
            self.ty -= 25
            self.tx = -250
        tracer(1)

