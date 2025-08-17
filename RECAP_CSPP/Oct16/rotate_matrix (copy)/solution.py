def rotate_matrix_withangle(matrix, angle):
    n = len(matrix)

    if angle == 0:
        return matrix
    elif angle == 90:
        return [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]
    elif angle == 180:
        return [[matrix[n - i - 1][n - j - 1] for j in range(n)] for i in range(n)]
    elif angle == 270:
        return [[matrix[j][n - i - 1] for j in range(n)] for i in range(n)]
    else:
        return matrix


rows = int(input().strip())
m = [list(map(int, input().strip().split())) for _ in range(rows)]
a = int(input().strip())

rotated_matrix = rotate_matrix_withangle(m, a)
for row in rotated_matrix:
    print(" ".join(map(str, row)))