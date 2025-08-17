def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def vectorSum(a,b):
	z=[]
	for i in range(len(a)):
		z.append(a[i]+b[i])
	return z



print(vectorSum(readArray(),readArray()))


