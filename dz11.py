num1 = None

while True:
    num1 = input("Введіть перше число: ")
    if num1 != 'y':
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
    else:
        break