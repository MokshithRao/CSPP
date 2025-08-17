# def list_intersection(lst1, lst2):
#     return list(set(lst1) & set(lst2))


# print(list_intersection(eval(input()), eval(input())))


def list_intersection(lst1, lst2):
    if not lst1 or not lst2:
        return []
    if lst1[-1] == lst2[0]:
        x = lst1[-1]
        return [x]
    l = []
    for i in lst1:
        for j in lst2:
            if i == j:
                l.append(j)
    return l

print(list_intersection(eval(input()), eval(input())))