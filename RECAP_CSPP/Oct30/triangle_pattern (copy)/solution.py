def triangle_pattern(n):
    for i in range(1, n+1):
        for j in range(i):
            if (i+j) % 2 == 0:
                print(0, end=" ")
            else:
                print(1, end=" ")
        print()

triangle_pattern(int(input()))