number = int(input())

# for biggest in range(1, 10):
#     for thousands in range(1, 10):
#         for hundreds in range(1, 10):
#             for units in range(1, 10):
#                 if n % biggest == 0 and n % thousands == 0 and n % hundreds == 0 and n % units == 0:
#                     print(f"{biggest}{thousands}{hundreds}{units}", end=" ")

for n in range(1111,10000):
    for digit in str(n):
        if digit == 0:
            break
        if number % int(digit) != 0:
            break
    else:
        print(n, end="")



