from turtle import Turtle, Screen
import random

shape = Turtle()
shape.shape("turtle")
colors = ['green', 'blue', 'pink', 'yellow', 'light_blue', 'olive']


def draw_shape(num):
    angle = 360/num
    for _ in range(num):
        shape.right(angle)
        shape.forward(100)


for shape_side in range(3, 11):
    draw_shape(shape_side)
    shape.color(random.choice(colors))

screen = Screen()
screen.exitonclick()
