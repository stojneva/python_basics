month = input()
nights_count = int(input())
place_to_sleep = ""
price_studio = 0
price_apartment = 0
discount = 0


if month == "May" or month == "October":
    price_studio = nights_count * 50
    price_apartment = nights_count * 65
    if 7 < nights_count <= 14:
        price_studio -= price_studio * 0.05
        price_apartment = nights_count * 65
    elif nights_count > 14:
        price_studio -= price_studio * 0.30
        price_apartment -= price_apartment * 0.10

elif month == "June" or month == "September":
    price_studio = nights_count * 75.20
    price_apartment = nights_count * 68.70
    if nights_count > 14:
        price_studio -= price_studio * 0.20
        price_apartment -= price_apartment * 0.10

elif month == "July" or month == "August":
    price_studio = nights_count * 76
    price_apartment = nights_count * 77
    if nights_count > 14:
        price_apartment -= price_apartment * 0.10

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")




