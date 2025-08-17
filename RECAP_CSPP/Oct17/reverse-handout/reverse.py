def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def reverse(a):
	return a[::-1]



print(reverse(readArray()))



# def readArray():
# 	a = []
# 	l = int(input())
# 	for i in range(l):
# 		a.append(int(input()))
# 	return a

# def reverse(a):
# 	r = a[::-1]
# 	return r


# print(reverse(readArray()))


