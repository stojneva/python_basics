import sys

n = int(input())
sum_numbers = 0

max_num = -sys.maxsize
for i in range(1, n + 1):
    current_num = int(input())

    if current_num > max_num:
        max_num = current_num

    sum_numbers = sum_numbers + current_num
    total_sum = sum_numbers - max_num

if total_sum == max_num:
    print("Yes")
    print(f"Sum = {total_sum}")
else:
    diff = abs(total_sum - max_num)
    print("No")
    print(f"Diff = {diff}")
