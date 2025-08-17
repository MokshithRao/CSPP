
def fabricExcess(inches):
	if inches == 0 or inches%36 == 0:
		return 0
	else:
		return 36-(inches%36)
		

print(fabricExcess(int(input())))