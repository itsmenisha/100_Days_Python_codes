from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "purple", "blue", "green", "yellow", "orange"]
all_colors = []
is_game_on = False
move = [20, 60, 100, -20, -60, -90]
for turtle_index in range(0, 6):
    turt = Turtle(shape="turtle")
    turt.penup()
    turt.color(colors[turtle_index])
    turt.goto(x=-230, y=(move[turtle_index]))
    all_colors.append(turt)

user_bet = screen.textinput(
    title="Choose a Player", prompt="Which turtle would you like to bet on. Pick a color:")
if user_bet:
    is_game_on = True
while is_game_on:
    for turtle in all_colors:
        if turtle.xcor() > 210:
            is_game_on = False
            winning_color = turtle.pencolor()

            if user_bet == winning_color:
                print(f"You won😃😃🎊.the turtle who won is {winning_color}🎊")
            else:
                print(f"You loose😞.the turtle who won is {winning_color}")

        num = random.randint(0, 10)
        turtle.forward(num)

screen.exitonclick()
