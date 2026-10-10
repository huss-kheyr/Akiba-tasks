COUNT = 10
largest = None
smallest = None
total = 0
even_count = 0
odd_count = 0

for i in range(1, COUNT + 1):
    num = int(input(f"Enter number {i}: "))
    
    if largest is None:
        largest = num
        smallest = num
    else:
        if num > largest:
            largest = num
        if num <smallest:
            smallest = num
    total += num
    
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
average = total / COUNT

print(f"Largest: {largest}")    
print(f"Smallest: {smallest}")
print(f"Sum: {total}")
print(f"Average: {average}")
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")




    
        