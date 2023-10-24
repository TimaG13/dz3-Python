num = int(input("Введіть 4-х значне число: "))
# Видобути окремі цифри числа та вивести їх в стовпчик
num1 = num // 1000
num2 = (num // 100) % 10
num3 = (num // 10) % 10
num4 = num % 10

print(num1)
print(num2)
print(num3)
print(num4)