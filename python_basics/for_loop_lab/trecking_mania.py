count_group = int(input())

musala_sum = 0
monblan_sum = 0
kilimanjaro_sum = 0
k2_sum = 0
everest_sum = 0

all_people = 0

for i in range(1, count_group + 1):
    people = int(input())
    all_people += people

    if people <= 5:
        musala_sum = musala_sum + people
    elif people <= 12:
        monblan_sum = monblan_sum + people
    elif people <= 25:
        kilimanjaro_sum = kilimanjaro_sum + people
    elif people <= 40:
        k2_sum = k2_sum + people
    elif people > 40:
        everest_sum = everest_sum + people

percent_musala = musala_sum / all_people * 100
percent_monblan = monblan_sum / all_people * 100
percent_kilimanjaro = kilimanjaro_sum / all_people * 100
percent_k2 = k2_sum / all_people * 100
percent_everest = everest_sum / all_people * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")

