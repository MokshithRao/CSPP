
def fabricYards(inches):
	if inches == 0:
		return 0
	elif inches <= 36:
		return 1
	else:
		if inches % 36 == 0:
			return inches // 36
		else:
			return inches // 36 + 1
print(fabricYards(int(input())))
