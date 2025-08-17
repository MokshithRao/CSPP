def readArray():
    s = input().split(" ")
    l = []
    for i in s:
        if len(i) != 0:
            l.append(int(i))
    return l

def smallestDifference(a):
    if not a:
        return -1
    a.sort()
    b = []
    diff = 0
    for i in range(len(a)-1):
        diff = abs(a[i]) - abs(a[i+1])
        b.append(abs(diff))
    return min(b)
    
print(smallestDifference(readArray()))





