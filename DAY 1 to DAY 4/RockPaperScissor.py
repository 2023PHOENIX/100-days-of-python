rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

User = int(input("Enter 0 for Rock \nEnter 1 for paper: \nEnter 2 scissors: "))
LL = [rock,paper,scissors]

import random
Com = random.randint(0,3)

if User==2 and Com==0:
    print(f"USER WIN\nUser input scissor: {LL[2]} Computer input :{LL[0]}")

if User > Com:
    print(f"USER WIN\nUser input: {LL[User]}\n Computer input: {LL[Com]}")
else:
    print(f"You lose\nUser input :{LL[User]}\n Computer input: {LL[Com]}")
