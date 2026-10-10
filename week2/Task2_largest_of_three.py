num_1 = int(input("The First Number: "))
num_2 = int(input("The Second Number: "))
num_3 = int(input("The Third Number: "))

if num_3 == num_2 == num_1 :
    print("All the numbers are equal")
else:
    if num_1 >= num_2 and num_1 >= num_3 :
        largest = num_1
    elif num_2 >= num_1 and num_2 >= num_3:
        largest = num_2
    else: 
        largest = num_3
        
    if[num_1, num_2, num_3].count(largest) == 2:
            print(f"{largest} is the greatest number (two numbers are tied to it)")
    else: 
            print(f"{largest} is the greatest number")