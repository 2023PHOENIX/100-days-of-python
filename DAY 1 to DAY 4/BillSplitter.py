import random as rd
n = int(input())
LongList = []
for i in range(0,n):
    LongList.append(input())

X = rd.randint(1,n)

print(f"{LongList[X-1]} is going to buy the meal today")
