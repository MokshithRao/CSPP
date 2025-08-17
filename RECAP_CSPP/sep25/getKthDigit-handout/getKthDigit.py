
def getKthDigit(digit, k):
    digit = abs(digit)
    digit = digit//(10**k)
    return digit%10
	
print(getKthDigit(int(input()), int(input())))