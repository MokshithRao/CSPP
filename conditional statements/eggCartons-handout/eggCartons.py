
def eggCartons(eggs):
	if eggs == 0:
		return 0
	elif eggs <= 12:
		return 1
	else:
		if eggs % 12 == 0:
			return eggs // 12
		else:
			return eggs // 12 + 1
		
print(eggCartons(int(input())))



    