def basic():
    x=input()
    # b=str(input())=="True"
    a,b = x.split()
    a = a == "True"
    b = b =="True"
    print(a and b)
    print(a or b)
    print(not(a), not(b))
    
basic()