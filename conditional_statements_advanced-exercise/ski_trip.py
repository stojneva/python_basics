days_stay = int(input())
place_sleep = input()
grade = input()

price_room = 0
price_apartment = 0
price_president = 0

if place_sleep == "room for one person":
    price_room = (days_stay - 1) * 18
    if grade == "positive":
        price_room += price_room * 0.25
    elif grade == "negative":
        price_room -= price_room * 0.10
    print(f"{price_room:.2f}")

if place_sleep == "apartment":
    price_apartment = (days_stay - 1) * 25
    if 10 >= days_stay:
        price_apartment = price_apartment - (price_apartment * 0.30)
        if grade == "positive":
            price_apartment += price_apartment * 0.25
        elif grade == "negative":
            price_apartment -= price_apartment * 0.10
    elif 10 < days_stay <= 15:
        price_apartment = price_apartment - (price_apartment * 0.35)
        if grade == "positive":
            price_apartment += price_apartment * 0.25
        elif grade == "negative":
            price_apartment -= price_apartment * 0.10
    elif days_stay > 15:
        price_apartment = price_apartment - (price_apartment * 0.50)
        if grade == "positive":
            price_apartment += price_apartment * 0.25
        elif grade == "negative":
            price_apartment -= price_apartment * 0.10
    print(f"{price_apartment:.2f}")

if place_sleep == "president apartment":
    price_president = (days_stay - 1) * 35
    if 10 >= days_stay:
        price_president = price_president - (price_president * 0.10)
        if grade == "positive":
            price_president += price_president * 0.25
        elif grade == "negative":
            price_president -= price_president * 0.10
    elif 10 < days_stay < 15:
        price_president = price_president - (price_president * 0.15)
        if grade == "positive":
            price_president += price_president * 0.25
        elif grade == "negative":
            price_president -= price_president * 0.10
    elif days_stay > 15:
        price_president = price_president - (price_president * 0.20)
        if grade == "positive":
            price_president += price_president * 0.25
        elif grade == "negative":
            price_president -= price_president * 0.10
    print(f"{price_president:.2f}")