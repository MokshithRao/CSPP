# 1. Space-Separated Single Line Input

# s = input().split()
# l = []
# for i in s:
#     l.append(int(i))
# print(l)

# ----------------------------------------------------------

# 2. Space-Separated Multiple Lines Input


# lst = []

# while True:
#     l = []
#     input_str = input()

#     if not input_str:
#         break

#     input_str = input_str.split()
#     for i in input_str:
#         l.append(int(i))
#     lst.append(l)
# print(lst)


#-----------------------------------------------------------------


# # 3. Comma-Separated Values

# s = input().split(",")
# # print(s)
# l = []
# for i in s:
#     l.append(int(i))
# print(l)

# ------------------------------------------------------------

# 4. Newline-Separated Multiple Values

# l = []
# while True:
#     x = int(input())
#     if not x:
#         break

#     l.append(x)
# print(l)



#-----------------------------------------------------------------------


# 5. Single Integer for Array Size Followed by Array Elements

# n = int(input())
# l = []
# for i in range(n):
#     y = int(input())
#     l.append(y)

# print(l)


# -------------------------------------------------------------------------


# 6. Matrix Input

# x,y = input().split()
# x = int(x)
# y = int(y)

# l = []
# for i in range(x):
#     l.append(list(map(int, input().split())))

# print(l)


# ----------------------------------------------------------------------

# 7. Test Cases Input

# l = []

# n = int(input())

# for i in range(n):
#     l.append(list(map(int, input().split())))
# print(l)

#---------------------------------------------------------------------

# 8. Single Line Input with Specific Character Delimiters

# s = input().split('/')
# print(list(map(int,s)))


# --------------------------------------------------------------------------


# 9. String Input with Spaces and Other Delimiters

# x = input().replace(',', ' ')
# print(x)


#---------------------------------------------------------------------------

# 10. Variable Number of Inputs (Dynamic Input)

# n = int(input())
# l = []
# for i in range(n):
#     l.append(list(map(int, input().split())))

# print(l)


# --------------------------------------------------------------------------

# 11. Input with Specific Range Constraints

# l = list(map(int, input().split()))
# print(l)

# ----------------------------------------------------------------------------


# 12. Multiple Test Case Input with Predefined Format


# n = int(input())

# for i in range(n):
#     l = list(map(int, input().split()))

#     x = input()
#     if x == 'Sum':
#         s = sum(l)
#         print(s)
#     elif x == 'Product':
#         p = 1
#         for i in l:
#             p *= i
#         print(p)


#-------------------------------------------------------------------------------

# 13. Nested Lists as Input

# l = eval(input())
# print(l)

# ------------------------------------------------------------------

# 14. Edge Cases with Large Inputs

# n = int(input())
# l = []
# while True:
#     s = input()

#     if not s:
#         break

#     s = list(map(int, s.split()))
#     l.extend(s)
# print(l)



# --------------------------------------------------------------------


# 15. Combination of Multiple Types of Inputs

# n = int(input())

# for i in range(n):
#     d,k = input().split()
#     l = []
#     for j in range(int(d)):
#         l.append(int(input()))
#     print(l)


# -------------------------------------------------------------------

# 16. Mixed Delimiters in a Single Line

# s = input().replace(';', ' ')
# s = s.replace(',', ' ')
# s = s.replace('/', ' ')
# s = s.replace(':', ' ')

# s = list(map(int, s.split()))
# print(s)


# ----------------------------------------------------------------

# 17. Nested Input with Multiple Levels

# l = input()
# l = l.replace('[', '').replace(']', '')
# l = list(map(int, l.split(',')))
# print(l)


# ----------------------------------------------------------------


# 18. Key-Value Pairs (Dictionary-Like Input)

# d = {}

# while True:
#     s = input()

#     if not s:
#         break

#     k,v = s.split(':')
#     d[k.strip()] = v.strip()
# print(d)


# -------------------------------------------------------------


# 19. Bracketed Expressions in a Single Line

