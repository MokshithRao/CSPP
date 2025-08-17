def inverted_pyramid(n):
    l = []

    for i in range(1,n+1):
        a = "*" * i
        l.append(a)

    return l[::-1]

print(inverted_pyramid(int(input())))