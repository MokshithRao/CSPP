def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a
	b = []
	l = int(input())
	for i in range(l):
		b.append(int(input()))
	return b
def isRotation(a,b):
    # your code goes here
    r =[]
    for i in range(len(a)):
        s1 = a[i:]+a[:i]
        r.append(s1)
    if b not in r:
        return False
    else:
        return True

print(isRotation(readArray(),readArray()))