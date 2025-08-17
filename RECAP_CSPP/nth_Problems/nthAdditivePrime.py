def isprime(n):
	if n<=1:
		return False
	if n==2:
		return True
	for i in range(2,n):
		if n%i==0:
			return False
	return True	
def sum(a):
	s=0
	while a>0:
		r=a%10
		a=a//10
		s=s+r
	return s

def isAdditivePrime(x):
	if isprime(x):
		if isprime(sum(x)):
			return True
	return False

# ans=[]
# for i in range(300):
#     if isAdditivePrime(i):
#         ans.append(i)

# print(ans)
# [2, 3, 5, 7, 11, 23, 29, 41, 43, 47, 61, 67, 83, 89, 101, 113, 131, 137, 139, 151, 157, 173, 179, 191, 193, 197, 199, 223, 227, 229, 241, 263, 269, 281, 283]

def nthAdditivePrime(b):
	i=1
	c=0
	result=0
	while c<b+1:
		if isAdditivePrime(i):
			result=i
			c+=1
		i+=1
	return result		
print(nthAdditivePrime(int(input())))