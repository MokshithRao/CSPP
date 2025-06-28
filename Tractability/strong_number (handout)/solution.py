def fact(n):
    p = 1
    i = 1
    while i <= n:
        p = p*i
        i+=1
    return p


def strongNum(n):
    num = n
    sum = 0
    while n>0:
        rem = n%10
        sum += fact(rem)
        n //= 10
    return sum == num

print(strongNum(int(input())))

