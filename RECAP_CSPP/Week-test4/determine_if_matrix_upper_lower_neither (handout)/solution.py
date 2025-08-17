# def determine_matrix(matrix):
#     if len(matrix)==1:
#         return "Upper"
#     elif len(matrix)==0:
#         return "Neither"
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i+1][j]==0 or matrix[i][j]==0:
#                 return "Upper"
#             elif matrix[i][j+1]==0:
#                 return "Lower"
#             # elif matrix[i+1][j]==0 and matrix[i][j]==0:
#             #     return "Neither"
#             # elif matrix[i][j] < 0:
#             #     return "Neither"
#             else:
#                 return "Neither"
            
# print(determine_matrix(eval(input())))


def Determine_matrix(m):

    upper = True
    lower = True

    for i in range(len(m)):
        for j in range(len(m)):
            if i>j:
                if m[i][j] != 0:
                    upper = False
            if j>i:
                if m[i][j] != 0:
                    lower = False


    if upper:
        return "Upper"
    if lower:
        return "Lower"
    return "Neither"
    
print(Determine_matrix(eval(input())))
                
