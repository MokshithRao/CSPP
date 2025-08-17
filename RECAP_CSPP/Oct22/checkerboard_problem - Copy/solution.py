def checkboard_pattern(n,m):
    l = []
    for i in range(n):
        lst = []
        for j in range(m):
            if (i+j) % 2 == 0:
                lst.append(0)
            else:
                lst.append(1)
        l.append(lst)
    return l

print(checkboard_pattern(int(input()), int(input()))) 