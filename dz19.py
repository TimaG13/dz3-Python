def common_elements():
    mul_3 = [x for  x in range(1,101) if x % 3 == 0]

    mul_5 = [x for x in range(1,101) if x % 5 == 0]

    com_set = set(mul_3) & set(mul_5)

    return com_set

res = common_elements()
print(res)