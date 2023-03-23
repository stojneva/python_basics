lenght = int(input())
width = int(input())
pieces = 0

cake = lenght * width

command = input()

while command != "STOP":

    pieces += int(command)

    if pieces >= cake:
        print(f"No more cake left! You need {pieces - cake} pieces more.")
        break

    command = input()

else:
    print(f"{abs(pieces - cake)} pieces are left.")