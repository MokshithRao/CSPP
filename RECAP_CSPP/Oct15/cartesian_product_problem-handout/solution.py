def cartesian_product(l1, l2):
    d = {}

    for ele in l1:
        d[ele] = l2
    return d


l1 = eval(input())
l2 = eval(input())

print(cartesian_product(l1, l2))