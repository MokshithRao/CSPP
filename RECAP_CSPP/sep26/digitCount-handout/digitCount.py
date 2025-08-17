
def digitCount(x):
	count = 0
	x=abs(x)
	if x==0:
		return 1
	while x > 0:
		x //= 10
		count += 1
	return count

print(digitCount(int(input())))


