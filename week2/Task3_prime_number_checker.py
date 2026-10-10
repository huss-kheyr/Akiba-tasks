number = int(input("Number: "))

if number < 2:
    print("The number is not prime")
else:
    is_prime = True    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    # we only need to chcck divisors up to the square root of the number
    if is_prime :
        print("The number is prime")
    else:
        print("The number is not prime")
        