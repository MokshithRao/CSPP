def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    return True


def rotateNumber(x):
    num_digits = 0
    n = x
    while n > 0:
        n //= 10
        num_digits += 1

    if num_digits == 1:
        return x

    last_digit = x % 10
    x //= 10
    x += last_digit * (10 ** (num_digits - 1))
    return x


def isCircularPrime(x):
    rotation = x
    digits_count = 0
    n = x

    while n > 0:
        n //= 10
        digits_count += 1

    for i in range(digits_count):
        if not isPrime(rotation):
            return False
        rotation = rotateNumber(rotation)

    return True


def nthCircularPrime(n):
    c = 0
    num = 2

    while True:
        if isCircularPrime(num):
            c += 1
            if c == n:
                return num
        num += 1


print(nthCircularPrime(int(input())))
