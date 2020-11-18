def PrimeNumber(number):
    flag = False
    for i in range(2, (number//2) + 1):
        if number%i==0:
            flag = True
            break
    return flag

n = int(input("Enter your number\n To check weather it is prime or not :"))

if PrimeNumber(number = n)  == False:
    print("Number is prime")
else:
    print("Number is not prime")
