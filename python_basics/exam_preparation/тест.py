day = int(input())
hour_per_day = int(input())

money = 0
days = 0
total = 0

for n in range(1, day + 1):
    for x in range(1, hour_per_day + 1):
        if n % 2 == 0 and x % 2 != 0:
            money += 2.50
        elif n % 2 != 0 and x % 2 == 0:
            money += 1.25
        else:
            money += 1
    days += 1
    print(f"Day: {n} - {money:.2f} leva")
    total += money
    money = 0

print(f"Total: {total:.2f} leva")
