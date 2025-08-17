
def digit_frequdncy_2d(s):
    d = {}

    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    l = []
    for key,value in d.items():
        a = [int(key),value]
        l.append(a)
    lst = sorted(l)
    return lst

print(digit_frequdncy_2d(input()))



