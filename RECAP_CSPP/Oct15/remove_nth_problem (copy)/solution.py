def remove_nth(l,n):
    r = []
    for i in range(len(l)):
        if (i + 1) % n != 0:
            r.append(l[i])
    return r
print(remove_nth(eval(input()), int(input())))