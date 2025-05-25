# Problem 1: Determine the Larger Number 
# Description: 
# Write a program that takes two numbers as input and prints the larger of the two. If the numbers are equal, print that they are equal. 


def larger_num():
    a=int(input())
    b=int(input())
    if a>b:
        return a 
    elif b>a:
        return b
    else:
        return "They are equal"
print(larger_num())
 