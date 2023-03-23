city = input()
package = input()
vip = input()
days = int(input())
price_per_night = 0

if days > 7:
    days -= 1

if city == "Bansko" or city == "Borovets":
    if package == "noEquipment":
        price_per_night = days * 80
        if vip == "yes":
            price_per_night = price_per_night - (price_per_night * 0.05)
    elif package == "withEquipment":
        price_per_night = days * 100
        if vip == "yes":
            price_per_night = price_per_night - (price_per_night * 0.10)
    if days < 1:
        print("Days must be positive number!")
    else:
        print(f"The price is {price_per_night:.2f}lv! Have a nice time!")

elif city == "Varna" or city == "Burgas":
    if package == "withBreakfast":
        price_per_night = days * 130
        if vip == "yes":
            price_per_night = price_per_night - (price_per_night * 0.12)
    elif package == "noBreakfast":
        price_per_night = days * 100
        if vip == "yes":
            price_per_night = price_per_night - (price_per_night * 0.07)
    if days < 1:
        print("Days must be positive number!")
    else:
        print(f"The price is {price_per_night:.2f}lv! Have a nice time!")

else:
    print("Invalid input!")