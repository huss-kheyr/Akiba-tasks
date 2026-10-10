""" 
 A prime number is a number greater than 1 that can only be divided exactly by 1 and itself.
Requirements
Your solution must use a loop to check possible divisors.
Important Cases
Your program should correctly handle:
0 → Not Prime
1 → Not Prime
2 → Prime
Challenge
Explain in your code comments why you do not need to check every number up to the input number.
"""
number = int(input("Number: "))

if number < 2:
    print("The number is not prime")
else:
    is_prime = True    
for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        is_prime = False
        break
    
    if is_prime :
        print("The number is prime")
    else:
        print("The number is not prime")
        