lenght = int(input())
width = int(input())
all_cake = lenght * width
pieces = 0

command = input()
while command != "STOP":
    cake = int(command)
    pieces += cake

    if pieces > all_cake:
        break

    command = input()

diff = abs(all_cake - pieces)
if pieces > all_cake:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{diff} pieces are left.")
