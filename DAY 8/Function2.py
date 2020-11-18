def AreaCalculation(length, width):
    coverage = 5
    return (length * width)/coverage

length = int(input("Enter your length: "))
width = int(input("Enter your width: "))


print(f"You need {AreaCalculation(length, width)} number of cans")
