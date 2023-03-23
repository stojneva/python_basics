command = input()
height = 5364
everest = 8848
days = 1

flag = False

while command != "END":
    climbed_height = int(input())

    if command == "Yes":
        days += 1

    if days > 5:
        break

    height += climbed_height

    if height >= everest:
        flag = True
        break

    command = input()

if flag:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(f"{height}")