from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 270

# move the turtle with keypass


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto_start()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def isatfinish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def goto_start(self):
        self.setpos(STARTING_POSITION)
