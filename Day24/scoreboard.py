from turtle import Turtle
ALIGNMENT = "CENTER"
FONT = ("courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("myscore.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        self.reset()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", move=False,
                   align="center", font=("courier", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("myscore.txt", mode="w") as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", move=False,
    #                align=ALIGNMENT, font=("courier", 20, "normal"))
    #     self.goto(0, -30)
    #     self.write(f"Score:{self.score}", move=False,
    #                align=ALIGNMENT, font=("courier", 16, "normal"))
