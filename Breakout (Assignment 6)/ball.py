from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#3F0071")
        self.penup()
        self.shape("circle")
        self.move_speed = 0.1
        self.goto(0, -150)
        self.turn = 90
        self.left(45)
        self.repeat = 0

    def move_forward(self):
        self.forward(10)

    def paddle(self, rotate):
        if 180 < self.heading() < 270:
            self.right(rotate)
        elif 270 < self.heading() < 360:
            self.left(rotate)

    def reflect(self):
        if self.xcor() < 0:
            self.goto(-450, self.ycor())
            if 0 < self.heading() <= 90:
                self.setheading(135)
            if 90 < self.heading() <= 180:
                self.setheading(45)
            if 180 < self.heading() <= 270:
                self.setheading(315)
            if 270 < self.heading() <= 360:
                self.setheading(225)
        else:
            self.goto(450, self.ycor())
            if 0 < self.heading() <= 90:
                self.setheading(135)
            if 90 < self.heading() <= 180:
                self.setheading(45)
            if 180 < self.heading() <= 270:
                self.setheading(315)
            if 270 < self.heading() <= 360:
                self.setheading(225)

    def top(self):
        self.goto(self.xcor(), 250)
        if 0 < self.heading() <= 90:
            self.setheading(315)
        if 90 < self.heading() <= 180:
            self.setheading(225)

    def hit(self):
        if 0 < self.heading() <= 90:
            self.setheading(315)
        elif 90 < self.heading() <= 180:
            self.setheading(225)
        elif 180 < self.heading() <= 270:
            self.setheading(315)
        elif 270 < self.heading() <= 360:
            self.setheading(45)

    def reset_position(self):
        self.hideturtle()
        self.right(180)
        self.goto(0, -150)
        self.move_speed = 0.1
        self.showturtle()

    def move(self):
        self.move_forward()
        if (-450 < self.xcor() < 450) is not True:
            self.reflect()
            self.move_forward()
        if self.ycor() > 250:
            self.top()
            self.move_forward()
        self.forward(10)
