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

def vectorSum(a,b):
    # your code goes here
    if len(a)> len(b):
        c = 0
        for i in range(len(b)):
        	c += a[i]*b[i]
    elif len(b) > len(a):
        c = 0 
        for i in range(len(a)):
        	c += a[i]*b[i]
    elif len(a) == len(b):
        c = 0 
        for i in range(len(a)):
        	c += a[i]*b[i]
        
    return c
		
	
print(vectorSum(readArray(),readArray()))


