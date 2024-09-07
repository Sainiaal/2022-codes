# -----------------------------Modules------------------------------------------
import random
import time
from turtle import Screen, Turtle
# -----------------------------Classes------------------------------------------
from ball import Ball
from paddle import Paddle
from brick import Bricks

# -----------------------------Screen setup------------------------------------------
screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("#000000")
screen.tracer(0)
# -----------------------------Objects------------------------------------------
ball = Ball()
paddle = Paddle()
brick = Bricks()

# -----------------------------Running Code------------------------------------------
screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

repeat = 0
angles = [60, 75, 85, 90, 95, 105]
points = 0
game_end = False

while not game_end:
    ball.move()
    time.sleep(ball.move_speed)
    screen.update()
    dist = ball.distance(paddle)
    repeat += 1
    if dist < 50 and repeat > 2 and ball.ycor() < -180:
        repeat = 0
        angle = random.choice(angles)
        ball.paddle(angle)
    for box in brick.all_bricks:
        if ball.distance(box) < 50:
            points += 10
            ball.hit()
            box.hideturtle()
            brick.all_bricks.remove(box)
            ball.move_forward()
            break
    if ball.ycor() < -250:
        brick.lives_left -= 1
        ball.reset_position()
        if brick.lives_left == 0:
            game_end = True
    brick.scoreboard(points)
    brick.show_lives()

screen.clear()
screen.bgcolor("#000000")

final = Turtle()
final.hideturtle()
final.goto(-250, 0)
final.penup()
final.color("white")
final.write(f"Your score was {points} points", font=("Arial", 40, "normal"))

screen.exitonclick()
