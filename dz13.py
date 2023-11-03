import string

input_str = "a-c" # -> abc
# "a-a" # -> a
# "s-H" # -> stuvwxyzABCDEFGH
#  "a-A" # -> abcdefghijklmnopqrstuvwxyzA


# input_str = input("Введіть дві літери через дефіс: ")

# Розбиваємо рядок на дві частини, використовуючи дефіс як роздільник
start_char, end_char = input_str.split('-')

# Знайдемо індекси літер у рядку ascii_letters
start_index = string.ascii_letters.index(start_char)
end_index = string.ascii_letters.index(end_char)

# Отримуємо підрядок від початкового індексу до кінцевого і включно
result_str = string.ascii_letters[start_index:end_index + 1]

print(result_str)