from turtle import Turtle, Screen
import random
import turtle as t
t.colormode(255)
nisha = Turtle()
nisha.speed("fastest")
screen = Screen()


def move_forward():
    nisha.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()
