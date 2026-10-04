""" Goal
Practice numerical input and formulas.
Ask the user for:
Name
Weight in kilograms
Height in meters
Calculate BMI:
BMI = weight / (height × height)

Display the result.
Example
================================
          BMI REPORT
================================

Name: Ahmed
Weight: 60 kg
Height: 1.70 m

BMI: 20.76
================================

"""

user_name = input("User Name: ")
weight = float(input("Weight in kgs: "))
height = float(input("Height in meters: "))

bmi = weight/ (height* height)
width = 40 

print("=" * width)
print("BMI REPORT".center(width))
print("=" * width)
print()
print(f"Name: {user_name}")
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print()
print(f"BMI = {bmi:.2f}")
print("=" * width)
