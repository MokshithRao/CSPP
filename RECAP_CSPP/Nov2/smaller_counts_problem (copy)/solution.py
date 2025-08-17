# def smaller_number(l):
#     lst = []

#     for i in range(len(l)):
#         c = 0
#         li = []
#         for j in range(i+1, len(l)):
#             if l[i] > l[j]:
#                 c += 1
#                 li.append(c)
#         lst.append(len(li))
#     return lst

# print(smaller_number(eval(input())))


list = eval(input())
def small_counts(list):

    li = [0] * len(list)

    for i in range(len(list)):
        c = 0
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                c += 1
        li[i] = c
    return li



print(small_counts(list))