# def boundary_sum(matrix):
#     sum = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if i == 0 or i == len(matrix)-1 or j == 0 or j == len(matrix)-1:
#                 sum += matrix[i][j]
#     return sum

# # matrix = [[1,2,3], [4,5,6], [7,8,9]]
# matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16]]
# print(boundary_sum(matrix))





#---------------------------------------------------------------------------------------------

# def get_target_sum(matrix):
#     return sum(matrix[0])

# def row_sum(matrix):
#     l = []
#     for row in matrix:
#         sum  = 0
#         for elements in row:
#             sum += elements
#         l.append(sum)
#     return l

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# print(row_sum(matrix))


# def column_sum(matrix):
    
#     l = []
#     for i in range(len(matrix)):
#         sum = 0
#         for j in range(len(matrix[i])):
#             sum += matrix[j][i]
#         l.append(sum)
#     return l

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# print(column_sum(matrix))
        


# def diagonal_sum(matrix):
#     sum = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if i == j:
#                 sum += matrix[i][j]
#     return sum

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# print(diagonal_sum(matrix))
        
            



# def magic_square(matrix):

#---------------------------------------------------------------------------------




# def snake_pattern(matrix):
#     l = []
#     for i in range(len(matrix)):
#         if i%2 == 0:
#             l.append(matrix[i])
#         else:
#             l.append(matrix[i][::-1])
#     return l


# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# print(snake_pattern(matrix))





#--------------------------------------------------------------------------------------------------------------------




# def mirror_matrix_horizontally(matrix):
#     for i in range(len(matrix)):
#         matrix = matrix[::-1]
#     return matrix
         

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# print(mirror_matrix_horizontally(matrix))



#------------------------------------------------------------------------------------------------------------


# def no_of_ilands(matrix):
#     count = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):



# ---------------------------------------------------------------------------------------------------------------------





# -----------------OCT30----------------------------------------



# Probelem1: Latin Square checker



# def latin_square_checker(matrix):
#     n = len(matrix)

#     #row check
#     for i in range(n):
#         row_check = [False] * n     # using it to find the duplicates
#         for j in range(n):
#             value = matrix[i][j]
#             if value < 1 or value > n or row_check[value - 1]:
#                 return False
#             row_check[value - 1] = True

#     #column check
#     for i in range(n):
#         row_check = [False] * n
#         for j in range(n):
#             value = matrix[j][i]
#             if value < 1 or value > n or row_check[value - 1]:
#                 return False
#             row_check[value - 1] = True
#     return True


# # matrix = eval(input())
# matrix = [[1,2,3], [3,1,2], [2,3,1]]
# print(latin_square_checker(matrix))


# -------------------------------------------------------------------------------------------



# problem2: Semi-Magic Square Validator


# def semi_magic_square(matrix):
#     r_list = []
#     c_list = []
#     for i in range(len(matrix)):
#         r_sum = 0
#         c_sum = 0 
#         for j in range(len(matrix[i])):
#             r_sum += matrix[i][j]
#             c_sum += matrix[j][i]
#         r_list.append(r_sum)
#         c_list.append(c_sum)
#     print(r_list, c_list)
#     if r_list == c_list:
#         return True
#     return False

# print(semi_magic_square(eval(input())))




#----------------------------------------------------------------------------------------------------


# Problem3: Orthogonal latin square checker


# def Matrix_Transpose(n):
#     matrix = [[0 for i in range(len(n))] for i in range(len(n[0]))]
#     # for i in range(len(n[0])):
#     #     lt = []
#     #     for j in range(len(n)):
#     #         lt.append(0)
#     #     matrix.append(lt)
        
#     # print(matrix)
#     for i in range(len(n)):
#         for j in  range(len(n[0])):
#             matrix[j][i] = n[i][j]
#     for row in matrix:
#         return row
# # m  = [[1,2],[4,5],[7,8]]
# # m = [[1,2,3], [3,1,2], [2,3,1]]
# # Matrix_Transpose(m)


# def transpose(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if 

# def func(matrix1, matrix2):
#     if matrix2 == Matrix_Transpose(matrix1):
#         return True
#     return False

# matrix1 = [[1,2,3], [3,1,2], [2,3,1]]
# matrix2 = [[1,3,2], [2,1,3], [3,2,1]]

# print(func(matrix1, matrix2))










