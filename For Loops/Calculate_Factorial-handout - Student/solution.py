# n=int(input())
# # p=1
# # i=1
def factorial(n):
    p=1
    i=1
    for i in range(1,n+1):
        p=p*i
    return p    
print(factorial(int(input())))

