# # # def determine_matrix(m):
# # #     diagonal = True
# # #     scalar = False

# # #     for i in range(m):
# # #         for j in range(m):



# # def diagonal_matrix(m):
# #     for i in range(len(m)):
# #         for j in range(len(m[i])):
# #             if m[i] != m[j] and m[i][j] != 0:
# #                 return False
# #     return True
            
# # # print(diagonal_matrix(eval(input())))



# def check_matrix_type(matrix):
#     n = len(matrix)
#     if n == 0:
#         return "Neither"
    
#     diagonal_value = None
#     is_diagonal = True

#     for i in range(n):
#         for j in range(n):
#             if i != j:  # Off-diagonal element
#                 if matrix[i][j] != 0:
#                     is_diagonal = False
#             else:  # Diagonal element
#                 if diagonal_value is None:
#                     diagonal_value = matrix[i][j]
#                 elif matrix[i][j] != diagonal_value:
#                     return "Diagonal"  # It's diagonal but not scalar
    
#     if is_diagonal:
#         return "Scalar"
#     else:
#         return "Neither"

# print(check_matrix_type(eval(input())))




def Diagonal_Matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i!=j:
                if matrix[i][j]!=0:
                    return False
    return True

def Scalar_Matrix(matrix):
    m = matrix[0][0]
    if not Diagonal_Matrix(matrix):
        return False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i==j:
                if matrix[i][j]!= m:
                    return False
    return True 
def Check_Matrix(matrix):
    if Scalar_Matrix(matrix):
        return "Scalar"
    elif Diagonal_Matrix(matrix):
        return "Diagonal"
    else:
        return "Neither"
print(Check_Matrix(eval(input())))