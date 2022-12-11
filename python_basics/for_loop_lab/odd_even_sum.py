numbers = int(input())

even = 0
odd = 0

sum_num = 0
for i in range(1, numbers + 1):
    current_num = int(input())
    if i % 2 == 0:
        even += current_num
    else:
        odd += current_num

different = abs(even - odd)

if even == odd:
    print("Yes")
    print(f"Sum = {even}")

else:
    print("No")
    print(f"Diff = {different}")


