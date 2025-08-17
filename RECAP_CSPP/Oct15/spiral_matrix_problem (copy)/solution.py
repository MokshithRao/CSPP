def create_spiral_matrix(list1, n):
    matrix = [[0] * n for _ in range(n)]

    top = 0
    bottom = n - 1
    left = 0
    right = n - 1
    index = 0

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = list1[index]
            index += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = list1[index]
            index += 1
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = list1[index]
                index += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = list1[index]
                index += 1
            left += 1

    return matrix


list1 = eval(input())
n = int(input())
print(create_spiral_matrix(list1, n))