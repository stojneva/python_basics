computers = int(input())
rating = 0
all_rating = 0

for _ in range(computers):
    num = input()

    rating = int(num[-1])
    sales = int(num[0] + num[1])
    all_rating += rating

    if rating == 2:
        sales = 0
    if rating == 3:
        sales *= 0.50
    elif rating == 4:
        sales *= 0.70
    elif rating == 5:
        sales *= 0.85
    elif rating == 6:
        sales *= 0.100

print(int(all_rating / num))




