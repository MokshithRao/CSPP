
def hasConsecutiveDigits(x):
	x = abs(x)
	while x > 9:
		if x%10 - (x//10)%10 == 1:
			return True
		x = x//10
	return False
		
print(hasConsecutiveDigits(int(input())))
