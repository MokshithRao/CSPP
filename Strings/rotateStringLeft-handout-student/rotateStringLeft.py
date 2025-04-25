def rotateStringLeft(s, n):
    length = len(s)
    n = n % length
    return s[n:] + s[:n]
    

print(rotateStringLeft(input(),int(input())))