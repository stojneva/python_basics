user = input()
password = input()

user_name = "yana.stoyneva"
user_pass = "12345"

if user == user_name:
    if password == user_pass:
        print("Welcome!")
    else:
        print("Wrong password")
        new_name = input()
        new_password = input()
        print("Welcome!")

else:
    print("Wrong password")
    new_name = input()
    new_password = input()
    print("Welcome!")