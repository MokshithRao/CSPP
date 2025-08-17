def is_palindrome_number(num):
    original = num
    reversed_num = 0
    
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return original == reversed_num
def isPrime(n):
    if n<=1:
        return False
    if n==2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
# print(isPrime(int(input())))

# print(is_palindrome_number(int(input())))
def nthPalindromicPrime(x):
    c = -1
    i = 2
    while c<x:
        if is_palindrome_number(i) and isPrime(i):
            c+=1
        i+=1
    return i-1


print(nthPalindromicPrime(int(input())))