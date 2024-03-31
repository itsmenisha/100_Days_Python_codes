# first hangman
from ctypes.wintypes import WORD
import random
word_list = ["ardvark", "baboon", "camel"]
random1 = random.choice(word_list)
print(f"the random word will be {random1}")
guess = input("Choose a word :").lower()
for each in random1:
    if guess == each:
        print("True")
    else:
        print("False")