
destination = input("Destination: ")
distance_km = int(input("Distance(km): "))
average_speed = float(input("Average speed(km): "))

total_hour = distance_km / average_speed
total_minutes = round(total_hour * 60)
hours,minutes = divmod(total_minutes, 60)

print(f"Estimated Travel Time: {hours} hours {minutes} minutes")