size = input("Enter size of pizza:\n1.S\t2.M\t3.L")
AddPepperoni = input("Do you want pepperoni? Y or N")
extraChesse = input("Do you want extra Cheese? Y or N")
Bill = 0
if size=="S":
    if AddPepporoni == 'Y':
        Bill = Bill + 2 + 15
    else:
        Bill = Bill + 15
if size=="M":
    if Addpepporoni == 'Y':
        Bill += 3 + 20
    else :
        Bill += 20
if size == 'L':
    if AddPepperoni == "Y":
        Bill += 3 + 25
    else :
        Bill += 25

if extraChesse=='Y':
    Bill+=1

print(f"Your total bill is ${Bill}.")
