def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def isRotation(a,b):
	# your code goes here
	for i in range(len(b)):
		r = b[i:] + b[0:i]
		if r==a:
			return True
	return False




print(isRotation(readArray(),readArray()))



