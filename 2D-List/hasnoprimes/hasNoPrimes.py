def read2DArray():
	a = []
	l = int(input())
	for i in range(l):
		s = input().split(" ")
		t = []
		for j in range(len(s)):
			t.append(int(s[j]))
		a.append(t)
	return a

def is_prime(n):
	if n<=1:
		return False
	for i in range(2,n):
		if n%i==0:
			return False
	return True

def hasNoPrimes(l):
	for z in l:
		for n in z:
			if is_prime(n):
				return False

	return True


print(hasNoPrimes(read2DArray()))

