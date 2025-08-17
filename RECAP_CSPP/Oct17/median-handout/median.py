def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(float(input()))
	return a

def median(a):
	if len(a) == 0:
		return None
	
	s_a = sorted(a)
	n = len(s_a)
	if n%2 == 0:
		m = (s_a[n//2-1] + s_a[n//2]) / 2
	else:
		m = s_a[n//2]
	return m


print(median(readArray()))





