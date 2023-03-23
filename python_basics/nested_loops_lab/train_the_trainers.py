count_jury = int(input())
presentation = input()
sum_grades = 0
counter = 0
sum_all = 0
counter_sum_all = 0

while presentation != "Finish":

    for jury in range(1, count_jury + 1):
        grades = float(input())
        sum_grades += grades
        sum_all += grades
        counter += 1
        counter_sum_all += 1

    print(f"{presentation} - {sum_grades / counter:.2f}.")
    sum_grades = 0
    counter = 0

    average_grade = sum_all / count_jury

    presentation = input()

average = sum_all / counter_sum_all
print(f"Student's final assessment is {average:.2f}.")



