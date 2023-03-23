import math

number_tournaments = int(input())
start_points = int(input())

all_sum = 0
points_tournaments = 0
won = 0

for i in range(0, number_tournaments):
    curr = input()

    if curr == 'W':
        all_sum += 2000
        won += 1

    elif curr == 'F':
        all_sum += 1200

    elif curr == 'SF':
        all_sum += 720

points_tournaments = all_sum + start_points
average = all_sum / number_tournaments
percent = (won/number_tournaments) * 100

print(f"Final points: {points_tournaments}")
print(f"Average points: {math.floor(average)}")
print(f"{percent:.2f}%")