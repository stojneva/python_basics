number_one = int(input())
number_two = int(input())


for number in range(number_one, number_two + 1):
    number_str = str(number)
    odd = 0
    even = 0
    for index, digit in enumerate(number_str):
        if index % 2 == 0:
            even += int(digit)
        else:
            odd += int(digit)
    if even == odd:
        print(number, end=" ")