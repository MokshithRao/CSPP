def smart():
    a=str(input())=="True"
    b=str(input())=="True"
    c=str(input())=="True"
    d=str(input())=="True"
    return (a and not(d)) or (b and not(d)) or (c and not(d))
print(smart())