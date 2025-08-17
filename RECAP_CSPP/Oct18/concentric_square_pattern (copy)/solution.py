def concentric_square(n):
    a = 2 * n - 1
    for i in range(a):
        for j in range(a):
            layer = min(i, j, a - 1 - i, a - 1 - j)
            print(n - layer, end=" ")
        print()

concentric_square(int(input()))