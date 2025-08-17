def prime_factors(n):
    f = []
    d = 2
    while n > 1:
        while n % d == 0:
            f.append(d)
            n //= d
        d += 1
    return f

def prime_factors_dict(lst):
    f_dict = {}
    for num in lst:
        f_dict[num] = prime_factors(num)
    return f_dict
print(prime_factors_dict(eval(input())))