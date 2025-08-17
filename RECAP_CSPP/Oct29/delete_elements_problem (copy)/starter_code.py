# def delete_elements(lst1, lst2):
#     for i in lst1:
#         for j in lst2:
#             if i == j:
#                 lst1.remove(i)
#     return lst1

# print(delete_elements(eval(input()), eval(input())))



def delete_elements(lst1, lst2):

    i = 0
    while i<len(lst1):
        if lst1[i] in lst2:
            lst1.remove(lst1[i])
        else:
            i+=1
    return lst1
print(delete_elements(eval(input()), eval(input())))