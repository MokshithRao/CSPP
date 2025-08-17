def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0 :
            return False
    return True

def sum_of_squares(n):
    t = 0
    while n > 0:
        rem = n % 10
        t += rem * rem
        n = n // 10
    return t

def isHappy(n):
    l1 = []
    while n != 1:
        if n in l1:
            return False
        l1.append(n)
        n = sum_of_squares(n)
    return True

def isHappyPrime(n):
    return isHappy(n) and isPrime(n)

def nthHappyPrime(n):
    count = 0
    num = 7
    while count <= n:
        if isHappyPrime(num):
            if count == n:
                return num
            count += 1
        num += 1

print(nthHappyPrime(int(input())))
