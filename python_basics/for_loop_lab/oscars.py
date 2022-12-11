name_actor = input()
points_from_academy = float(input())
count_exam_person = int(input())

points = points_from_academy

for i in range(1, count_exam_person + 1):
    name_exam_person = input()
    points_from_person = float(input())

    current_points = ((len(name_exam_person) * points_from_person) / 2)
    points = points + current_points

    if 1250.5 <= points:
        break

if 1250.5 <= points:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {points:.1f}!")
elif 1250.5 > points:
    diff = abs(points - 1250.50)
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")



