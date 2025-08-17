def wordWrap(s,n):
    z=s.split()
    print(z)
    y="-".join(z)
    print(y)
    i=0
    while (i<len(y)):
        print(y[i:i+n])
        i+=n
wordWrap(input(), int(input()))