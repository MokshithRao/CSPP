def is_Prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def counter(n):
    c = 0
    while n != 0:
        c = c + 1
        n = n // 10
    return c

def LeftTruncatable(n):
    while(n>0):
        if n%10 == 0:
            return False
        n =n//10
    return True

def IsLeftTruncatablePrime(n):
    if LeftTruncatable(n):
        x = counter(n)
        while(x>=1):
            n = n%(10**(x))
            if not is_Prime(n):
                return False
            x-=1
        return True
    return False


def nthLeftTruncatablePrime(n):
    c =-1
    i = 2
    while(n!=c):
        if IsLeftTruncatablePrime(i):
            c = c+1
        i = i+1
    return i-1

print(nthLeftTruncatablePrime(int(input())))