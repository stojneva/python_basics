budget = int(input())
season = input()
count_fisher = int(input())

boat_rent = 0

if season == "Spring":
    boat_rent = 3000

elif season == "Summer" or season == "Autumn":
    boat_rent = 4200

elif season == "Winter":
    boat_rent = 2600

if count_fisher <= 6:
    boat_rent -= boat_rent * 0.10

elif 7 < count_fisher <= 11:
    boat_rent -= boat_rent * 0.15

elif count_fisher > 12:
    boat_rent -= boat_rent * 0.25

if count_fisher % 2 == 0 and season != "Autumn":
    boat_rent -= boat_rent * 0.05

diff = abs(boat_rent - budget)

if budget >= boat_rent:
    print(f"Yes! You have {diff:.2f} leva left.")

else:
    print(f"Not enough money! You need {diff:.2f} leva.")
