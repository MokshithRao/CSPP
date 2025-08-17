def consecutive_pattern(l):
    d = {}

    for i in range(len(l)):
        for j in range(len(l[i])-1):
            # print(l[i][j])
            a = l[i][j:j+2]
            if a not in d:
                d[a] = [(i,j)]
            else:
                d[a] += [(i,j)]
            

    return d
print(consecutive_pattern(eval(input())))