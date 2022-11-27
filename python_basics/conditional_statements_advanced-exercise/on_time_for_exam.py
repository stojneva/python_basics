hours_exam = int(input())
minutes_exam = int(input())
hours_come = int(input())
minutes_come = int(input())

hours = 0
minutes = 0
total_time_exam = hours_exam * 60 + minutes_exam
total_time_come = hours_come * 60 + minutes_come
dif_time = abs(total_time_exam - total_time_come)

if total_time_exam < total_time_come:
    print('Late')
    if dif_time >= 60:
        hours_late = dif_time // 60
        minutes_late = dif_time % 60
        print(f'{hours_late} : {minutes_late:02d} hours after the start')
    else:
        print(f'{dif_time} minutes after the start')

elif total_time_come <= total_time_exam and dif_time <= 30:
    print('On time')
    if dif_time > 0:
        print(f'{dif_time} minutes before the start')
else:
    print('Early')
    if dif_time >= 60:
        hours_early = dif_time // 60
        minutes_early = dif_time % 60
        print(f'{hours_early}:{minutes_early:02d} hours before the start')
    else:
        print(f'{dif_time} minutes before the start')