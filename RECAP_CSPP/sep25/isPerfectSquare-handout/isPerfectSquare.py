
def isPerfectSquare(n):
    if n < 0:
        return False
    elif n == 0 or n == 1:
        return True
    else:
        x = n ** 0.5
        return x == int(x)

print(isPerfectSquare(int(input())))
