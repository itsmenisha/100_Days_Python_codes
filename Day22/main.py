from turtle import Screen
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
# create a screen
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# create and move two paddle
R_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score = Scoreboard()

# what she did
screen.listen()
screen.onkey(R_paddle.up, "Up")
screen.onkey(R_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# create a ball and make it move
is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
# detect the collision and make it bounce
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()


# detect collision with paddle
    if ball.distance(R_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("made contact")
        ball.bounce_x()

# keep score
    if ball.xcor() < -380:
        print("left ball missed")
        ball.reset_pos()
        score.r_point()

    if ball.xcor() > 380:
        print("right ball missed")
        ball.reset_pos()
        score.l_point()


screen.exitonclick()
