def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def reverse(a):
	# your code goes here
	return a[::-1]



print(reverse(readArray()))


