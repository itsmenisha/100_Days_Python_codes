from turtle import Turtle, Screen
import random
import turtle as t
t.colormode(255)
shape = Turtle()
shape.speed("fastest")
shape.pensize(10)

direction = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(400):
    color = random_color()
    shape.forward(30)
    shape.setheading(random.choice(direction))
    shape.color(random_color())


screen = Screen()
screen.exitonclick()
