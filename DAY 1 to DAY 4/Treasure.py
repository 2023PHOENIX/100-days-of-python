
print("Welcome to Treasure Island. \n Your Mission is to find the treasure.")

choice1 = input('Enter your choice:\n "L" : left  \n "R" : Right\n' )

if choice1 == "R":
    print("Game Over!!!")
else :
    choice2 = input("You Have two choices Either Swim(S) or Wait(W) :")
    if choice2=='S':
        print("Game Over!!!")
    else:
        choice3 = input("Enter which door you want to open Red(R),YEllow(Y) or Blue(B)")
        if choice3=="R" or choice3=="B":
            print("Game Over!!!")
        if choice3=="Y":
            print("You Win. Game Ended!!!")
