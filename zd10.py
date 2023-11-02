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
# "assert" #=> True
# "and " #=> True

import keyword
import string

name_var = input("Введіть назву: ")

# Перевірка, чи починається ім'я змінної з цифри
if name_var[0].isdigit():
    print(False)
# Перевірка, чи складається ім'я тільки з цифр
elif name_var.isdigit():
    print(False)
# Перевірка, чи містить рядок великі літери, пробіли та знаки пунктуації (окрім нижнього підкреслення "_")
elif any(symb.isupper() or symb in string.punctuation for symb in name_var if symb != "_"):
    print(False)
# Перевірка, чи рядок містить лише дозволені символи
elif not all(symb.isalnum() or symb == "_" for symb in name_var):
    print(False)
# чи ім'я не є зарезервованим словом
elif name_var in keyword.kwlist:
    print(False)
else:
    print(True)