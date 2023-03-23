contract_time = input()
type_contract = input()
mobile_internet = input()
count_months = int(input())
tax = 0

if type_contract == "Small":
    if contract_time == "one":
        tax = 9.98
    elif contract_time == "two":
        tax = 8.58
elif type_contract == "Middle":
    if contract_time == "one":
        tax = 18.99
    elif contract_time == "two":
        tax = 17.09
elif type_contract == "Large":
    if contract_time == "one":
        tax = 25.98
    elif contract_time == "two":
        tax = 23.59
elif type_contract == "ExtraLarge":
    if contract_time == "one":
        tax = 35.99
    elif contract_time == "two":
        tax = 31.79

if mobile_internet == "yes":
    if tax <= 10:
        tax += 5.50
    elif tax <= 30:
        tax += 4.35
    elif tax > 30:
        tax += 3.85

end_price = tax * count_months

if contract_time == "two":
    end_price -= end_price * 0.0375

print(f"{end_price:.2f} lv.")





