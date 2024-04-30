from turtle import Turtle, Screen
import random

shape = Turtle()
shape.speed("fastest")
shape.pensize(10)
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan", "magenta", "brown",
          "turquoise", "lime", "teal", "maroon", "navy", "gold", "orchid", "slategray", "salmon", "skyblue"]
direction = [0, 90, 180, 270]

for _ in range(300):
    shape.forward(30)
    shape.setheading(random.choice(direction))
    shape.color(random.choice(colors))

# direction = ['left', 'right']


# def draw_line(num):
#     for _ in range(num):
#         direct = random.choice(direction)
#         if direct == "right":
#             shape.right(90)
#         else:
#             shape.left(90)
#         shape.forward(10)


# for shape_side in range(1, 360):
#     draw_line(shape_side)
#     shape.color(random.choice(colors))

screen = Screen()
screen.exitonclick()
