import random

# Генеруємо випадковий список від 3 до 10 елементів
lst = [random.randint(1, 100) for _ in range(random.randint(3, 10))]

# Перевірка, чи список має принаймні 3 елементи
if len(lst) >= 3:
    new_list = [lst[0], lst[2], lst[-2]]
    print(lst)
    print(new_list)
else:
    print("Початковий список має менше ніж 3 елементи.")