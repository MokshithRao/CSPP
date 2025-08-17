# Number Patterns Programs In Python
# I have created various programs that print different styles of number patterns. Let’s see them one by one. Let’s print the following number pattern using a for loop.

# 1  
# 2 2  
# 3 3 3  
# 4 4 4 4  
# 5 5 5 5 5

# n = 6
# def pattern(n):
#     for i in range(1,n):
#         for j in range(i):
#             print(i, end=' ')
#         print('')
        
# pattern(n)


#------------------------------------------------------------------------



# Pyramid pattern of numbers


# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# Note: In each row, every next number is incremented by 1.

# Program:


# def pattern(n):
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             print(j, end=" ")
#         print(' ')

# pattern(int(input()))



#----------------------------------------------------------------------------


# Inverted pyramid pattern of numbers
# An inverted pyramid is a downward pattern where numbers get reduced in each iteration, and on the last row, it shows only one number. Use reverse for loop to print this pattern.

# Pattern

# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5

# def pattern(n):
#     a = 0
#     for i in range(n, 0, -1):
#         a += 1
#         for j in range(1, i+1):
#             print(a, end=" ")
#         print(' ')
# pattern(int(input()))


#-----------------------------------------------------------------

# Inverted Pyramid pattern with the same digit

# Pattern: –

# 5 5 5 5 5 
# 5 5 5 5 
# 5 5 5 
# 5 5 
# 5



# def pattern(n):
#     for i in range(n, 0, -1):
#         for j in range(0, i):
#             print(n, end=" ")
#         print(' ')
# pattern(int(input()))


#--------------------------------------------------------------------------



# Another inverted half-pyramid pattern with a number
# Pattern: –

# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1



# def pattern(n):
#     for i in range(n, 0, -1):
#         for j in range(0, i+1):
#             print(j, end=' ')
#         print(' ')

# pattern(int(input()))




#---------------------------------------------------------------------------

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# def fun(n):
#     for i in range(1,n):
#         for j in range(i):
#             print("*", end=" ")
#         print()

#     for i in range(n, 0, -1):
#         for j in range(1,i+1):
#             print("*", end=" ")
#         print()

# fun(int(input()))


#------------------------------------------------------------------------------



#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * *


# def pattern(n):
#     for i in range(1,n):
#         for j in range(n-i):
#             print(" ", end="")
#         for j in range(i):
#             print("*", end=" ")
#         print()
# pattern(int(input()))


#---------------------------------------------------------------------------------



