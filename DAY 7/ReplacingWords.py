#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.


import random
word_list = ["aardvark", "baboon", "camel"]
pick = random.choice(word_list)
display = []
for i in range(len(pick)):
    display+="_"
print(display)
import random
flag = True
while flag:
    guess = input("Enter your guess char:")
    for letter in range(len(pick)):
        if guess == pick[letter]:
            display[letter] = guess
            print(display)
        if "_" not in display:
            flag = False
