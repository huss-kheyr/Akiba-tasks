start = int(input("Start: "))
end = int(input("End: "))

i = start
while i <= end:
    if i % 3 == 0 and i % 5 == 0 :
                print("FIZZBUZZ")
    elif i % 3 == 0 and i % 5 != 0 :
            print("FIZZ")
    elif i % 5 == 0 and i % 3 != 0:
            print("BUZZ")
    else:
            print(i)
    i += 1
