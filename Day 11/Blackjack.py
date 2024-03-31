# This is a Blackjack card game that is did on my own at the begining
import random
from art import logo
# for the server
cards = [1, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
a = random.choice(cards)
b = random.choice(cards)
card_s = [a, b]
# for user
c = random.choice(cards)
d = random.choice(cards)
card_u = [c, d]

play = input('''Do you want to play the game of blackjack.
      if yes, type 'y' and if no type 'n':''').lower()

while play:
    if play == "y":
        play = True
        print(logo)
        print(f'''the computers first card is
                    [{a},*] ''')
        print(f"  Your cards {card_u}")

        another = input(
            "type 'y' to get another card and type 'n' to pass:").lower()
        if another == "y":
            e = random.choice(cards)
            card_u.append(e)
            print(f'''yours cards now:
                    {card_u}''')
            play = True
            total_user = 0
            for each in card_u:
                total_user += each
            total_server = 0
            for each in card_s:
                total_server += each
            print(f"Your final hand {card_u}")
            print(f"the total: {total_user}")
            print(f"The computers  final hand {card_s} ")
            print(f"the total: {total_server}")
            if total_user > 21:
                print("you loose3")
                break
            if total_server > 21:
                print("you win3")
                break

        elif another == "n":
            print(f"Your final hand {card_u}")
            print(f"The computers  final hand {card_s} ")
            total_user = 0
            for each in card_u:
                total_user += each
            total_server = 0
            for each in card_s:
                total_server += each
            print(f"Your final hand {card_u}")
            print(f"the total: {total_user}")
            print(f"The computers  final hand {card_s} ")
            print(f"the total: {total_server}")
            if total_user > 21:
                print("you loose3")
                break
            if total_server > 21:
                print("you win3")
                break

        total_user = 0
        for each in card_u:
            total_user += each
        total_server = 0
        for each in card_s:
            total_server += each
        if (a == 11 or b == 11) and (a == 10 or b == 10):
            print("You win1")
            play = False
            if (c == 11 or d == 11) and (c == 10 or d == 10):
                print("Draw")
                play = False
        elif (c == 11 or d == 11) and (c == 10 or d == 10):
            print("You Loose1")
            play = False
        if card_u > card_s and total_user <= 21:
            print("you win2")
            play = False
        if card_u < card_s and total_server <= 21:
            print("you loose2")
            play = False
