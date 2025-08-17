# Write your solution here
def Pythagorean_Theorem(a,b):
    c = (a**2 + b**2)**0.5
    return round(c,2)
print(Pythagorean_Theorem(float(input()), float(input())))