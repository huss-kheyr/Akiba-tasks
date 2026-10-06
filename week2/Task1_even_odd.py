""" Problem
Write a program that asks the user to enter a number and determines whether the number is even or odd.
Requirements
Get the number from the user.
Use a condition to make the decision.
Display the result clearly.
Challenge
Also handle:
Positive numbers
Negative numbers
Zero

"""

number = int(input("Number: "))

if number == 0 :
    print("Zero")
if number != 0 and number % 2 == 0:
    print(number ,"is even.")
else :
    print(number,"is odd.")
    