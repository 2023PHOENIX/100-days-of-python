def Add(a, b):
    return a + b


def Sub(a, b):
    return a - b


def Mul(a, b):
    return a * b


def Div(a, b):
    return a / b


def absoluteDiv(a, b):
    return a // b


# key are +,-, =,/. Values are function calls
OperationDict = {
    "+": Add,
    "-": Sub,
    "/": Div,
    "*": Mul,
    "//": absoluteDiv
}

a = int(input("Enter your number:"))
b = int(input("Enter your number:"))

while True:

    for symbol in OperationDict:
        print(symbol)

    OperationSymbol = input("Enter your operation symbol: ")

    calculationFunction = OperationDict[OperationSymbol]
    answer = calculationFunction(a, b)
    print(f"{a} {OperationSymbol} {b} = {answer}")

    choice = input("Do you want to perform calculation over previos result.? (y/n): ")

    if choice == "y":
        a = answer
        b = int(input("Enter your number"))
    else:
        break
