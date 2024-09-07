from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("#FB2576")
        self.hideturtle()
        self.goto(x=0, y=-200)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.showturtle()

    def go_right(self):
        if self.xcor() < 430:
            new_x = self.xcor() + 50
            self.goto(new_x, self.ycor())

    def go_left(self):
        if self.xcor() > -430:
            new_x = self.xcor() - 50
            self.goto(new_x, self.ycor())
