money_needed = float(input())
my_money = float(input())

days_total = 0
spend_days = 0

while my_money < money_needed:
    if spend_days == 5:
        break
    action = input()
    money_spend_save = float(input())

    days_total += 1

    if action == "spend":
        spend_days += 1
        my_money = my_money - money_spend_save
        if my_money < 0:
            my_money = 0

    elif action == "save":
        spend_days = 0
        my_money = my_money + money_spend_save


if spend_days == 5:
    print(f"You can't save the money.")
    print(days_total)
else:
    print(f"You saved the money for {days_total} days.")




