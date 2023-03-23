number_of_days = int(input())
number_of_hours = int(input())
costs = 0

for day in range(1, number_of_days + 1):
    parking = 0

    for hour in range(1, number_of_hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            parking += 2.50
            costs += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            parking += 1.25
            costs += 1.25
        else:
            parking += 1
            costs += 1


    print(f"Day: {day} - {parking:.2f} leva")
print(f"Total: {costs:.2f} leva")

