def wordWrap(s,n):
    z=s.split()
    y="-".join(z)
    i=0
    while (i<len(y)):
        print(y[i:i+n])
        i+=n
wordWrap(input(), int(input()))