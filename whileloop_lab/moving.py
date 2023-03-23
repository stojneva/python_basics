width = int(input())
lenght = int(input())
height = int(input())

count_boxes = 0

command = input()
while command != "Done":
    boxes = int(command)
    count_boxes += boxes

    volume = width * lenght * height
    if volume <= count_boxes:
        break

    command = input()

diff = abs(volume - count_boxes)
if volume < count_boxes:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")

