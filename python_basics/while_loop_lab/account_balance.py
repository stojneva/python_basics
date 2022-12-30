money = 0

while True:
    command = input()

    if command == "NoMoreMoney":
        break
    if float(command) < 0:
        print("Invalid operation!")
        break
    else:
        money += float(command)
        print(f"Increase: {float(command):.2f}")

print(f"Total: {float(money):.2f}")