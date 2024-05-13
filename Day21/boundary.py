from turtle import Turtle
import random


class Boundary(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.touch()

    def touch(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
