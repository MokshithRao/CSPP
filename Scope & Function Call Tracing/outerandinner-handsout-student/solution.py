def outer():
    x=int(input())
    y=x/2
    return inner(y)
def inner(x):
    y=x+1
    return y
print(outer())
