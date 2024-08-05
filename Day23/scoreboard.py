from turtle import Turtle
# create a scoreboard

FONT = ("Courier", 15, "normal")
FONTg = ("Courier", 25, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 260)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def levelup(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONTg)
