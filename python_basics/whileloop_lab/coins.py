coins = float(input()) * 100
counter = 0

while True:
    if int(coins) <= 0:
        break
    elif int(coins) >= 200:
        coins -= 200
        counter += 1
    elif int(coins) >= 100:
        coins -= 100
        counter += 1
    elif int(coins) >= 50:
        coins -= 50
        counter += 1
    elif int(coins) >= 20:
        coins -= 20
        counter += 1
    elif int(coins) >= 10:
        coins -= 10
        counter += 1
    elif int(coins) >= 5:
        coins -= 5
        counter += 1
    elif int(coins) >= 2:
        coins -= 2
        counter += 1
    elif int(coins) >= 1:
        coins -= 1
        counter += 1

print(counter)




