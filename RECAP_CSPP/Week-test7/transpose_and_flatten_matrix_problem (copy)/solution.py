# def Transpose_flatten(n):

#     matrix = []
#     for i in range(len(n[0])):
#         lt = []
#         for j in range(len(n)):
#             lt.append(0)
#         matrix.append(lt)
        
#     for i in range(len(n)):
#         for j in  range(len(n[0])):
#             matrix[j][i] = n[i][j]
    

#     l = []
#     for i in matrix:
#         for j in i:
#             a = str(j)
#             l.append(a)
#     return ' '.join(l)
# print(Transpose_flatten(eval(input())))


def Transpose_flatten(matrix):

    m1 = []

    for i in range(len(matrix[0])):
        m2 = []
        for j in range(len(matrix)):
            m2.append(matrix[j][i])
        m1.append(m2)
    
    l = []
    for i in m1:
        for j in i:
            a = str(j)
            l.append(a)
    return ' '.join(l)



print(Transpose_flatten(eval(input())))