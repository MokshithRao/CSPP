def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(float(input()))
	return a

def isPalindromicList(a):
	
	return a[::1]==a[::-1]



print(isPalindromicList(readArray()))
