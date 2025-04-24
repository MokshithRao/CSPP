n=int(input())
def prime():
    s=0
    for i in range (1,n+1):
        if n%i != 0:
            s=s+1
    if s == n-2:
        return True
    else:
        return False
    
print(prime())

