needed_profit = float(input())
all_price = 0

while True:
    coctail = input()

    if coctail == "Party!":
        break

    count_coctail = int(input())
    price_coctail = int(len(coctail))

    price = price_coctail * count_coctail
    if price % 2 != 0:
        price -= price * 0.25
    all_price += price

    if needed_profit <= all_price:
        break

if needed_profit > all_price:
    diff = abs(all_price - needed_profit)
    print(f"We need {diff:.2f} leva more.")
    print(f"Club income - {all_price:.2f} leva.")
else:
    print("Target acquired.")
    print(f"Club income - {all_price:.2f} leva.")