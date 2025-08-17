n = abs((int(input())))
def isprime(n):
    if n<=1:
    	return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True    

def sumofdigits(n):
    sum = 0
    while(n>0):
        r= n%10
        n= n//10
        sum = sum+r
    return sum

def isTenlyPrime(n):
    if (isprime(n) and sumofdigits(n) == 10):
        return True 
    return False

def nthnumber(n):
    i = 19 
    c = -1
    while(c<n):
        if isTenlyPrime(i) :
            c = c+1
        i = i+1
    return i-1
            
print(nthnumber(n))




	
