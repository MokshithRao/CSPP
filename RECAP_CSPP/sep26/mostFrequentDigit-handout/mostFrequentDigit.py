def mostFrequentDigit(n):
	n=abs(n)
	maxcount=0
	freqdigit=n%10
	if n==0:
		return 0
	temp=n
	while temp>0:
		digit=temp%10
		count=0
		while n>0:
			if n%10==digit:
				count=count+1
			n=n//10
		n=temp
		if count>maxcount or (count==maxcount and digit<freqdigit):
				maxcount=count
				freqdigit=digit
		temp=temp//10
	return freqdigit
		

print(mostFrequentDigit(int(input())))