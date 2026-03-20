print('----MY PERSONAL BODY MASS INDEX(BMI) CALCULATOR----')
weight=float(input('Please Enter Your Weight In Kilograms: '))
height=float(input('Please Enter Your Height In Meters: '))
bmi=weight/(height**2)
print(f'Your BMI is: {bmi}')
if bmi <= 18.5:
    print('You Are Underweight')
elif bmi >18.5 and bmi <= 24.9:
    print('You Have A Normal Weight')
elif bmi > 24.9 and bmi <= 29.9:
    print('You Are Overweight')
elif bmi > 29.9 and bmi <= 34.9:
    print('You Are Obese')
print('THIS PROJECT IS DESIGNED BY NSIKAN AKPAN')
print(int(bmi))
print("Thank You For Using And Accessing our Calculator")