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

def hasDuplicates(L):
	b =[]
	for i in L:
		for j in i:
			if j in b:
				return True
			b.append(j)
	return False



print(hasDuplicates(read2DArray()))


