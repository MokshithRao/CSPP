def Prime(x):
    if x == 0 and x == 1:
        return False
    i =2
    while(x>i):
        if x%i == 0:
            return False
        i = i+1
    return True   
def Additive(x):
    s = 0
    while(x>0):
        s +=(x%10)
        x = x//10
    if Prime(s):
        return True
    return False

def AdditivePrime(x):
    if Additive(x) and Prime(x):
        return True
    return False    
def nthAdditivePrime(x):
    c = -1
    i = 2
    while(x!=c):
        if AdditivePrime(i):
            c = c+1
        i = i+1
    return i-1
print(nthAdditivePrime(int(input())))