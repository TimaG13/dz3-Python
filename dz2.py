input_list = [1, 2, 3, 4, 5, 6, 7]
result = []

if len(input_list) % 2 == 0:
    # Якщо у списку парна кількість елементів
    midpoint = len(input_list) // 2
    first_half = input_list[:midpoint]
    second_half = input_list[midpoint:]
else:
    # Якщо у списку непарна кількість елементів
    midpoint = len(input_list) // 2 + 1
    first_half = input_list[:midpoint]
    second_half = input_list[midpoint:]

result = [first_half, second_half]
print(result)