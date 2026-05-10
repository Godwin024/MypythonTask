weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)

print("BMI =", bmi)

if bmi < 18.5:
    print("Underweight")

elif 18.5 <= bmi < 24.9:
    print("Normal")

elif 25 <= bmi < 29.9:
    print("Overweight")

else:
    print("Obese")
