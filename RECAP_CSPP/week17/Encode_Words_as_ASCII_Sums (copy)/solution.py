def ascii_sum(l):
    d = {}
    s = 0

    for i in l:
        for j in i:
            s += ord(j)
        d[i] = s
        s = 0
    return d
print(ascii_sum(eval(input())))


