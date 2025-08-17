# def is_prime(n):
# 	if n<=1:
# 		return False
# 	for i in range(2,n):
# 		if n%i==0:
# 			return False
# 	return True
# # print(is_prime(int(input())))

# def tenly_prime(n):
# 	temp = n
# 	sum = 0
# 	while temp>0:
# 		a = temp%10
# 		sum += a
# 		temp//=10
# 	return sum == 10 and is_prime(n)

# # print(tenly_prime(int(input())))




# def nthTenlyPrime(n):
# 	# temp = n
# 	count = -1
# 	i = 19
# 	while count<n:
# 		if tenly_prime(i):
# 			count += 1
# 		i+=1
# 	return i-1

# print(nthTenlyPrime(int(input())))


	










def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
# print(is_prime(int(input())))


def tenly_prime(n):
    if is_prime(n):
        temp = n
        sum = 0
        while temp>0:
            a = temp%10
            sum+=a
            temp//=10
        return sum == 10
# print(tenly_prime(int(input())))
        


def nth_tenly_prime(n):
    c=-1
    i = 19
    while c<n:
        if tenly_prime(i):
            c+=1
        i+=1
    return i-1
print(nth_tenly_prime(int(input())))