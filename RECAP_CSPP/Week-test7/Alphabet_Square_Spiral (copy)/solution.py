# def Alphabet_Square_Spiral(n):
#     alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] * 26
#     l = []
#     c = 0
#     for i in range(n):
#         l1 = []
#         for j in range(n):
#             l1.append(alp[c])
#             c += 1
#         l.append(l1)

#     for i in range(len(l)):
#         if i%2 != 0:
#             x = l[i][::-1]
#             print(" ".join(x))
#         else:
#             print(" ".join(l[i]))


# (Alphabet_Square_Spiral(int(input())))






m = [['a', 'b', 'c', 'd'], ['h', 'g', 'f', 'e'], ['i', 'j', 'k', 'l'], ['p', 'o', 'n', 'm']]
def transpose(m):
    l = []
    for i in range(len(m)):
        l1 = []
        for j in range(len(m[i])):
            l1.append(m[j][i])
            # x=m[i][j]
            # print(x)
        l.append(l1)
    return l
# print(transpose(eval(input())))


def fun(n):
    alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] * 26
    l = []
    c = 0
    for i in range(n):
        l1 = []
        for j in range(n):
            l1.append(alp[c])
            c += 1
        l.append(l1)
    lst = []
    for i in range(len(l)):
        if i%2 != 0:
            x = l[i][::-1]
            # print(x)
            lst.append(x)
        else:
            # print(l[i])
            lst.append(l[i])

    z = transpose(lst)

    # for i in z:
    #     print(i)
    return z

print(fun(int(input())))


