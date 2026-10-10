""" Problem
Ask the user for a positive number N.
Your program should count from 1 to N and calculate:
How many numbers are even
How many numbers are odd
The sum of all numbers
 
Computational Thinking Challenge
Do not solve each result separately.
Think about how one loop can be used to calculate all three results.
"""
number = int(input("Number: "))
number = abs(number)
total_sum = 0
even_num = 0
odd_num = 0

for i in range(1, number + 1):
    total_sum += i   
    if i % 2 == 0:
        even_num += 1
    else:
        odd_num += 1

    
print(f"The total number of even numbers is {even_num}")
print(f"The total number of odd numbers is {odd_num}")
print(f"The total sum is {total_sum}")