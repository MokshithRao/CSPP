def Most_popular_number(l):
    d = {}

    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    # print(d)

    a = max(list(d.values()))
    lst = []
    # m = 0
    # key = None
    for k,v in d.items():
        if v == a:
            # m = v
            # key = k
            lst.append(k)

    return lst
print(Most_popular_number(eval(input())))