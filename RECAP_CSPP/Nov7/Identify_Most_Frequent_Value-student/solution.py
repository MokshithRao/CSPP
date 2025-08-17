def most_frequent_value(d):
    l = list(d.values())
    lst = []
    for i in l:
        for j in i:
            lst.append(j)

    d1 = {}
    # print(lst)
    for i in lst:
        # print(i)
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1
    

    max = 0
    freq = None
    for k,v in d1.items():
        if v > max:
            max = v
            freq = k

    return freq


print(most_frequent_value(eval(input())))