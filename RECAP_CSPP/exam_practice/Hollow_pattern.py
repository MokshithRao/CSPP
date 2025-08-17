# Model 1: Standard Hollow Square Pattern (Original Question)


# Example Input and Output:

# Input: n = 5
# Output:

# *****
# *   *
# *   *
# *   *
# *****


# def hollow(n):
#     for i in range(n):
#         for j in range(n):
#             if i == 0 or i==n-1 or j==0 or j==n-1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()

# hollow(int(input()))



#------------------------------------------------------------------------------------------


# Model 2: Hollow Square with Custom Border Characters

# Example Input and Output:

# Input: n = 5, border_char = '#', inner_char = '.'
# Output:

# #####
# #...#
# #...#
# #...#
# #####


# def hollow(n):
#     for i in range(n):
#         for j in range(n):
#             if i==0 or i==n-1 or j==0 or j==n-1:
#                 print("*", end="")
#             else:
#                 print("-", end="")

#         print()

# hollow(int(input()))


#--------------------------------------------------------------------------



# Model 3: Solid Square with Hollow Cross in the Middle


# Example Input and Output:

# Input: n = 5
# Output:

# *****
# ** **
# *   *
# ** **
# *****





#---------------------------------------------------------------------------



# Model 4: Hollow Square with Diagonal Lines
    
# Example Input and Output:

# Input: n = 5
# Output:

# *****
# ** **
# * * *
# ** **
# *****



# def hollow_pattern_with_diagonals(n):
#     for i in range(n):
#         for j in range(n):
#             if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or j == n-i-1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()

# hollow_pattern_with_diagonals(int(input()))



#----------------------------------------------------------------------------


# Model 5: Hollow Square with Dynamic Padding
    

# Example Input and Output:

# Input: n = 7, padding = 2
# Output:

# *******
# *******
# **   **
# **   **
# **   **
# *******
# *******




# ----------------------------------------------------------------------------------------------------------

def hollow(n):
    space = 2*n-1
    gap = 0
    for i in range(n,1,-1):
        for j in range(0,i):
            print("*",end="")
        for j in range(gap):
            print(" ",end="")
        for j in range(0,i):
            print("*",end="")
        
        gap+=2
        print()
    for i in range(n):
        for j in range(0,i+1):
            print("*",end="")
        for j in range(space-1):
            print(" ",end="")
        for j in range(0,i+1):
            print("*",end="")
        
        space-=2
        print()
       
# hollow(5)


# ---------------------------------------------------------------Hollow Diamond----------------------------------------------------------------------------


def hollowTrinagle(n):
    for i in range(1,n+1):
        for j in range(n,i-1,-1):
            print(" ",end="")
        for j in range(1,2*i):
            if j == 1 or j == 2*i-1 or i == n:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    
# hollowTrinagle(5)

# --------------------------------------------------------------------------hollow_Right_Angle_Triangle-----------------------------------------------------
def hollow_Right_Angle_Triangle(n):
    for i in range(1,n+1):
        for j in range(n,i-1,-1):
            print(" ",end="")
        for j in range(1,i):
            if j == 1 or j == i-1 or i == n:
                print("*",end="")
            else:
                print(" ",end="")
        print()


# hollow_Right_Angle_Triangle(10)

# --------------------------------------------------------------------------hollow_Right_Angle_Triangle(left)--------------------------------------------------

def hollow_Right_Angle_Triangle(n):
    for i in range(1,n+1):
        for j in range(1,i):
            if j == 1 or j == i-1 or i == n:
                print("*",end="")
            else:
                print(" ",end="")
       
            
        print()


# hollow_Right_Angle_Triangle(10)

# ---------------------------------------------------------hollowLowerTrinangle-------------------------------------------------------------------
def lowerTriangle(n):
    c = 0
    for i in range(n,-1,-1):
        for j in range(n,i-1,-1):
            print(" ",end="")
        for j in range(1,2*i):
            if j == 1 or j == 2*i-1 or i == n :
                if i == n:
                    c = c+1
                    print("*",end=" ")
                    if c == n:
                        break 
                else:
                    print("*",end="")
            else:
                print(" ",end="")
        print()
# lowerTriangle(10)


# --------------------------------------------------------hollowDiamond--------------------------------------------------------------------------


def hollowDiamond(n):
    for i in range(1,n+1):
        for j in range(n,i-1,-1):
            print(" ",end="")
        for j in range(1,2*i):
            if j == 1 or j == 2*i-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    for i in range(n,-1,-1):
        for j in range(n,i-1,-1):
            print(" ",end="")
        for j in range(1,2*i):
            if j == 1 or j == 2*i-1 :
                print("*",end="")
            else:
                print(" ",end="")
        print()

# hollowDiamond(5)