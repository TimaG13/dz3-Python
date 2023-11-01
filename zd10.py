import string

# "_" #=> True
# "x" #=> True
# "get_value" #=> True
# "get value" #=> False
# "get!value" #=> False
# "some_super_puper_value" #=> True
#  "Get_value" #=> False
# "get_Value" #=> False
# "getValue" #=> False
# "3m" #=> False
# "m3" #=> True

# Введення рядка від користувача
name_var = input("Введіть назву: ")

# Перевірка, чи починається ім'я змінної з цифри
if name_var[0].isdigit():
    print(False)
# Перевірка, чи складається ім'я тільки з цифр
elif name_var.isdigit():
    print(False)
# Перевірка, чи містить рядок великі або малі літери, цифри та символ нижнього підкреслення
elif all(symb.isalnum() or symb == "_" for symb in name_var):
    # Перевірка, чи всі літери є малими
    if name_var.islower() or name_var == "_":
        print(True)
    else:
        print(False)
else:
    print(False)