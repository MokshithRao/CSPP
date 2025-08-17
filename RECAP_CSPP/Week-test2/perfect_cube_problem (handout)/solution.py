# import math

# def is_perfect_cube(n):
#     # if n<0:
#     #     return False
#     # a = int(n**0.4)
#     # a=abs(a)
#     a = math.ceil(n**(1/3))
#     a = abs(a)
#     if n==0:
#         return True
#     if a**3 == n:
#         return True
#     # elif n<0:
#     #     return True
#     else:
#         return False

# print(is_perfect_cube(abs(int(input()))))





def perfect_cube(n):
    for i in range(1, n+1):
        cube = i ** 3

        if cube == n:
            return True
        elif cube > n:
            return False
    return False
print(perfect_cube(int(input())))


