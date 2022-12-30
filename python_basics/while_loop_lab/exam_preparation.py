count_bad_grades = int(input())

average_grade = 0
number_problems = 0
last_problem = ""
bad_grades = 0

while True:

    problem_name = input()

    if problem_name == "Enough":
        break
    grade = int(input())

    if grade <= 4:
        bad_grades += 1
        if bad_grades == count_bad_grades:
            break

    average_grade += grade
    number_problems += 1
    last_problem = problem_name
    average = average_grade / number_problems

if bad_grades == count_bad_grades:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {number_problems}")
    print(f"Last problem: {last_problem}")
