def is_upper_triangle(matrix):
    # l = len(matrix)
    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] != 0:
                return False
    return True
print(is_upper_triangle(eval(input().strip().replace("matrix = ",""))))