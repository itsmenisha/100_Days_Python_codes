from turtle import Turtle, Screen
screen = Screen()

# create and move a paddle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)


# for moving what i did

# def up():
#     new_y = R_paddle.ycor()+20
#     R_paddle.goto(R_paddle.xcor(), new_y)


# def down():
#     new_y = R_paddle.ycor()-20
#     R_paddle.goto(R_paddle.xcor(), new_y)


# def up_w():
#     new_y = l_paddle.ycor()+20
#     l_paddle.goto(l_paddle.xcor(), new_y)


# def down_s():
#     new_y = l_paddle.ycor()-20
#     l_paddle.goto(l_paddle.xcor(), new_y)

# screen.listen()
# screen.onkey(up, "Up")
# screen.onkey(down, "Down")
# screen.onkey(up_w, "w")
# screen.onkey(down_s, "s")
