def is_prime(n):
	if n<=1:
		return False
	for i in range(2,n):
		if n%i==0:
			return False
	return True


def nth_Carol_prime(n):
	c = -1
	k = 2
	while c!=n:
		a = (2**k - 1)**2 -2
		if is_prime(a):
			c+=1
		k+=1
	return a
print(nth_Carol_prime(int(input())))


