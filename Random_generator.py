import random as rd


print("Welcome to Coin Toss!")

z = input("Enter {S} for start : ")

if(z=='S'):
    a = rd.randint(1,1999)
    if a&1==0:
        print("Tails")
    else:
        print("Head")

if(z=='T'):
    a = rd.seed(123)
    a = rd.randint(1,1999)
    if a&1==0:
        print("Tails")
    else:
        print("Head")
