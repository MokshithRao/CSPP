def average(l):
    s = 0
    for i in l:
        s += i
    return abs(s//len(l))
# print(average(eval(input())))
    
def product(a):
    return a[0]*a[0]
# print(product(eval(input())))



def nearest_product(l,a):
    l1 = []

    for i in range(len(l)):
        for j in range(1,len(l)-1):
            l1.append((l[i], l[j]))
    print(l1)
    l2 = []
    for i in l1:
        a = product(i)
        l2.append(a)
    print(l2)
    

    for i in l2:
        if i == average(l):
            # print(i, average(l))
            a = l2.index(i)
            # print(a)
    return l1[a]



print(nearest_product(eval(input())))







# def nearest_product(l):
#     d = {}

#     for i in range(len(l)):
#         for j in range(1,len(l)-1):
#             d[(l[i], l[j])] = product(l[i], l[j])
#     print(d)
    

#     for key, values in d.items():
#         if values == average(l):
#             a = key
#             break
#         elif values == average(l)-1:
#             a = key
#     return a

# print(nearest_product(eval(input())))