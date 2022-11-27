type_flower = input()
count_flower = int(input())
budget = int(input())

price = 0

if type_flower == "Roses":
    price = count_flower * 5
    if count_flower > 80:
        price -= price * 0.10

elif type_flower == "Dahlias":
    price = count_flower * 3.80
    if count_flower > 90:
        price -= price * 0.15

elif type_flower == "Tulips":
    price = count_flower * 2.80
    if count_flower > 80:
        price += price * 0.15

elif type_flower == "Narcissus":
    price = count_flower * 3
    if count_flower < 120:
        price -= price * 0.15

elif type_flower == "Gladiolus":
    price = count_flower * 2.50
    if count_flower < 80:
        price += price * 0.20

diff = abs(price - budget)

if budget >= price:
    print(f"Hey, you have a great garden with {count_flower} {type_flower} and {diff:.2f} leva left.")

else:
    print(f"Not enough money, you need {diff:.2f} leva more.")

