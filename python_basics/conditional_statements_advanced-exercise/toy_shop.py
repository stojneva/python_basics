trip_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle = 2.60
talking_doll = 3
teddy_bear = 4.10
minion = 8.20
truck = 2

all_price = (puzzle_count * puzzle) + (dolls_count * talking_doll) + \
           (bears_count * 4.10) + (minions_count * minion) + (trucks_count * truck)

all_toys_count = puzzle_count + dolls_count + bears_count + minions_count + trucks_count

if all_toys_count >= 50:
    all_price = all_price - (all_price * 0.25)

rent = all_price * 0.10

profit = all_price - rent
result = abs(profit - trip_price)

if trip_price <= profit:
    print(f"Yes! {result:.2f} lv left.")

else:
    print(f"Not enough money! {result:.2f} lv needed.")