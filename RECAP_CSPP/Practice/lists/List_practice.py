# lst = [num for num in range(1,11)]
# print(lst)
# print(lst[2], lst[4], lst[6])


#---------------------------------------------------------------------------



# l = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(l[1:5])

#------------------------------------------------------------------------------


# l = ['red', 'green', 'blue', 'white', 'black']
# index = l.index('blue')   #useful for only first occurence
# print(index)

# l[index] = 'yellow'
# print(l)

# # l[2] = 'yellow'
# # print(l)

# l.append('purple')
# print(l)

# del l[3]
# print(l)


#----------------------------------------------------------------------------------


# l = [1,2,3]
# m = [4,5,6]

# p = l+m
# print(p)

# l.extend(m)
# print(l)


# lst = [7,8]
# print(lst * 3)

#-------------------------------------------------------------------------------


# a = [1,2,3]
# b = a
# b[0] = 100
# print(a)
# print(b)


#-------------------------------------------------------------------------------


# x = [1,2,3,4]
# y = x[:]
# print(y)
# y[2] = 99
# print(y)
# result = x == y
# print(result)


#---------------------------------------------------------------------------------



# Problem 1: Reverse a lst


# l = [1, 2, 3, 111, 444, 555]
# print(l[::-1])

# a = []
# for i in range(len(l)-1, -1, -1):
#     a.append(l[i])

# print(a)


#---------------------------------------------------------------------


# Problem 2: Sum of lst elements


# l = [1, 2, 3, 111, 444, 555]
# sum = 0
# for i in l:
#     sum += i
# print(sum)


#-------------------------------------------------------------------------


# Problem 3: Remove Duplicates


# l = [1, 2, 3, 1, 5, 6, 1]
# print(lst(set(l)))

# lst = []
# for i in l:
#     if i not in lst:
#         lst.append(i)
# print(lst)


#----------------------------------------------------------------------------


# l = [1, 2, 3, 7, 4, 5, 6]
# k = 4
# for i in range(1):
#     l = l[k:] + l[:k]

# print(l)

#-----------------------------------------------------------------------------------------

# def rotate_list(l, k):
#     if not l:
#         return l
    
#     k = k % len(l)
#     return l[-k:] + l[:-k]


# print(rotate_list([1,2,3,4,5], 1))



#--------------------------------------------------------------------------------



# 2D Lists

# Problem1 : Find Maximuum in Each Row


# def max_in_rows(matrix):
#     lst = []
#     for row in matrix:
#         a = max(row)
#         lst.append(a)
#     return lst

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# print(max_in_rows(matrix))


# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# lst = []
# max = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] > max:
#             max = matrix[i][j]
#     lst.append(max)
# print(lst)





#--------------------------------------------------------------------


# Problem2: Count Zeros in 2D List


# def count_zeros(matrix):
#     count = 0
#     for row in matrix:
#         for element in row:
#             if element == 0:
#                 count += 1
#     return count
    
# matrix = [[1,0,3], [4,5,0], [0,0,0]]
# print(count_zeros(matrix))


        #    or



# def count_zeros(m):
#     sum_zeros = 0
#     for row in m:
#         sum_zeros += row.count(0)
#     return sum_zeros

# m = [[1,0,3], [4,5,0], [0,0,0]]
# print(count_zeros(m))


#---------------------------------------------------------------------------



# Problem3: Row wise sum


# def row_wise_sum(matrix):
#     lst = []
#     for row in matrix:
#         sum = 0
#         for element in row:
#             sum += element
#         lst.append(sum)
#         # lst.append(sum(row))  
#     return lst

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# print(row_wise_sum(matrix))



#------------------------------------------------------------------------------


# Problem4: Reverse rows

# def reverse_rows(matrix):
#     lst = []
#     for row in matrix:
#         lst.append(row[::-1])

#     return lst

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# print(reverse_rows(matrix))



#----------------------------------------------------------------------------------


# Problem5: Addition of Matrix

# def matrix_additiion(matrix1, matrix2):
#     lst = []
#     for i in range(len(matrix1)):
#         l = []
#         for j in range(len(matrix1[0])):
#             a = matrix1[i][j] + matrix2[i][j]
#             l.append(a)
#         lst.append(l)
#     return lst


# matrix1 = [[1,2,3], [4,5,6]]
# matrix2 = [[7,8,9], [1,2,3]]
# print(matrix_additiion(matrix1, matrix2))
            



#---------------------------------------------------------------------------------------


# Probelm6: Extract Column


# def extract_column(matrix, n):
#     lst = []
#     for row in matrix:
#         lst.append(row[n])
#     return lst

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# print(extract_column(matrix, 2))





#---------------------------------------------------------------------------------



# Problem7: Replace all negative numbers


# def replace_negative_num(matrix):
#     lst = []
#     for row in matrix:
#         l = []
#         for element in row:
#             if element < 0:
#                 element = 0
#             l.append(element)
#         lst.append(l)
#     return lst

# matrix = [[1,-2,3], [-4,5,6], [7,8,9]]
# print(replace_negative_num(matrix))


#-----------------------------------------------------------------------



# Probelm8: Check Identical Elements



# def identical_elements(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if i!=j and matrix[i][j] != 0:
#                 return False
#     return True
    
# # matrix = [[1,0,0], [0,1,0], [0,0,1]]
# # matrix = [[1,0], [0,1]]
# matrix = [[1,0,4], [1,1,4]]
# print(identical_elements(matrix))




#--------------------------------------------------------------------------------




# def sum_of_rows_and_columns(matrix):
#     lst = []
#     l = []
    
