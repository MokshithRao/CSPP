n=int(input())
def sum():
    s=0
    for i in range(1,n):
        if ((i%3==0) or (i%5==0)):
            s=s+i
    return s
print(sum())

        
