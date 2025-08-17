def sameChars(s1, s2):
	for i in s2:
		if i not in s1:
			return False
	return True



print(sameChars(input(), input()))
