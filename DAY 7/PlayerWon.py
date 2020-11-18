display = []

word_list = ["aardvark", "baboon", "camel"]
import random
choosen_word = random.choice(word_list)

print(choosen_word)
for i in range(len(choosen_word)):
    display += "_";
print(display)

flag = True

guess = input("Enter your char guess: ")


while flag:
    for i in range(len(choosen_word)):
        if guess == choosen_word[i]:
            display[i] = guess

            print("You guessed  correct character")
            if "_" not in display:
                flag = False



print(display)
