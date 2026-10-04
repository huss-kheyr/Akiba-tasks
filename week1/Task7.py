""""
Goal
Practice working with time, distance, and user input.
Create a simple travel information program.
Ask the user for:
Destination
Distance in kilometers
Average speed in km/h
Calculate approximately how many hours the journey will take.
Formula:
Time = Distance / Speed

Example
Destination: Adama
Distance: 100 km
Average Speed: 50 km/h

Estimated Travel Time: 2 hours

Bonus
Display the result in hours and minutes.

"""

destination = input("Destination: ")
distance_km = int(input("Distance(km): "))
average_speed = float(input("Average speed(km): "))

total_hour = distance_km / average_speed
total_minutes = round(total_hour * 60)
hours,minutes = divmod(total_minutes, 60)

print(f"Estimated Travel Time: {hours} hours {minutes} minutes")