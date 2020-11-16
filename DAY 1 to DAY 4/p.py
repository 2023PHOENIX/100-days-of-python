Weight = float(input())
Height = float(input())


BMI = round(Weight/Height**2)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, You are underweight")
elif 18.5 <= BMI < 25:
    print(f"Your BMI is {BMI} ,Your Weight is normal")
elif 25 <= BMI < 30:
    print(f"Your BMI is {BMI} , You are Overweight")
elif 30 <= BMI <=35:
    print("you are Obese")
else:
    print(f"Your BMI is {BMI}, You are clinically Obese")
