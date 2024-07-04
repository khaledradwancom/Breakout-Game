from turtle import Turtle
import random


class Scoreboard(Turtle):
    def __init__(self):
        self.player_score = 0
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-100, 360)
        self.write(f'score :{self.player_score}', align='center', font=('Arial', 20, 'normal'))

    def new_score(self):
        self.clear()
        self.player_score += random.randint(100,500)
        self.write(f'score :{self.player_score}', align='center', font=('Arial', 20, 'normal'))