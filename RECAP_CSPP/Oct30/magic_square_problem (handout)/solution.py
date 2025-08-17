
def diagonal(matrix):
    d = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                d += matrix[i][j]
    return d
# print(diagonal(eval(input())))



def sum_of_row_col(matrix):
    r_list = []
    c_list = []
    for i in range(len(matrix)):
        r_sum = 0
        c_sum = 0
        for j in range(len(matrix[i])):
            r_sum += matrix[i][j]
            c_sum += matrix[j][i]
        r_list.append(r_sum)
        c_list.append(c_sum)


    for i in range(len(r_list)):
        if diagonal(matrix) != r_list[i] or diagonal(matrix) != c_list[i]:
            return False
    return True
    
print(sum_of_row_col(eval(input())))









