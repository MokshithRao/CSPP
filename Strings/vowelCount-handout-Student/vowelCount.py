
def vowelCount(s):
	count=0
	for character in s:
		if character=="a" or character=="e" or character=="i" or character=="o" or character=="u" or character=="A" or character=="E" or character=="I" or character=="O" or character=="U":
			count += 1
	return count
	

print(vowelCount(input()))