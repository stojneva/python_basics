from math import ceil

height_wall = int(input())
width_wall = int(input())
no_color_percent = int(input()) / 100

litres = 0

all_wall = height_wall * width_wall * 4
walls_to_color = int(all_wall - (all_wall * no_color_percent))

colors = 0
liters = input()

while litres != "Tired!":

    colors += int(liters)

    if walls_to_color == colors:
        print("All walls are painted! Great job, Pesho!")
        break

    if walls_to_color < colors:
        print(f"All walls are painted and you have {int(abs(walls_to_color - colors))} l paint left!")
        break

    liters = input()

    if liters == "Tired!":
        print(f"{ceil(abs(walls_to_color - colors))} quadratic m left.")
        break
