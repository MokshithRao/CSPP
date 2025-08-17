
# -----------------------------------------------------------------Transpose--------------------------------------------------------------------
def Matrix_Transpose(n):
    matrix = [[0 for i in range(len(n))] for i in range(len(n[0]))]
    # for i in range(len(n[0])):
    #     lt = []
    #     for j in range(len(n)):
    #         lt.append(0)
    #     matrix.append(lt)
        
    print(matrix)
    for i in range(len(n)):
        for j in  range(len(n[0])):
            matrix[j][i] = n[i][j]
    for row in matrix:
        print(row)
m  = [[1,2],[4,5],[7,8]]
# Matrix_Transpose(m)




