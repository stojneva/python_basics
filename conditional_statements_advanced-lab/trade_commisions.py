number = int(input())

flag = False

if -100 <= number <= 100 and number != 0:
    flag = True

if flag:
    print("yes")
else:
    print("no")