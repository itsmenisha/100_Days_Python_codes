# This ia learned from angela
import random
from art import logo, vs
from dictionary import account


def check_data(followersA, followersB, decision):
    if followersA > followersB:
        return decision == "a"
    elif followersB > followersA:
        return decision == "b"
    else:
        return decision == "equal"


def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    return (f"{account_name}is a {account_desc}")


print(logo)
scores = 0
game_continue = True
account_a = random.choice(account)
account_b = random.choice(account)
while game_continue:

    if account_a == account_b:
        account_b = random.choice(account)
    print(f"compare A:{format_data(account_a)}")
    print(vs)
    print(f"Against B:{format_data(account_b)}")

    decision = input(
        '''Who do you think has more followers
                        (a,b or are they equal): ''').lower()
    followersA = account_a["followers"]
    followersB = account_b["followers"]

    is_correct = check_data(followersA, followersB, decision)
    if is_correct:
        scores += 1
        account_a = account_b
        game_continue = True
        print(f'''You are correct.Your score is {scores}''')
    else:
        game_continue = False
        # answers != "equal" and decisions != answers:
        print(f"opps!That was incorrect. Your final score is {scores}")
