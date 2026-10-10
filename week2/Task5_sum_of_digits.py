num = int(input("Number: "))

def add_digits(num):
    total = 0
    num = abs(num)
    while num > 0:
        total += num % 10
        num //= 10
    
    return total

print(f"The total is {add_digits(num)}")
    