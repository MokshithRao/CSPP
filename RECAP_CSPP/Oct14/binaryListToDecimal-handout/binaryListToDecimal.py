def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def binaryListToDecimal(a):
	dec = 0
	for i, b in enumerate(a):
		dec += b * (2 ** (len(a) - 1 - i))
	return dec
print(binaryListToDecimal(readArray()))



