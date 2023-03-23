numbers = input()

for n in range(1, int(numbers[2]) + 1):
    for x in range(1, int(numbers[1]) + 1):
        for z in range(1, int(numbers[0]) + 1):
            result = n * x * z
            print(f"{n} * {x} * {z} = {result};")