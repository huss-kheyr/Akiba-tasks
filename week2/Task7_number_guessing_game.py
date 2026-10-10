import random 
max_attempts = 5
attempts_used = 0
secret_number = random.randint(1,10)

print("I have picked a number between 1 and 10.")
print(f"You have {max_attempts} attempts to guess it.")

while attempts_used < max_attempts:
    try: 
        guess = int(input("Guess the number: "))
    except ValueError:
        print("Please enter a valid number")
        continue
    attempts_used += 1
        
    if guess == secret_number:
        print(f"Congratulations! \n You've guessed the number in {attempts_used} attempts.")
        break
    else:
        print("Try again")
else:
    print("Game Over!")
    
    