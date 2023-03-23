import math

height_wall = int(input())
width_wall = int(input())
no_color_percent = int(input()) / 100
command = input()

paint_total = 0
all_wall = height_wall * width_wall * 4
walls_to_color = all_wall - (all_wall * no_color_percent)

if_tired = False
is_enough = False
no_paint = False

while command != "Tired!":
    paint = int(command)
    paint_total += paint
    walls_to_color -= paint

    if walls_to_color == paint_total:
        is_enough = True
        break

    if walls_to_color < paint_total:
        no_paint = True
        break

    command = input()
    if command == "Tired!":
        if_tired = True
        break

diff = abs(walls_to_color - paint_total)

if if_tired:
    print(f"{walls_to_color} quadratic m left.")
if no_paint:
    print(f"All walls are painted and you have {math.floor(abs(walls_to_color))} l paint left!")
if is_enough:
    print("All walls are painted! Great job, Pesho!")

