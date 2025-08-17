def rotateStringRight(s, n):
	for i in range(n):
		s=s[-1]+s[0:len(s)-1]
	return s
	
print(rotateStringRight(input(), int(input())))