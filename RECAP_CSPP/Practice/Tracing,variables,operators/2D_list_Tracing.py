# def fun(lst):
#     new_list = []
#     for i in range(len(lst)-1, -1, -1):
#         new_list.append(lst[i])
#     return new_list

# lst = [1, 2, 3, 4]
# print(fun(lst))



# def fun(lst):
#     for i in range(len(lst)):
#         lst[i] = lst[i] ** 2
#     return lst

# lst = [2, 4, 6]
# print(fun(lst))



# def fun(lst):
#     max_val = lst[0]
#     for val in lst:
#         if val > max_val:
#             max_val = val
#     return max_val

# lst = [10, 23, 45, 1, 34]
# print(fun(lst))


# def fun(lst):
#     for i in range(1, len(lst)):
#         lst[i] += lst[i-1]
#     return lst

# lst = [1, 2, 3, 4]
# print(fun(lst))

# def fun(lst):
#     result = []
#     for x in lst:
#         if x % 2 != 0:
#             result.append(x)
#     return result

# lst = [1, 2, 3, 4, 5, 6]
# print(fun(lst))

# def fun(lst):
#     if len(lst) == 0:
#         return lst
#     result = [lst[-1]]  # Start with the last element
#     for i in range(len(lst) - 1):
#         result.append(lst[i])  # Append the rest of the elements
#     return result

# lst = [1, 2, 3, 4]
# print(fun(lst))

# def fun(lst):
#     return sum(lst[2:5])

# lst = [10, 20, 30, 40, 50, 60]
# print(fun(lst))


# def fun(lst, target):
#     for i in range(len(lst)):
#         if lst[i] == target:
#             return i
#     return -1

# lst = [5, 9, 2, 6, 3]
# print(fun(lst, 7))



# def fun(lst1, lst2):
#     return lst1 + lst2

# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# print(fun(lst1, lst2))



# def fun(lst):
#     return sorted(lst)

# lst = [34, 12, 4, 56, 17]
# print(fun(lst))



# def fun(lst):
#     total = 0
#     for row in lst:
#         for col in row:
#             total += col
#     return total

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(fun(matrix))



# def fun(matrix):
#     t = []
#     for i in range(len(matrix[0])):  # Iterate over the columns of the matrix
#         temp = []
#         for row in matrix:  # Iterate over the rows of the matrix
#             temp.append(row[i])  # Append the i-th element of each row to temp
#         t.append(temp)  # Append the transposed row to the result
#     return t



# matrix = [[1, 2, 3], [4, 5, 6]]
# print(fun(matrix))



# def fun(matrix):
#     total = 0
#     for i in range(len(matrix)):
#         total += matrix[i][i]
#     return total

# matrix = [[5, 1, 2], [3, 9, 7], [4, 8, 6]]
# print(fun(matrix))



# def fun(matrix):
#     result = []
#     for sublist in matrix:  # Iterate over each sublist in the matrix
#         for item in sublist:  # Iterate over each item in the sublist
#             result.append(item)  # Append each item to the result list
#     return result


# matrix = [[1, 2], [3, 4], [5, 6]]
# print(fun(matrix))





# def fun(matrix):
#     product = 1
#     for row in matrix:
#         for col in row:
#             product *= col
#     return product

# matrix = [[1, 2], [3, 4]]
# print(fun(matrix))




# def fun(matrix):
#     result = []
#     for row in matrix:  # Iterate over each row in the matrix
#         max_value = max(row)  # Find the maximum value in the row
#         result.append(max_value)  # Append the maximum value to the result list
#     return result


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(fun(matrix))




# def fun(matrix):
#     col_sums = [0] * len(matrix[0])
#     for row in matrix:
#         for i in range(len(row)):
#             col_sums[i] += row[i]
#     return col_sums

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(fun(matrix))




# def fun(matrix, target):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == target:
#                 return (i, j)
#     return None

# matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# print(fun(matrix, 60))




# def fun(matrix):
#     total = 0
#     for i in range(len(matrix)):
#         for j in range(i+1, len(matrix[0])):
#             total += matrix[i][j]
#     return total

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(fun(matrix))




# def fun(matrix):
#     result = []
#     for i in range(len(matrix[0]) - 1, -1, -1):  # Iterate over the columns in reverse order
#         temp = []
#         for j in range(len(matrix)):  # Iterate over the rows
#             temp.append(matrix[j][i])  # Append the element from the matrix
#         result.append(temp)  # Append the transposed and reversed row to the result
#     return result

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(fun(matrix))





