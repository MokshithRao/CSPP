def Tidy_num(n):
    r=n%10
    while(n!=0):
        i=r
        n = n//10
        r=n%10
        if(i<r):
            return False
    return True

def nthnumber(n):
    i = 1 
    c = -1
    while(c<n):
        if Tidy_num(i) :
            c = c+1
        i = i+1
    return i-1
print(nthnumber(int(input())))
