def add_digits(number):
    total = 0
    number = abs(number)
    while number > 0:
        total += number % 10
        number //= 10
    
    return total

number = int(input("Number: "))
print(f"The total is {add_digits(number)}")
    