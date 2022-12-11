text = input()

a = 1
e =	2
i = 3
o = 4
u = 5
sum_symbol = 0

for symbol in text:
    if symbol == "a":
        sum_symbol += a
    elif symbol == "e":
        sum_symbol += e
    elif symbol == "i":
        sum_symbol += i
    elif symbol == "o":
        sum_symbol += o
    elif symbol == "u":
        sum_symbol += u
print(sum_symbol)