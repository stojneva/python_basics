first_book = input()
books = input()
count = 0

while books != "No More Books":
    if books == first_book:
        print(f"You checked {count} books and found it.")
        break
    count += 1
    books = input()

else:
    print(f"The book you search is not here!")
    print(f"You checked {count} books.")



