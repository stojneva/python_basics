count_visitors = int(input())
back = 0
chest = 0
legs = 0
abs_activity = 0
shake = 0
bar = 0


for _ in range(count_visitors):
    activity = input()

    if activity == "Back":
        back += 1
    elif activity == "Chest":
        chest += 1
    elif activity == "Legs":
        legs += 1
    elif activity == "Abs":
        abs_activity += 1
    elif activity == "Protein shake":
        shake += 1
    elif activity == "Protein bar":
        bar += 1

work_out = back + chest + abs_activity + legs
eat = shake + bar

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_activity} - abs")
print(f"{shake} - protein shake")
print(f"{bar} - protein bar")
print(f"{work_out/count_visitors * 100:.2f}% - work out")
print(f"{eat/count_visitors * 100:.2f}% - protein")


