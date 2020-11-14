Height = int(input())
Age = int(input())
bill = 0
if Height >= 120:
    print("You are eligible for RollerCoaster:")
    if Age<12:
        print("Child ticket is $5.")
        bill = 5
    if 12<Age<=18:
        print("Youth ticket is $7.")
        bill = 7
    else:
        print("Adult ticket are $12.")
        bill = 12

WantPhoto = input("Do you want to photo?")

if WantPhoto=="Y":
    bill += 3

print(f"Your final bill is {bill}.")
