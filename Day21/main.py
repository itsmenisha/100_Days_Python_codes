from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
is_game_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while is_game_on:
    screen.update()
    time.sleep(0.1)
#  control the snake(done)

# secondchallanges

# collision with the food
    if snake.head.distance(food) < 15:
        # print("yummyyyy!!")
        food.refresh()
        snake.extend()
        # creating a scoreboard
        scoreboard.increase_score()
# detect collision with the wall-game over
    if snake.head.xcor() > 279 or snake.head.xcor() < -279 or snake.head.ycor() > 279 or snake.head.ycor() < -279:
        print("game over")
        is_game_on = False
        scoreboard.game_over()
# detect collision with its own tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            print("game over")
            is_game_on = False
            scoreboard.game_over()

    snake.move()


screen.exitonclick()
