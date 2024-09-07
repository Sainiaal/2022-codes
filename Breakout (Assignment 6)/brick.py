import random
from turtle import Turtle

colors = ["#CF0A0A", "#DC5F00", "#FF5858", "#9A1663"]


class Bricks:
    def __init__(self):
        self.all_bricks = []
        self.create()
        self.score = Turtle()
        self.lives = Turtle()
        self.lives_left = 3
        self.scoreboard()
        self.show_lives()

    def scoreboard(self, points=0):
        self.score.penup()
        self.score.goto(380, 270)
        self.score.color("white")
        self.score.hideturtle()
        self.score.clear()
        self.score.write(f"Points: {points}", font=("Arial", 16, "normal"))

    def show_lives(self, points=0):

        self.lives.penup()
        self.lives.goto(-380, 270)
        self.lives.color("white")
        self.lives.hideturtle()
        self.lives.clear()
        self.lives.write(f"Lives: {self.lives_left}", font=("Arial", 16, "normal"))

    def create(self):
        for pos_y in range(0, 5):
            for pos_x in range(-6, 7):
                self.add_brick(pos_x, pos_y)

    def add_brick(self, x, y):
        new_brick = Turtle(shape="square")
        color = random.choice(colors)
        new_brick.penup()
        new_brick.color(color)
        new_brick.goto(x*70, y*50)
        new_brick.shapesize(stretch_wid=1, stretch_len=3)
        self.all_bricks.append(new_brick)
