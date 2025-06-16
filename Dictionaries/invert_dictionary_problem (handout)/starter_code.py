a=eval(input())
def swap(a):
    d={}
    for key,value in a.items():
        if value not in d:
            d[value]=[]
        d[value].append(key)
    return d
print(swap(a))
