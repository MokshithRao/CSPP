def saddle_point(matrix):
    sp = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            element = matrix[i][j]
            if element == min(matrix[i]) and element == max(row[j] for row in  matrix):
                sp.append((i, j))
    return sp
print(saddle_point(eval(input())))