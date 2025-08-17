# Write your solution here
a = float(input())
b = float(input())
c = float(input())
def Roots_Quadratic_equ(a,b,c):
    x = (-b + ((b**2) - 4*(a*c))**0.5)/(2*a)
    y = (-b - ((b**2) - 4*(a*c))**0.5)/(2*a)
    z = (x , y)
    return z

print(Roots_Quadratic_equ(a,b,c))