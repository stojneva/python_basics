from math import ceil

count_food = int(input())

sugar_all = 0
flour_all = 0
max_sugar = 0
max_flour = 0

for _ in range(count_food):
    sugar = int(input())
    flour = int(input())

    sugar_all += sugar
    flour_all += flour

    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour

packets_sugar = ceil(sugar_all / 950)
packets_flour = ceil(sugar_all / 750)

print(f"Sugar: {packets_sugar}")
print(f"Flour: {packets_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")


