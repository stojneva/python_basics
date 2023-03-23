# name = "abcde"
# name = name[:2]
# print(name)
ticket_price = 0
value_voucher = int(input())
suma = 0
command = input()

while command != "End":

    if len(command) >= 8:
        ticket_price = command[:2]

        for symbol in ticket_price:
            suma += ord(symbol)

    if len(command) < 8:
        if len(command) >= 8:
            ticket_price = ord(command[0])
            suma += ticket_price

        print(suma)




    command = input()



