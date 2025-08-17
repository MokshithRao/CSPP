# def Balanced_word(s):
#     s = s.split()
#     l = []

#     special = '~!@#$%^&*()_+|><'

    # nc = 0
    # lc = 0

    # for i in s:
    #     for j in i:
    #         if j in special:
    #             continue
    #         elif j.isalpha():
    #             lc += 1
    #         else:
    #             nc += 1
        
    #     if nc == lc:
    #         l.append(i)

#     z = ""
#     lst = []

#     for i in l:
#         # print(i)
#         for j in i:
#             if j in special:
#                 continue
#             else:
#                 z += j
        
#         lst.append(z)
#     z = ""


#     return lst

# print(Balanced_word(input()))




# a = ['1234abcd!!']
# special = '~!@#$%^&*()_+|><'
# z = ""
# lst = []
# for i in a:
#     # print(i)
#     for j in i:
#         # print(j)
#         if j in special:
#             continue
#         else:
#             z += j
#             # print(z)
# lst.append(z)    
# z = ""
# print(lst)





def remove_dup(s):
    s=s.split()
    l = []
    special = '~!@#$%^&*()_+|><'
    r = ""
    for i in s:
        for j in i:
            if j in special:
                continue
            else:
                r += j
        l.append(r)
        r = ""
    
    l1 = []

    nc = 0
    lc = 0
    if s == []:
        return ['']
    for i in l:
        for j in i:
            if j.isalpha():
                lc += 1
            else:
                nc += 1
        
        if nc == lc:
            l1.append(i)
        lc = 0
        nc = 0
    return l1
print(remove_dup(input()))

