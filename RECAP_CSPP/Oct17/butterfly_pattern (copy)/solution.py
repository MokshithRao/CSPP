n=int(input())
def star(n):
    s = (n-2)
    s1 = n-1
    for i in range(1,n):
        print("*"*i+" "*s+" "*s1+"*"*i)
        s-=1
        s1-=1
    print("*"*(2*n-1))
    s2 = 1
    s3 = 0
    for i in range(n-1,0,-1):
        print("*"*i+" "*s2+" "*s3+"*"*i)
        s2+=1
        s3+=1
star(n)