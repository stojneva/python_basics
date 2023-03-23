dollars_processor = float(input()) * 1.57
dollars_video = float(input()) * 1.57
dollars_RAM = float(input()) * 1.57
ram_count = int(input())
discount = float(input())

all_price_ram = dollars_RAM * ram_count
all_processor = dollars_processor - (dollars_processor * discount)
all_video = dollars_video - (dollars_video * discount)

all = all_processor + all_video + all_price_ram

print(f"Money needed - {all:.2f} leva.")


