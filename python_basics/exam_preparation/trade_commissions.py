city = input()
volume_sales = float(input())

flag = False
price = 0

if city == "Sofia":
    if 0 <= volume_sales <= 500:
        price = volume_sales * 0.05
        flag = True
    elif 500 < volume_sales <= 1000:
        price = volume_sales * 0.07
        flag = True
    elif 1000 < volume_sales <= 10000:
        price = volume_sales * 0.08
        flag = True
    elif volume_sales > 10000:
        price = volume_sales * 0.12
        flag = True
    else:
        flag = False

if city == "Varna":
    if 0 <= volume_sales <= 500:
        price = volume_sales * 0.045
        flag = True
    elif 500 < volume_sales <= 1000:
        price = volume_sales * 0.075
        flag = True
    elif 1000 < volume_sales <= 10000:
        price = volume_sales * 0.10
        flag = True
    elif volume_sales > 10000:
        price = volume_sales * 0.13
        flag = True
    else:
        flag = False

if city == "Plovdiv":
    if 0 <= volume_sales <= 500:
        price = volume_sales * 0.055
        flag = True
    elif 500 < volume_sales <= 1000:
        price = volume_sales * 0.08
        flag = True
    elif 1000 < volume_sales <= 10000:
        price = volume_sales * 0.12
        flag = True
    elif volume_sales > 10000:
        price = volume_sales * 0.145
        flag = True
    else:
        flag = False

if flag:
    print(f"{price:.2f}")
else:
    print("error")
