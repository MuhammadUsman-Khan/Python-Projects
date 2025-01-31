def bmi(weight, height):
    result = weight / ((height / 100) ** 2)
    if result < 18.5:
        print("You are Under weight")

    elif result > 18.5 and result < 24.9:
        print("You are Normal weight")

    elif result > 25 and result < 29.9:
        print("You are Overweight")

    elif result > 30:
        print("You are Obese")

weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in cm: "))
bmi(weight, height)