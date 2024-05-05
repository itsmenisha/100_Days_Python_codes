from turtle import Turtle, Screen
import turtle as t
t.colormode(255)
nisha = Turtle()
nisha.speed("fastest")
screen = Screen()


def move_forward():
    nisha.forward(10)


def move_right():
    nisha.right(10)


def move_left():
    nisha.left(10)


def move_backward():
    nisha.backward(10)


def clear_screen():
    nisha.clear()
    nisha.penup()
    nisha.home()
    nisha.pendown()



screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(move_backward, "s")
screen.onkey(clear_screen, "c")
screen.exitonclick()
