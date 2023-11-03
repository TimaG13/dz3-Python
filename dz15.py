seconds =  0 #-> 0 днів, 00:00:00
# 224930 #-> 2 дні, 14:28:50
# 466289 #-> 5 днів, 09:31:29
# 950400 #-> 11 днів, 00:00:00
# 1209600 #-> 14 днів, 00:00:00
# 1900800 #- > 22 дні, 00:00:00
# 8639999 #-> 99 днів, 23:59:59
# 22493 #-> 0 днів, 06:14:53
# 7948799  # -> 91 день, 23:59:59


# seconds = int(input("Введіть кількість секунд (0-8640000): "))

if 0 <= seconds < 8640000:
    days, seconds = divmod(seconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)

    if days % 10 == 1 and days % 100 != 11:
        day_label = "день"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        day_label = "дні"
    else:
        day_label = "днів"

    time_str = f"{days} {day_label}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

    print(time_str)
else:
    print("Некоректне введення. Введіть число в межах від 0 до 8640000.")
