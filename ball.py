from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('white')
        self.n_x = 10
        self.n_y = 10
        self.speeed = ['slowest', 'slow', 'normal', 'fast', 'fastest']
        self.call = 0
        self.faster = 0.1

    def ball_speed(self):
        self.speed(self.speeed[self.call])
        self.call += 1
        if self.call == 4:
            return False

    def ball_move(self):
        new_1x = self.xcor() + self.n_x
        new_1y = self.ycor() + self.n_y
        self.goto(new_1x, new_1y)

    def byounce(self):
        self.n_y *= -1
        self.faster *= 0.9

    def by2(self):
        self.n_x *= -1

    def recet_ball(self):
        self.goto(0, 0)
        self.by2()
        self.faster = 0.05
