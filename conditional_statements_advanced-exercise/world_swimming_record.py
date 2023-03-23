world_rec_sec = float(input())
distance_metres = float(input())
time_in_sec_m = float(input())

metres_to_swim = distance_metres * time_in_sec_m
seconds = (distance_metres // 15)
every_15_metres = seconds * 12.5

all_time = metres_to_swim + every_15_metres

if all_time >= world_rec_sec:
    time = abs(all_time - world_rec_sec)
    print(f"No, he failed! He was {time:.2f} seconds slower.")

else:
    time_not_enough = abs(metres_to_swim + every_15_metres)
    print(f"Yes, he succeeded! The new world record is {time_not_enough:.2f} seconds.")