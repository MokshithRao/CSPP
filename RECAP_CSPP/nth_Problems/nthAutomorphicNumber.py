def Automorphic(num):
    a = num * num
    n = 0
    t = num
    
    while t > 0:
        t //= 10
        n += 1
    
    return a % (10 ** n) == num


def nthAutomorphicNumber(n):
    c = 0
    i = 0
    while c < n:
        if Automorphic(i):
            c += 1
        i += 1
    return i - 1

print(nthAutomorphicNumber(int(input())))
