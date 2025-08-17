# def contains_sub_matrix(l, sub):
#     n = len(l)
#     m = len(l[0]) if n > 0 else 0
#     p = len(sub)
#     q = len(sub[0]) if p > 0 else 0

#     for i in range(n - p + 1):
#         for j in range(m - q + 1):
#             match = True

#             for sub_i in range(p):
#                 for sub_j in range(q):
#                     if l[i + sub_i][j + sub_j] != sub[sub_i][sub_j]:
#                         match = False
#                         break
#                 if not match:
#                     break

#             if match:
#                 return True

#     return False


# l = eval(input())

# sub = eval(input())

# print(contains_sub_matrix(l, sub))



