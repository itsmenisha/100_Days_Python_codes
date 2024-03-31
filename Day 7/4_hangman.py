# fourth hangman
import random
stages = [  # final state: head, torso, both arms, and both legs
    """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
    # head, torso, both arms, and one leg
    """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
    # head, torso, and both arms
    """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
    # head, torso, and one arm
    """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
    # head and torso
    """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
    # head
    """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
    # initial empty state
    """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
]
word_list = ["ardvark", "baboon", "camel"]
random1 = random.choice(word_list)
lives = 6
print(f"the random word will be {random1}")
display = []
wordlen = len(random1)
for _ in range(wordlen):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Choose a word :").lower()
    for position in range(wordlen):
        letter = random1[position]
        if letter == guess:
            display[position] = letter
    if guess not in random1:
        lives -= 1
    if lives == 0:
        end_of_game = True

    print(f"[{'  '.join(display)}]")
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print('''you won!!!!
        
         ()  ()  () ()
         ||  ||  || ||  
         ||  ||  || ||  
         ||..||..||.||
         ||..||..||.||
         {.............}
       }}}}} _   _ {{{{{
       }}}}  O   O  {{{{
      {{{{{    ^    }}}}}
     {{{{{{\ ----- /}}}}}}
     {{{{{{{;.___.;}}}}}}}
      {{{{{{{)   (}}}}}}}'
       `""'"':   :'"'"'`
''')