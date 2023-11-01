while True:
    num1 = input("Введіть перше число: ")
    operator = input("Введіть операцію (+, -, *, /): ")
    num2 = input("Введіть друге число: ")
    # //

    if operator == '+':
        result = float(num1) + float(num2)
        print(result)
    elif operator == '-':
        result = float(num1) - float(num2)
        print(result)
    elif operator == '*':
        result = float(num1) * float(num2)
        print(result)
    elif operator == '/':
        if num2 == 0:
            print("Помилка: дільник не може бути 0.")
        else:
            result = float(num1) / float(num2)
            print(result)
    else:
        print("Непідтримувана операція.")
    # Питаємо користувача, чи він хоче продовжити роботу
    response = input("Бажаєте продовжити? (y/n): ")
    if response.lower() != 'y':
        break