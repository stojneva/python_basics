from math import ceil

movie_name = input()
movie_long = int(input())
break_long = int(input())

lunch_time = break_long / 8
break_time = break_long / 4

time_left = break_long - lunch_time - break_time

result = ceil(abs(time_left - movie_long))

if time_left >= movie_long:
    print(f"You have enough time to watch {movie_name} and left with {result} minutes free time.")

else:
    print(f"You don't have enough time to watch {movie_name}, you need {result} more minutes.")
