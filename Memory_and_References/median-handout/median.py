def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(float(input()))
	return a

def median(a):
	a.sort()
	b=len(a)
	if b==0:
		return None
	if b%2==0:
		return (a[b//2-1]+a[b//2])/2
	else:
		return a[b//2]

print(median(readArray()))


