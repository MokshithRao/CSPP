
def vowelCount(s):
	count = 0
	for char in s:
		if char in "AEIOUaeiou":
			count += 1

	return count

print(vowelCount(input()))