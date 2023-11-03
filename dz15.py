 # 0 #-> 0 днів, 00:00:00
# 224930 #-> 2 дні, 14:28:50
# 466289 #-> 5 днів, 09:31:29
# 950400 #-> 11 днів, 00:00:00
# 1209600 #-> 14 днів, 00:00:00
# 1900800 #- > 22 дні, 00:00:00
# 8639999 #-> 99 днів, 23:59:59
# 22493 #-> 0 днів, 06:14:53
seconds = 7948799 #-> 91 день, 23:59:59


# Отримуємо введене число від користувача
# seconds = int(input("Введіть кількість секунд (0-8640000): "))

if 0 <= seconds < 8640000:
    days, seconds = divmod(seconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)

    # Форматуємо результат
    time_str = f"{days} днів, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    if days == 1:
        time_str = time_str.replace("днів", "день")

    print(time_str)
else:
    print("Некоректне введення. Введіть число в межах від 0 до 8640000.")