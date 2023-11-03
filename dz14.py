# '1000' #-> 0
# 423 #-> 8
# 33 #-> 9
# 25 #-> 0
# 1 #-> 1
user_input = input("Введіть ціле число: ")

while len(user_input) > 1:
    prod = 1
    for digit in user_input:
        prod *= int(digit)
    user_input = str(prod)

result = int(user_input)
print(result)