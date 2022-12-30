name = input()
grades = 0
failed_years = 0
all_grades = 0

while True:
    annual_grade = float(input())
    grades += 1

    if annual_grade < 4:
        failed_years += 1
        if failed_years == 2:
            print(f"{name} has been excluded at {grades} grade")
            break
        grades -= 1
    else:
        all_grades += annual_grade

    if grades == 12:
        mid_grade = all_grades / 12
        print(f"{name} graduated. Average grade: {mid_grade:.2f}")
        break





