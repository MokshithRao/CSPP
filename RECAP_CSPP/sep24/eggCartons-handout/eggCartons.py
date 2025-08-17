def eggCartons(eggs):
	if eggs%12 == 0:
		return eggs//12
	if eggs%12 != 0:
		return eggs//12 +1
	return 0

print(eggCartons(int(input())))