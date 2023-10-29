# lst = [1, 3, 5] # => 30
lst = [6] # => 36
# lst = [] # => 0

if not lst:  # Перевірка на порожній список
    res = 0
else:
    sum_e = 0
    for i in range(0, len(lst), 2):  # Перебираємо парні індекси
        sum_e += lst[i]

    res = sum_e * lst[-1]  # Помножуємо суму на останній елемент

print(res)