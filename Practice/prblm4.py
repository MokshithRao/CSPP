# Problem 4: Determine Triangle Type 
# Description: 
# Write a program that takes three sides of a triangle as input and determines whether the triangle is equilateral, isosceles, or scalene. 


def triangle():
    a=int(input())
    b=int(input())
    c=int(input())
    if a==b==c:
        return "equilateral triangle"
    elif a==b or a==c or b==a or b==c or c==a or c==b:
        return "isosceles triangle"
    elif a!=b!=c:
        return "scalene triangle"

print(triangle())
    