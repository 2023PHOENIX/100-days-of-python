import random
from ART import logo

chance = 0

print(logo)


def Play(c):
    guesses = random.randint(0, 101)
    print("I am guessing the number Please Wait...!")
    for i in range(c):
        print(f"You are left with {c - i} chances")
        player_guess = int(input("Enter you guess :"))
        if guesses == player_guess:
            print("You guessed it correctly..!")
            break
        elif guesses < player_guess:
            print("Too high")
        elif guesses > player_guess:
            print("Too low")

        print(f"sorry You are not able to guess the number in {c} chances")


#
# print(guess)

difficulty = input("Enter your difficulties level (Easy/Hard) :")

if difficulty == 'Easy':
    chance = 10

elif difficulty == 'Hard':
    chance = 5
print(f"You have {chance} to guess the number correctly")
Play(chance)
