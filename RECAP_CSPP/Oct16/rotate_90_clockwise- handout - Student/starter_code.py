def rotate_matrix_90(matrix):
    row_count = len(matrix)
    col_count = len(matrix[0])

    if row_count == 1 and col_count > 0:
        rotated = [[] for _ in range(col_count)]

        for index in range(col_count):
            rotated[index].append(matrix[0][index])
        return rotated

    else:
        rotated = []

        for col in range(col_count):
            new_row = []

            for row in range(row_count - 1, -1, -1):
                new_row.append(matrix[row][col])
            rotated.append(new_row)
            
        return rotated
print(rotate_matrix_90(eval(input())))