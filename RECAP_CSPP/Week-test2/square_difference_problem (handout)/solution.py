def fun(n):
    sum = 0
    sum1 = 0
    while n>0:
        sum += (n**2)
        sum1 += n
        n-=1
    return (sum1**2)-sum



print(fun(int(input())))

