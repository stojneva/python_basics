count_tours = int(input())
points = int(input())

sf_point = 0
f_points = 0
w_points = 0
win = 0

for i in range(1, count_tours + 1):
    stage_tour = input()

    if stage_tour == "W":
        win += 1
        points += 2000
        w_points += 2000
    elif stage_tour == "F":
        points += 1200
        f_points += 1200
    elif stage_tour == "SF":
        points += 720
        sf_point += 720

all_points = int((w_points + f_points + sf_point) / count_tours)
percent_win = (win / count_tours) * 100

print(f"Final points: {points}")
print(f"Average points: {all_points}")
print(f"{percent_win:.2f}%")
