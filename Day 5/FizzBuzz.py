for i in range(1,101):
    if(i%5==0 and i%3==0):
        print(i)
        print("Fizz and Buzz")
    elif i%3==0:
        print(i)
        print("Fizz")
    elif i%5==0:
        print(i)
        print("Buzz")
    else: print(i)
