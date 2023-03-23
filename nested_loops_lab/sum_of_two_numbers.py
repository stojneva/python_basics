first_number = int(input())
second_number = int(input())
magic_number = int(input())
counter = 0
flag = False

for a in range(first_number, second_number + 1):
    for b in range(first_number, second_number + 1):
        counter += 1

        result = a + b
        if result == magic_number:
            print(f"Combination N:{counter} ({a} + {b} = {magic_number})")
            flag = True
            break
    if flag:
        break

if not flag:
    print(f"{counter} combinations - neither equals {magic_number}")


