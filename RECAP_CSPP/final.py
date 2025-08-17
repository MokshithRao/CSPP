# l = [60, 20, 56, 82, 30, 100, 69]

# first = 0
# second = 0

# for i in l:
#     if i > first:
#         second = first
#         first = i
#     elif i > second:
#         second = i
# print(second)


#------------------------------------------------------------

# 1  
# 2 3  
# 4 5 6  
# 7 8 9 10  
# 11 12 13 14 15  

# n = 5
# m =1
# for i in range(1,n+1):
#     for j in range(i):
#         print(m, end=" ")
#         m += 1
#     print()

#-------------------------------------------------------------

#    *  
#   ***  
#  *****  
# *******  

# n = 4
# for i in range(1,n+1):
#     print(" " * (n - i), end="")
#     print("*" * (2*i-1))

# n = 4
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for k in range(2*i-1):
#         print("*", end="")
#     print()

#-----------------------------------------------------------

#     *  
#    ***  
#   *****  
#  *******  
# *********  
#  *******  
#   *****  
#    ***  
#     *  

# n = 5
# for i in range(1,n+1):
#     print(" " * (n - i), end="")
#     print("*" * (2*i-1))

# for i in range(n-1, 0, -1):
#     print(" " * (n - i), end="")
#     print("*" * (2*i-1))
    
#----------------------------------------------------------------

# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********

# n = 5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ", end="")
#     for k in range(2*i-1):
#         print("*", end="")
#     print()
    
# for i in range(2,n+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for k in range(2*i-1):
#         print("*", end="")
#     print()


