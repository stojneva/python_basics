cinema_project = input()
rows = int(input())
columns = int(input())

price = 0
flag = False

incomes_full_cinema = rows * columns

if cinema_project == "Premiere":
    price = incomes_full_cinema * 12.00
    flag = True

elif cinema_project == "Normal":
    price = incomes_full_cinema * 7.50
    flag = True

elif cinema_project == "Discount":
    price = incomes_full_cinema * 5.00
    flag = True

if flag:
    print(f"{price:.2f}")

else:
    print("Try again.")
