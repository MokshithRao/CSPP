def x_shape_pattern(n):
    for i in range(n):
        for j in range(n):
            if j == i or j == n-i-1:
                print(n-i, end=" ")
            else:
                print(" ", end=" ")
        print()


x_shape_pattern(int(input()))


