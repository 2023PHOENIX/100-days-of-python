import random
letter = int(input("Enter total number of letters"))
symbol = int(input("Enter total number of symbols"))
number = int(input("Enter total number of numbers"))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

Password = []

for i in range(letter):
    Password.append(random.choice(letters))
for i in range(number):
    Password.append(random.choice(numbers))
for i in range(symbol):
    Password.append(random.choice(symbols))

random.shuffle(Password)
print(f"Your password is {Password}")
