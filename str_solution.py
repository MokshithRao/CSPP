


# Given a String and a character (String). Find the count of occurrences 
# second string in first string.

# countOccurrences(abcabcabc, a) - 3
# countOccurrences(abcabcabc, z) - 0
# countOccurrences(abcabcabc, c) - 3
# countOccurrences(abcabcabcd, d) - 1

def countOccurrences1(main_string, search):
	count = 0
	for character in main_string:
		if search == character:
			count += 1
	return count

def countOccurrences2(main_string, search):
	count = 0
	for index in range(len(main_string)):
		if search == main_string[index]:
			count += 1
	return count

def countOccurrences(main_string, search):
	count = 0
	index = 0
	while index < len(main_string):
		if search == main_string[index]:
			count += 1
		index += 1
	return count
print(countOccurrences("abcabcabc", "a"))
print(countOccurrences("abcabcabc", "z"))
print(countOccurrences("abcabcabc", "c"))
print(countOccurrences("abcabcabcd", "d"))




# Given a string, check whethere it is palindrome or not?

def is_Palindrome_String1(string):
	return string == string[::-1]

def is_Palindrome_String(string):
	temp = ""
	for index in range(len(string) - 1, -1, -1):
		temp = temp + string[index]
	return temp == string

print(is_Palindrome_String("madam"))
print(is_Palindrome_String("1001"))
print(is_Palindrome_String("Taz"))
print(is_Palindrome_String("""Tazzat"""))



# Given a string with vowels, replace each vowel with a empty space

# replaceVowels("abcd") -  bcd
# replaceVowels("aeiou") -      
# replaceVowels("bcd") -  bcd     


def replaceVowels(string):
	temp = ""
	for character in string:
		if character == "a" or character == "e" or character == "i" or character == "o" or character == "u": 
			temp = temp + " "
		else:
			temp = temp + character
	return temp

print(replaceVowels("abcd"))
print(replaceVowels("bcd"))
print(replaceVowels("aeiou"), len(replaceVowels("aeiou")))

