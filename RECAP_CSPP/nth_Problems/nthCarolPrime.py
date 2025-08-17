def isprime(n):
    if n<=1:
        return False
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True


def iscarolnumber(n):
    a= (((2**n )- 1)**2) - 2
    return a
 
    
def carolprime(n):
    a=iscarolnumber(n)
    return isprime(a)

def nthCarolPrime(n):
    c=-1
    i=2
    while c<n:
        if carolprime(i):
            c+=1
            
        i+=1
    return iscarolnumber(i-1)

print(nthCarolPrime(int(input())))