# Write your solution here
P = float(input())
r = float(input())
n = int(input())
t = float(input())
def Compound_intrest(P,r,n,t):
    A = P*(1 + (r/100)/n)**(n*t)
    return round(A,2)
print(Compound_intrest(P,r,n,t))