
def fabricYards(inches):
	if inches == 0:
		return 0
	elif inches%36 == 0:
		return inches//36
	elif inches%36 != 0:
		return inches//36 + 1
	else:
		return 0

print(fabricYards(int(input())))