def readList():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a


def recursionOnlyAlternatingSum(l,i,sum):
	if i==len(l):
		return sum
	else:
		if i%2==0:
			sum+=l[i]
		else:
			sum-=l[i]
	return recursionOnlyAlternatingSum(l,i+1,sum)	

print(recursionOnlyAlternatingSum(readList(),0,0))


