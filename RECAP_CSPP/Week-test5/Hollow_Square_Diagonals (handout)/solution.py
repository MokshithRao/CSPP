def hollow_square_with_diagonal(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or j == n-i-1:
                print("*", end="")
            else:
                print(" ", end="")

        print()

hollow_square_with_diagonal(int(input()))

# for i in range(1, n+1):
#     if i == 1 or i == n:
#         print("*" * n)
#     else:
#         print("*" + " " * (n-2) + "*")