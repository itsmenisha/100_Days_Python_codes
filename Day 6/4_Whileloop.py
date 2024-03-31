# hurdle 2 challange
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


num_hurdle = 6
while num_hurdle > 6:
    jump()
    num_hurdle -= 1
    print(num_hurdle)
