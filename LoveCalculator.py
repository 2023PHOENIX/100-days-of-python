print("Welcome to the Love Calculator")

name1 = input("Enter your name.?")
name2 = input("Enter their name.?")

name1 = name1.lower()
name2 = name2.lower()
t = 0;
l = 0;
combine_string = name1 + name2

t += combine_string.count("t")
t += combine_string.count("r")

t += combine_string.count("u")
t += combine_string.count("e")


l += combine_string.count("l")
l += combine_string.count("o")

l += combine_string.count("v")
l += combine_string.count("e")

Love_score = t*10 + l

if(Love_score>80):
    print(f"Your score is {Love_score}, You are alright together")
elif (Love_score>=40) and (Love_score<80):
    print(f"your score is {Love_score}, you are okay!")
else:
    print("katega tumhra")
