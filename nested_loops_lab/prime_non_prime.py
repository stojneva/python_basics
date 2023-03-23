count_prime = 0
count_nonprime = 0

command = input()
while command != "stop":
    number = int(command)

    if number < 0:
        print("Number is negative.")
        command = input()
        continue

    count = 0

    for n in range(1, number + 1):
        if number % n == 0:
            count += 1
    if count == 2:
        count_prime += number
    else:
        count_nonprime += number
    command = input()


print(f"Sum of all prime numbers is: {count_prime}")
print(f"Sum of all non prime numbers is: {count_nonprime}")
