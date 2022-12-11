age_lilly = int(input())
price_wash_machine = float(input())
price_per_toy = int(input())

toy_count = 0
money_save = 0
total_sum = 0
brother_took = 0

for i in range(1, age_lilly +1):
    if i % 2 != 0:
        toy_count = toy_count + 1
    else:
        brother_took = brother_took + 1
        money_save = money_save + 10
        total_sum = total_sum + money_save

result = (toy_count * price_per_toy) + total_sum - brother_took

diff = abs(result - price_wash_machine)
if result >= price_wash_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")






