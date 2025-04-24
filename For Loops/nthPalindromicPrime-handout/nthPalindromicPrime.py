def is_palindrome(n):
    temp=n
    r=0
    while n>0:
        num=n%10
        r=r * 10 + num
        n //=10
    return temp == r


def is_prime(n):
    if n<1:
        return False
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True


def nthPalindromicPrime(n):
    count = 0
    i = 2
    while True:
        if is_prime(i) and is_palindrome(i):
            if count == n:
                return i
            count = count+1
        i = i+1
print(nthPalindromicPrime(int(input())))
