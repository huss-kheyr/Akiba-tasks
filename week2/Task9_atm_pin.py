""" 

Requirements
Use:
while or another appropriate loop
Conditions
Counter
User input
Challenge
Display how many attempts remain.
Example:
Incorrect PIN.
Attempts remaining: 2
"""
max_attempts = 3
attempts_used = 0

pin = 1234

while attempts_used < max_attempts:
    attempt = int(input("Enter the pin: "))
    if attempt == pin:
        print("Verified successfully")
        break
    elif attempt != pin:
        print(f"Incorrect pin.\n you have {max_attempts - attempts_used} attempts left")
    attempts_used += 1
else:
     print("please try again later")       
    