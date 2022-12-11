open_tabs = int(input())
init_salary = int(input())

salary = init_salary

for i in range(open_tabs):
    name_website = input()

    if name_website == "Facebook":
        salary = salary - 150
    elif name_website == "Instagram":
        salary = salary - 100
    elif name_website == "Reddit":
        salary = salary - 50

    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)
