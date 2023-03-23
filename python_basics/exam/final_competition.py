count_dancers = int(input())
count_points = float(input())
season = input()
country = input()
expenses = 0

money_win = count_dancers * count_points

if country == "Bulgaria":
    money_win = count_dancers * count_points
    if season == "summer":
        expenses = money_win - (money_win * 0.05)
    elif season == "winter":
        expenses = money_win - (money_win * 0.08)
elif country == "Abroad":
    money_win += (money_win * 0.50)
    if season == "summer":
        expenses = money_win - (money_win * 0.10)
    elif season == "winter":
        expenses = money_win - (money_win * 0.15)

charity = expenses * 0.75
money_left = expenses - charity
money_dancer = money_left / count_dancers

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_dancer:.2f}")