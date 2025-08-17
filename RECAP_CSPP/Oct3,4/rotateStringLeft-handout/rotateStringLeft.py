def rotateStringLeft(s, n):
    for i in range(n):
        s=s[1:]+s[0]

    return s
    

print(rotateStringLeft(input(), int(input())))


 