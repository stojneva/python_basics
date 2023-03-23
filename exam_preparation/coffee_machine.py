import math

drink = input()
sugar = input()
count_drinks = int(input())

price = 0


if drink == "Espresso":
    if sugar == "Without":
        price = count_drinks * 0.90
        if count_drinks >= 5:
            price = price - (price * 0.25)

    elif sugar == "Normal":
        price = count_drinks * 1.00
        if count_drinks >= 5:
            price = price - (price * 0.25)

    elif sugar == "Extra":
        price = count_drinks * 1.20
        if count_drinks >= 5:
            price = price - (price * 0.25)

if drink == "Cappuccino":
    if sugar == "Without":
        price = count_drinks * 1.00

    elif sugar == "Normal":
        price = count_drinks * 1.20

    elif sugar == "Extra":
        price = count_drinks * 1.60

if drink == "Tea":
    if sugar == "Without":
        price = count_drinks * 0.50

    elif sugar == "Normal":
        price = count_drinks * 0.60

    elif sugar == "Extra":
        price = count_drinks * 0.70

if sugar == "Without":
    price = price - (price * 0.35)

if price > 15:
    price = price - (price * 0.20)

print(f"You bought {count_drinks} cups of {drink} for {price:.2f} lv.")
