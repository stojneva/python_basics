budget_peter = float(input())
count_video = int(input())
count_processor = int(input())
ram_count = int(input())



price_one_video = 250 * count_video
processor = price_one_video * 0.35 * count_processor
ram = price_one_video * 0.10 * ram_count

all_price = price_one_video + processor + ram

if count_video > count_processor:
    all_price = all_price - (all_price * 0.15)

if all_price <= budget_peter:
    money_left = budget_peter - all_price
    print(f"You have {money_left:.2f} leva left!")

else:
    need_money  = all_price - budget_peter
    print(f"Not enough money! You need {need_money:.2f} leva more!")
