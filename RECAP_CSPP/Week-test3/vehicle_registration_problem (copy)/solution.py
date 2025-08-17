def Validate_reg_num(s):
    up = 0
    d = 0
    a = 0
    if len(s) > 8:
        return False
    for i in s:
        if i.isupper():
            up+=1
        if i.isnumeric():
            d += 1
        if i.isalnum():
            a += 1
    if up>=2 and d >= 2:
        return True
    return False
print(Validate_reg_num(input()))
