import heroes
from turtle import Turtle, Screen
# import turtle as nisu
nisu = Turtle()
nisu.shape("turtle")
nisu.color('olive')
# print(heroes.gen())

# nisha_turtle.forward(200)
# nisha_turtle.left(90)
# nisha_turtle.forward(200)
# nisha_turtle.left(90)
# nisha_turtle.forward(200)
# nisha_turtle.left(90)
# nisha_turtle.forward(200)

for _ in range(4):
    nisu.forward(200)
    nisu.left(90)

screen = Screen()
screen.exitonclick()
