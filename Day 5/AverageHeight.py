StudentHeight = input("Enter list of student height").split()

for student in range(len(StudentHeight)):
    StudentHeight[student] = int(StudentHeight[student])

AverageTotalHeight = 0

for i in range(len(StudentHeight)):
    AverageTotalHeight += StudentHeight[i]

AverageTotalHeight /= len(StudentHeight)

print(round(AverageTotalHeight))

Stcount = 0

for student in StudentHeight:
    Stcount += 1
print(Stcount)
