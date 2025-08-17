# def sum_of_elements(lst):
#     lst = lst.split()
#     # print(lst)
#     l = []
#     for i in lst:
#         a = int(i)
#         l.append(a)
#     # print(l,type(l))

#     min_ind = min(l)
#     max_ind = max(l)
#     # print(min_ind, type(min_ind), max_ind, type(max_ind))

#     # for i in lst:
#     a = l.index(min_ind)
#     b = l.index(max_ind)
#     # print(a,b)
#     sum = 0
#     for i in range(a,b+1):
#         sum += int(lst[i])
#         # print(sum)
#     return sum


# print(sum_of_elements((input())))





# def Sum_of_Elements(l):
#     maxp = max(l)
#     minp = min(l)
#     # print(maxp, minp)
#     max_i = l.index(maxp)
#     min_i = l.index(minp)
#     # print(max_i, min_i)

#     s = 0
#     for i in range(min_i, max_i+1):
#         # print(l[i], type(l[i]))
#         s += l[i]
#     return s

# l = list(map(int, input().split()))
# print(Sum_of_Elements(l))