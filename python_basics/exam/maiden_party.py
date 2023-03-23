price_girls_party = float(input())

love_wish = int(input())
roses = int(input())
keys = int(input())
caricatures = int(input())
wishes = int(input())

all_price = (love_wish * 0.60) + (roses * 7.20) + (keys * 3.60) + (caricatures * 18.20) + (wishes * 22)
count = love_wish + roses + keys + caricatures + wishes

if count >= 25:
    all_price -= (all_price * 0.35)

hosting = all_price - (all_price * 0.10)

if hosting > price_girls_party:
    print(f"Yes! {hosting - price_girls_party:.2f} lv left.")
else:
    print(f"Not enough money! {abs(price_girls_party - hosting):.2f} lv needed.")


