matrix1 = (input()).split('=')
matrix2 = (input()).split('=')

matrix1 = eval(matrix1[1].strip())
matrix2 = eval(matrix2[1].strip())

def check_identical(matrix1, matrix2):
    if matrix1 == matrix2:
        return True
    else:
        return False
    
print(check_identical(matrix1, matrix2))

