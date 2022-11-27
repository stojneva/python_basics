from math import floor

time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes_sum = total_time // 60
seconds_sum = total_time % 60

if seconds_sum < 10:
    print(f"{floor(minutes_sum)}:0{seconds_sum}")

else:
    print(f"{minutes_sum}:{seconds_sum}")