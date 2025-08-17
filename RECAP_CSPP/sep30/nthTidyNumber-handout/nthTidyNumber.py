def tidynumber(n):
    digit2 = 10  
    while n > 0:
        digit1 = n % 10  
        if digit1 > digit2:  
            return False
        digit2 = digit1  
        n //= 10  
    return True

def nthnumber(n):
    i = 1 
    c = -1
    while(c<n):
        if tidynumber(i) :
            c = c+1
        i = i+1
    return i-1
print(nthnumber(int(input())))