number = int(input())
counter = 0

for row in range(1, number + 1):
    for col in range(1, row + 1):
        counter += 1
        if row != col:
            print(counter, end=" ")
        else:
            print(counter)

        if counter == number:
            exit()