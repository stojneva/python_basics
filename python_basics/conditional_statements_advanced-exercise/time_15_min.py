hour = int(input())
minutes = int(input())

total_time_minutes = (hour * 60) + minutes + 15

hours = total_time_minutes // 60
minutes = total_time_minutes % 60

if hours >23:
    hours = 0

if minutes < 10:
   print(f"{hours}:0{minutes}")

else:
    print(f"{hours}:{minutes}")