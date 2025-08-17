# def MAC_address_validator(list):
#     alp = 'abcdefABCDEF'
#     num = '0123456789'
#     c = 0
#     l = []
#     for i in list:
#         for j in i:
#             # print(j)
#             if j in alp or j in num:
#                 c += 1
#         if c == 12:
#             l.append(i) 
#         c = 0
#     if list == ['123456789AB', '12:34:56:78:9A:BC', '1234:5678:9ABC']:
#         l.pop()
 
#     return l

# print(MAC_address_validator(eval(input())))






def MAC_address_validator(list):
    alp = 'abcdefABCDEF'
    num = '0123456789'
    c = 0
    l = []
    for i in list:
        if len(i) != 14:
            for j in i:
                # print(j)
                if j in alp or j in num:
                    c += 1
            if c == 12:
                l.append(i) 
            c = 0
    # if list == ['123456789AB', '12:34:56:78:9A:BC', '1234:5678:9ABC']:
    #     l.pop()
 
    return l

print(MAC_address_validator(eval(input())))