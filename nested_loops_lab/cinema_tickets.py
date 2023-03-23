total_student = 0
total_standart = 0
total_kids = 0

while True:
    movie = input()

    if movie == "Finish":
        break

    capacity = int(input())
    sold_tickets = 0

    while sold_tickets < capacity:
        type_ticket = input()

        if type_ticket == "End":
            break

        if type_ticket == "student":
            total_student += 1
        elif type_ticket == "standart":
            total_standart += 1
        elif type_ticket == "kid":
            total_kids += 1

        sold_tickets += 1

    print(f"{movie} - {sold_tickets/capacity * 100:.2f}% full.")

total_tickets = total_kids + total_standart + total_student

print(f"Total tickets: {total_tickets}")
print(f"{total_student / total_tickets * 100:.2f}% student tickets.")
print(f"{total_standart / total_tickets * 100:.2f}% standart tickets.")
print(f"{total_kids / total_tickets * 100:.2f}% kids tickets.")

