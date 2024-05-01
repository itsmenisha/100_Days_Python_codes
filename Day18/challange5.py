from turtle import Turtle, Screen
import random
import turtle as t
t.colormode(255)
shape = Turtle()
shape.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def sipraphhon(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        color = random_color()
        shape.circle(100)
        shape.color(random_color())
        # shape.left(5)
        print(shape.heading())
        shape.setheading(shape.heading()+size_of_gap)


sipraphhon(5)
screen = Screen()
screen.exitonclick()
