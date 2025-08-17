def Extract_image_sources(s):
    s = s.split('<img')
    # print(s)
    l = []
    for i in s[1:]:
        # print(i)
        a = i.split('=')
        print(a)
        # b = a.split('>')
        # print(b)
    #     if len(a) == 1:
    #         continue
    #     else:    
    #         l.append(a[1])
    # return l

# print(Extract_image_sources(input()))



def extract(s):
    s = s.split('=')
    img = ""
    s = ''.join(s)
    s = s.split('"')
    # print(s)

    for i in s:
        if i == '<img src' or i == '>' or i == '><img src' or i == ' ':
            s.remove(i)
    return s


print(extract(input()))

    # for i in 









# def remove_special_character(l):
#     s = ""
#     l = []
#     sp = '>"'
#     print(l)
#     for i in l:
#         print(i)
#         for j in i:
#             if j in sp:
#                 continue
#             else:
#                 s += j
#         l.append(s)
#     # s = ""
#     return l
# print(remove_special_character(eval(input())))
