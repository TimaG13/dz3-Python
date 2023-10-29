num1 = float(input("Введіть перше число: "))
operator = input("Введіть операцію (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))
#//
if operator == '+':
    result = num1 + num2
    print(f"Результат: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"Результат: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"Результат: {result}")
elif operator == '/':
    if num2 == 0:
        print("Помилка: дільник не може бути 0.")
    else:
        result = num1 / num2
        print(f"Результат: {result}")
else:
    print("Непідтримувана операція.")