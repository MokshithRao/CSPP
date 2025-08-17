
def isMultiple(f, n):
	if f==0 and n==0:
		return True
	elif n==0:
		return False
	if f%n == 0:
		return True
	else:
		return False 

print(isMultiple(int(input()), int(input())))