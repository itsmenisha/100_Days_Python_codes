from art import logo
import random
easy = 10
hard = 5


def play_game():
    def set_diffiiculty():
        a = input("Choose a difficulty level 'easy or 'hard: ").lower()
        if a == "hard":
            return hard
        if a == "easy":
            return easy

    numberof = set_diffiiculty()

    def check_answer(guess, number, no_of_live):
        if guess < number:
            print("guess higher")
            return no_of_live - 1
        elif (guess > number):
            print("guess lower")
            return no_of_live - 1
        else:
            print("you guessed right")
            print(f"the answer is {number}")
            return no_of_live

    print(logo)
    print("Welcome to the number Guessing game")
    print("Think a number between 1 to 100")
    number = random.randint(0, 300)
    guess = 0
    while guess != number:
        print(f"you have {numberof} turns remaining")
        guess = int(input("Make a guess:"))
        numberof = check_answer(guess, number, numberof)
        if numberof <= 0:
            print("You lost all of your chances. You loose")
            print(f"the answer was {number}")
            return
        elif guess != number:
            print("Guess again")


play_game()
