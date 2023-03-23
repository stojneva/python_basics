budget_movie = float(input())
statist_count = int(input())
cloth_per_statist = float(input())

decor_movie = budget_movie * 0.10
clothes_price = statist_count * cloth_per_statist

if statist_count > 150:
    clothes_price = clothes_price * 0.90

all_price_movie = decor_movie + clothes_price

money_left = abs(budget_movie - all_price_movie)

if budget_movie >= all_price_movie:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")

else:
    print("Not enough money!")
    print(f"Wingard needs {money_left:.2f} leva more.")