def patternedMessage(s, p):
	l = ""
	for i in s:
		if i==" ":
			continue
		l+=i
	res = ""
	id = 0
	for i in range(len(p)):
		if p[i] == " ":
			res+=" "
		else:
			res+=l[id]
			if(id<len(l)-1):
				id+=1
			else:
				id = 0
	return res

print(patternedMessage(input(), input()))