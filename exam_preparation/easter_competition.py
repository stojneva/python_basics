count_bake = int(input())
best_baker = ""
best_baker_score = 0

for _ in range(count_bake):
    name = input()
    current_score = 0

    while True:
        command = input()

        if command == "Stop":
            print(f"{name} has {current_score} points.")
            break
        current_score += int(command)
    if current_score > best_baker_score:
        best_baker_name = name
        best_baker_score = current_score
        print(f"{name} is the new number 1!")

print(f"{best_baker} won competition with {best_baker_score} points!")

