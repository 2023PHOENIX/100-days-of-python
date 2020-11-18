#Step 1

word_list = ["aardvark", "baboon", "camel"]
import random
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# 1. Create
print(random.choice(word_list))

guess = input("Guess a letter: ")

guess = guess.lower()
flag = False

for i in range(0, len(word_list)):
    if guess == word_list[i]:
        flag = True;

if flag:
    print("Word found")
else:
    print("Word not found")
