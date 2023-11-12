def add_one(some_list):
    # Перетворюємо список цифр у число
    num = int(''.join(map(str, some_list)))

    # Додаємо 1 до числа
    num += 1

    # Розбиваємо отримане число на список цифр
    result_list = [int(digit) for digit in str(num)]

    return result_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")