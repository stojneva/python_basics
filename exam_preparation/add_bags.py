price_luggage_20_kg = float(input())
kg_luggage = float(input())
days_to_travel = int(input())
count_luggage = int(input())

price = 0

if kg_luggage < 10:
    price = price_luggage_20_kg - (price_luggage_20_kg * 0.80)
elif 10 <= kg_luggage <= 20:
    price = price_luggage_20_kg * 0.50
elif 20 < kg_luggage:
    price = price_luggage_20_kg

if days_to_travel > 30:
    price = price + (price * 0.10)
elif 7 <= days_to_travel <= 30:
    price = price + (price * 0.15)
elif days_to_travel < 7:
    price = price + (price * 0.40)

all_price = price * count_luggage

print(f"The total price of bags is: {all_price:.2f} lv.")