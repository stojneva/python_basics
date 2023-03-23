unique_number = int(input())
current_sum = 0

while True:
    current_number = int(input())
    current_sum += current_number

    if current_sum >= unique_number:
        print(current_sum)
        break

# unique_number = int(input())
# current_sum = 0
#
# while current_sum < unique_number:
#     current_number = int(input())
#     current_sum += current_number
#
# print(current_sum)