#     for rows in matrix:
#         lst.append(sum(rows))
#     for i in range(len(matrix)):
#         s = 0
#         for j in range(len(matrix[i])):
#             s += matrix[j][i]
#         l.append(s)
#     return lst, l

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# print(sum_of_rows_and_columns(matrix))

#               (OR)


# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# r_list = []
# c_list = []
# for i in range(len(matrix)):
#     r_sum = 0
#     c_sum = 0 
#     for j in range(len(matrix[i])):
#         r_sum += matrix[i][j]
#         c_sum += matrix[j][i]
#     r_list.append(r_sum)
#     c_list.append(c_sum)

# print(f"{r_list}\n{c_list}")






#-------------------------------------------------------------------------------------



# def Transpose_a_matrix(matrix):
#     lst= []
#     for i in range(len(matrix)):
#         l = []
#         for j in range(len(matrix[i])):
#             l.append(matrix[j][i])
#         lst.append(l)
#     return lst
# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# print(Transpose_a_matrix(matrix))




#----------------------------------------------------------------------------------------



# def max_element_in_row(matrix):
#     lst = []
#     max = 0
#     for row in matrix:
#         for element in row:
#             if element > max:
#                 max = element
#         lst.append(max)
#     return lst
# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# print(max_element_in_row(matrix))


#-----------------------------------------------------------------------------------



# def rotate_list(lst, k):
#     l = []
#     # for i in range(len(lst)):
#     a = lst[-k:] + lst[:-k]
#     l.append(a)
#     return l
# lst = [1,2,3,4,5]
# print(rotate_list(lst,2))



#------------------------------------------------------------------------


# def merge_sorted_list(l1, l2):
#     l = l1 + l2
#     return sorted(l)
# l1 = [1,2,4]
# l2 = [2,3,5]
# print(merge_sorted_list(l1, l2))



#--------------------------------------------------------------------------------



#check is a matrix is symmetric.


# def transpose(matrix):
#     lst = []
#     for i in range(len(matrix)):
#         l = []
#         for j in range(len(matrix[0])):
#             l.append(matrix[j][i])
#         lst.append(l)
#     return lst
# matrix = [[1,2,3], [2,4,5], [3,5,6]]
# print(transpose(matrix))


# def is_symmetric(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if matrix[i][j] != matrix[j][i]:
#                 return False
#     return True

# matrix = [[1,2,3], [2,4,5], [3,5,6]]
# print(is_symmetric(matrix))



#----------------------------------------------------------------------------------------------------


# def search_a_value(matrix, target):
#     lst = []
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == target:
#                 a = i,j
#                 lst.append(a)
#     return lst
# #     return None
            
# matrix = [[1,2,3], [4,1,6], [7,8,1]]
# print(search_a_value(matrix, 1))



#--------------------------------------------------------------------------------------------



# def sum_of_upper_triangle(matrix):
#     sum = 0
#     for i in range(len(matrix)):
#         for j in range(i,len(matrix)):
#              sum += matrix[i][j]
#     return sum
# matrix = [[1,2,3], [4,5,6], [7,8,9]]    
# print(sum_of_upper_triangle(matrix)) 




#-----------------------------------------------------------------------------------------



# def shift_matrixElement_byOne(matrix,n):
#     lst = []
#     x = []
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             lst.append(matrix[i][j])
#     a = lst[-1:] + lst[:-1]
#     for k in range(0,len(a),n):
#         x.append(a[k:k+n])
#     return x


# matrix = [[1,2,3], [4,5,6], [7,8,9]] 
# print(shift_matrixElement_byOne(matrix, 3))
        





#----------------------------------------------------------------------------------------------


# Find all local maximum in the matrix


# def is_local_max(matrix, i, j):
#     val = matrix[i][j]
#     neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
#     for x, y in neighbors:
#         if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] >= val:
#             return False
#     return True


# def find_local_maximum(matrix):
#     local_max = []
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if is_local_max(matrix, i, j):
#                 local_max.append(matrix[i][j])
#     return local_max

# matrix = [[1,2,1], [3,4,3], [1,2,1]]
# print(find_local_maximum(matrix)) 




#------------------------------------------------------------------------------------------------



#Replace the diagonal with row sums


# def replace_row_sum(matrix):
#     for i in range(len(matrix)):
#         row_sum = sum(matrix[i])
#         matrix[i][i] = row_sum
#     return matrix
        
        
# matrix = [[1,2,3], [4,5,6], [7,8,9]] 
# print(replace_row_sum(matrix))




#---------------------------------------------------------------------------------------------------


# 16. Find Second Most Frequent Character in a String
# Question: Write a program that finds the second most frequent character in a string. Ignore spaces and punctuation.

# Example Input: "success is the key to success"
# Example Output: 'c' (since 'c' appears the second most after 's')



# s = "success is the key to success"
# def fun(s):
#     d = {}
#     for i in s:
#         if i == " ":
#             continue
#         elif i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1

#     a = (sorted(d.items(), key=lambda item: item[1], reverse=True))
#     print(a, type(a))
#     if len(a) > 1:
#         # Return the second most frequent character
#         return a[1][0]
#     else:
#         return None
        

# print(fun(s))



# --------------------------------------------------------------------------------------------



# 25. Sort a List by String Length
# Question: Write a program that sorts a list of strings by the length of each string, in ascending order.

# Example Input: ["banana", "apple", "kiwi", "strawberry"]
# Example Output: ["kiwi", "apple", "banana", "strawberry"]



# l=eval(input())


# def fun():
#     for i in range(len(l)-1):
#         for j in range(i+1):
#             if len(l[j])>len(l[j+1]):
#                 l[j],l[j+1]=l[j+1],l[j]
#     return l
        
    
# print(fun())






