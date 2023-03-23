judges = int(input())
total_grades = 0
all_grades = 0

while True:
    command = input()
    if command == "Finish":
        break

    grades_sum = 0

    for _ in range(judges):
        grades_sum += float(input())
    total_grades += grades_sum
    all_grades += judges
    print(f"{command} - {grades_sum / judges:.2f}.")

print(f"Student's final assessment is {total_grades/all_grades:.2f}.")

