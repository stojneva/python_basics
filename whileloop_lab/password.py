# username = input()
# password = input()
#
# entry_pass = input()
#
# while entry_pass != password:
#     entry_pass = input()
#
#
# print(f"Welcome {username}!")

username = input()
password = input()

while True:
    data = input()
    if data == password:
        print(f"Welcome {username}!")
        break
