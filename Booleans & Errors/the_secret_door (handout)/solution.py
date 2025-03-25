def fun():
    x=str(input())=="True"
    y=str(input())=="True"
    z=str(input())=="True"
    return (x and y and z) or (x and z) or (y and (x or z))
print(fun())