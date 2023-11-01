import string
# ascii_lowercase
def validate_pin(pin):
    num = 0
    for i in list(string.ascii_lowercase):
        print(pin)
        if i == pin:
            num = num + 1
            print(num, i)


validate_pin(list(input('aasd:')))