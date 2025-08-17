# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True

# def Palindromic_prime(n):
#     temp = n
#     rev = 0
#     while temp>0:
#         a = temp%10
#         rev = rev*10 + a
#         temp//=10
#     return n == rev and is_prime(n)
       
# # print(Palindromic_prime(int(input()))) 




# def nthPalindromicPrime(x):
#     count = 0
#     i = 2
#     while count<=x:
#         if Palindromic_prime(i):
#             count += 1
#         i+=1
#     return i-1
        

# print(nthPalindromicPrime(int(input())))



def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True


def Palindromic_prime(n):
    if is_prime(n):
        temp = n
        rev = 0
        while temp>0:
            a = temp%10
            rev = rev*10 + a
            temp//=10
        return rev == n
    
# print(Palindromic_prime(int(input())))


def nth_Palindromic_prime(n):
    c = 0
    i = 2
    while c<=n:
        if Palindromic_prime(i):
            c+=1
        i+=1
    return i-1
print(nth_Palindromic_prime(int(input())))
