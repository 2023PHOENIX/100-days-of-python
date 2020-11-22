"""display art

generate a random account from the game data

fromat the account data into printable format

Ask user for a guess

check if user is correct

get follower count of each if user is correct.
        
give user feed back on their guess.

Score keeping 
Make the game repeatable. 
Making account at position B become the next account at  position A 
clear the screen
"""
from ART import logo, vs
from Data import data
import random

print(logo)
score = 0


def format_data(c):
    account_name = c["name"]
    account_descr = c["description"]
    account_country = c["country"]
    print(f"{account_name}, a {account_descr} , from {account_country}")


def is_correct(g, a, b):
    if a["follower_count"] > b["follower_count"]:
        if g == 'A':
            return True
        else:
            return False
    else:
        if g == 'B':
            return True
        else:
            return False


while True:
    account_a = random.choice(data)
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    # data in dictionaries
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")
    guess = input("Guess Who has more followers A or B")
    if is_correct(guess, account_a, account_b):
        score += 1
        print(f"You're right your current score is {score}.\n\n")
    else:
        print(f"sorry,that's wrong. Final Score {score}.\n\n")
        break
    clear()
