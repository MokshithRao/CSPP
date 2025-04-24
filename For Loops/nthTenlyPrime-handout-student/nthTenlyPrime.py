def isprime(n):
	if n<=1:
		return False
	if n==2:
		return True
	for i in range(2,n):
		if n%i==0:
			return False
	return True

def Tenlysum(n):
	count = 0
	while(n>0):
		r = n%10
		count=count+r
		n=n//10
	if count==10:
		return True
	else:
		return False


def nthTenlyPrime(n):
	count = -1
	num=0
	while(count<n):
		if isprime(num) and Tenlysum(num):
			count+=1
		num+=1
	return num-1

print(nthTenlyPrime(int(input())))





	

