budget = float(input())
season = input()

destination = ""
place_to_sleep = ""
expenses = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        expenses = budget * 0.30
        place_to_sleep = "Camp"
    else:
        expenses = budget * 0.70
        place_to_sleep = "Hotel"

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        expenses = budget * 0.40
        place_to_sleep = "Camp"
    else:
        expenses = budget * 0.80
        place_to_sleep = "Hotel"


elif budget > 1000:
    destination = "Europe"
    expenses = budget * 0.90
    place_to_sleep = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place_to_sleep} - {expenses:.2f}")