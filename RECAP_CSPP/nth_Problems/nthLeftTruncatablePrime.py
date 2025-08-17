def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i ==0:
            return False
    return True


def leftTruncatable(x):
    while x > 0:
        if x % 10 == 0:
            return False
        x = x // 10
    return True


def counter(n):
    c = 0
    while n != 0:
        c = c + 1
        n = n // 10
    return c


def isLeftTruncatable(n):
    if leftTruncatable(n):
        p = counter(n)
        while p >= 1:
            n = n % (10 ** (p))
            if not isPrime(n):
                return False
            p -= 1
        return True
    return False


def nthLeftTruncatablePrime(x):
    count = -1
    num = 2
    while x != count:
        if isLeftTruncatable(num):
            count = count + 1
        num = num + 1
    return num - 1


print(nthLeftTruncatablePrime(int(input())))
