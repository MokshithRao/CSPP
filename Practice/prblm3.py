# Problem 3: Find the Middle Number 
# Description: 
# Write a program that takes three numbers as input and prints the middle one. Assume the numbers are distinct and not necessarily in any particular order. 

def Middle_num():
    a=int(input())
    b=int(input())
    c=int(input())
    if a>b and a<c:
        return a
    elif b>a and b<c:
        return b
    else:
        return c
print(Middle_num())  