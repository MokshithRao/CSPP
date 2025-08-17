import math

def isRightTriangle(x1, y1, x2, y2, x3, y3):

    a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    if a > b and a > c:
        return a**2 == b**2 + c**2
    elif b > a and b > c:
        return b**2 == a**2 + c**2
    else:
        return c**2 == a**2 + b**2
    
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
    
print(isRightTriangle(x1, y1, x2, y2, x3, y3))