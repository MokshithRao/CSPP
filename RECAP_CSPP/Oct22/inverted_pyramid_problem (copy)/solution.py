def Inverted_half_pyramid(n):
    l = []
    for i in range(n, 0, -1):
        a = '*' * i
        l.append(a)
    return l
print(Inverted_half_pyramid(int(input())))