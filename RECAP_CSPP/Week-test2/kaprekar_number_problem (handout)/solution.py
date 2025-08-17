def karprekar_number(n):
    d = n*n
    digits = 0
    temp = n
    while temp > 0:
        digits += 1
        temp //= 10

    right_part = d%(10 ** digits)
    left_part = d // (10 ** digits)
    return (left_part + right_part) == n

print(karprekar_number(int(input())))
        