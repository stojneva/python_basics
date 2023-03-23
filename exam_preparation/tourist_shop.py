budget = float(input())
costs = 0
count_products = 0

while True:
    name = input()

    if name == "Stop":
        break

    product_price = float(input())

    count_products += 1
    if count_products % 3 == 0:
        product_price /= 2

    if product_price > budget:
        count_products -= 1
        break

    costs += product_price
    budget -= product_price

if product_price > budget:
    diff = abs(product_price - budget)
    print(f"You don't have enough money!")
    print(f"You need {diff:.2f} leva!")
else:
    print(f"You bought {count_products} products for {costs:.2f} leva.")




