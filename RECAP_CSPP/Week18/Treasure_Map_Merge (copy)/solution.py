def Treasure_map_merge(d1,d2):
    for k,v in d2.items():
        if k in d1:
            d1[k] += v
        else:
            d1[k] = v
    return d1


d1 = eval(input())
d2 = eval(input())
print(Treasure_map_merge(d1, d2))