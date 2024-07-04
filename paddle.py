from turtle import Turtle,mainloop,listen,onkeypress,tracer,Vec2D,bgcolor,Screen
from random import choice,randint

screen = Screen()


class Paddle(Turtle):
    colors = ['green', 'orange', 'yellow', 'pink', 'purple', 'gold', 'gray', 'brown', 'white']
    def __init__(self, position):

        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=10, stretch_wid=1)
        self.color(choice(self.colors))
        self.goto(position)
        self.speed('fast')


    def a(self):
        new_y = self.xcor() - 35
        self.goto(new_y, self.ycor())

    def d(self):
        new_y = self.xcor() + 35
        self.goto(new_y, self.ycor())

