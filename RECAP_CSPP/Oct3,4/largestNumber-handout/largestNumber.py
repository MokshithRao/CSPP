def largestNumber(s):
	x = ''
	max_num = None  # Change from max = 0 to max_num = None
	for i in range(len(s)):
		if s[i].isdigit():
			x += s[i]
		
		# Handle all non-digit characters, not just spaces
		elif not s[i].isdigit() and x != '':  
			if max_num is None or int(x) > max_num:
				max_num = int(x)
			x = ''

		# Handle the last number at the end of the string
		if (i == len(s)-1) and x != '':
			if max_num is None or int(x) > max_num:
				max_num = int(x)

	# No need to check for '0', just return max_num
	return max_num 

print(largestNumber(input()))