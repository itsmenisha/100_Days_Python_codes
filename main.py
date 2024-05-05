from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet",
                            prompt="Choose your players color:")
is_race_on = False
y_position = [20, 50, 80, -10, -40, -70]
colors = ["red", "blue", "yellow", "green", "purple", "orange"]
all = []

for turtle_index in range(0, 6):
    turt = Turtle(shape="turtle")
    turt.penup()
    turt.goto(x=-220, y=y_position[turtle_index])
    turt.color(colors[turtle_index])
    all.append(turt)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()

            if user_bet == winning_color:
                print(f"You won😃😃🎊.the turtle who won is {winning_color}🎊")
            else:
                print(f"You loose😞.the turtle who won is {winning_color}")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
