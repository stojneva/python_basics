numbers = int(input())

sum_left = 0
sum_right = 0

for i in range(numbers):
    num1 = int(input())
    sum_left += num1

for x in range(numbers):
    num2 = int(input())
    sum_right += num2

if sum_left == sum_right:
    print(f"Yes, sum = {sum_right}")
else:
    print(f"No, diff = {abs(sum_right - sum_left)}")
