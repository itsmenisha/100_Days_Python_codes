from turtle import Turtle, Screen
import random
# import colorgram
import turtle as t
t.colormode(255)
shape = Turtle()
shape.speed("fastest")

# colors = colorgram.extract('image.jpg', 35)
# # i = 0
# colors_persent = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color = (r, g, b)
#     colors_persent.append(color)
# print(colors_persent)

colors_persent = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160,
                                                                                                                                                                                                                                                                 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141),]


def colors_choice():
    colors = random.choice(colors_persent)
    return colors


shape.penup()
shape.hideturtle()
shape.setheading(215)
shape.forward(280)
shape.setheading(0)

is_true = True
for _ in range(10):
    for _ in range(10):
        colorss = colors_choice()
        shape.dot(20, colorss)
        shape.forward(50)
    shape.left(90)
    shape.forward(40)
    shape.left(90)
    shape.forward(500)
    shape.right(180)

screen = Screen()
screen.exitonclick()

# trial
#     def random_color():
#     global i
#     first_color = colors[i]
#     rgb = first_color.rgb  # e.g. (255, 151, 210)
#     hsl = first_color.hsl
#     proportion = first_color.proportion
#     # print(rgb)
#     i += 1
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     color = (r, g, b)
# return color
# for _ in range(20):
#     color = random_color()
#     print(color)
# shape.circle(10)
# shape.fillcolor()
# shape.color(random_color())
# print(shape.heading())
