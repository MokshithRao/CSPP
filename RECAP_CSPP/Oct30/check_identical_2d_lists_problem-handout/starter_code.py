matrix1 = (input()).split("=")
matrix2 = (input()).split("=")


matrix1 = eval(matrix1[1].strip())
matrix2 = eval(matrix2[1].strip())

# def check_identical(matrix1, matrix2):
#     if matrix1 == matrix2:
#         return True
#     return False

# print(check_identical(matrix1, matrix2))


def check_identical(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        return False
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            if matrix1[i][j] != matrix2[i][j]:
                return False
            
    return True

print(check_identical(matrix1, matrix2))