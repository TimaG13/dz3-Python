# lst = [0, 1, 0, 12, 3] # [1, 12, 3, 0, 0]
# lst = [0] #-> [0]
# lst =[1, 0, 13, 0, 0, 0, 5] # [1, 13, 5, 0, 0, 0, 0]
lst =[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] # [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

# Видалення нулів зі списку
not_Null = [x for x in lst if x != 0]

# Знайдення кількості нулів
len_Null = len(lst) - len(not_Null)

# Формування нового списку
new_lst = not_Null + [0] * len_Null

print(new_lst)