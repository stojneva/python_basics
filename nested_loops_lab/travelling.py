while True:
    destination = input()

    if destination == "End":
        break

    min_budget = float(input())

    while True:
        if min_budget <= 0:
            print(f"Going to {destination}!")
            break
        salary = float(input())

        min_budget -= salary
