# second hangman
import random
word_list = ["ardvark", "baboon", "camel"]
random1 = random.choice(word_list)
print(f"the random word will be {random1}")
display = []
wordlen = len(random1)
for _ in range(wordlen):
    display += "_"
print(display)
guess = input("Choose a word :").lower()

for position in range(wordlen):
    letter = random1[position]
    if letter == guess:
        display[position] = letter
print(display)
