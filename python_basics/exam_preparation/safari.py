budget = float(input())
litres = float(input())
day_of_week = input()

price_litres = litres * 2.10
price_tour = price_litres + 100

if day_of_week == "Sunday":
    price_tour -= (price_tour * 0.20)
elif day_of_week == "Saturday":
    price_tour -= (price_tour * 0.10)

if budget >= price_tour:
    print(f"Safari time! Money left: {abs(budget - price_tour):.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {abs(budget - price_tour):.2f} lv.")




