StudentScore = input("Enter your list").split()

print(StudentScore)
for i in range(len(StudentScore)):
    StudentScore[i] = int(StudentScore[i])

HighestScore = 0
for i in range(len(StudentScore)):
    if StudentScore[i] > HighestScore:
        HighestScore = StudentScore[i]

print(HighestScore)
