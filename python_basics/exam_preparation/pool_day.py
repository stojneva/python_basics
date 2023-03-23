from math import ceil
count_people = int(input())
tax = float(input())
price_one_bed = float(input())
price_one_umbrella = float(input())

all_tax = count_people * tax
price_beds = ceil(count_people * 0.75) * price_one_bed
price_umbrellas = ceil(count_people * 0.50) * price_one_umbrella
end_price = all_tax + price_beds + price_umbrellas

print(f"{end_price:.2f} lv.")

