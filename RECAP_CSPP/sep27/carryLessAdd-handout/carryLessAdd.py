def carrylessAdd(x, y):
    r = 0
    p = 1

    while x > 0 or y > 0:
        dig_x = x % 10
        dig_y = y % 10
        c_d = (dig_x + dig_y) % 10
        r += c_d * p
        x //= 10
        y //= 10
        p *= 10

    return r

print(carrylessAdd(int(input()), int(input())))