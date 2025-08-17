# s = "Programming"
# print(s[6])

# s = "Python"
# print(s[-1])

# s = "Language"
# print(s[0:4])

# s = "PythonProgramming"
# print(s[6:9])

# s = "PythonProgrammingLanguage"
# print(s[6:17])

# s = "abcdefghijklm"
# print(s[2::2],s)

# s = "abcdefabcdefabcdef"
# print(s[::3])

# s = "PythonProgramming"
# print(s[-12::-1])

# s = "HelloWorld"
# print(s[:4]+s[6:])

# s = "PythonLanguage"
# print(s[6:])


# s = "Palindrome"
# print(s[::-1])

# s = "abcdefgh"
# print(s[-1::-2])

# s = "abcdefghi"
# print(s[3:6], s[-6:-3])


# s = "Complete"
# print(s[0:8:1])


# s = "Programming"
# print(s[-8:-3])

# s = "123456789"
# print(s[-1::-2])


# s = "University"
# s1 = s[0:4]
# print(s1[::-1])

# s = "PythonLanguage"
# print(s[2::2])

# s = "DataScience"
# print(s[-6::-1])


# s = "ArtificialIntelligence"
# print(s[-22:-4])


#--------------------------------------------------------------------


# 1. Reverse a String:
# ○ Write a function reverse_string(s) that takes a string s and returns the
# string reversed.
# 2. Check for Palindrome:
# ○ Write a function is_palindrome(s) that checks if the given string s is a
# palindrome (reads the same forwards and backwards).
# Example:
# Input: "racecar"
# Output: True


# def Reverse_a_string(s):
#     r= ""
#     for char in s:
#         r = char + r
#     return r == s  #Check for Palindrome
# print(Reverse_a_string(input()))


#-----------------------------------------------------------------------



# 3. Count Vowels:
# ○ Write a function count_vowels(s) that counts the number of vowels (a, e,
# i, o, u) in a given string s.
# Example:
# Input: "Programming"
# Output: 3



# def count_vowels(s):
#     count = 0
#     for char in s:
#         if char in "aeiou0":
#             count += 1
#     return count
# print(count_vowels(input()))


#-----------------------------------------------------------------------


# 4. Remove Duplicates:
# ○ Write a function remove_duplicates(s) that removes all duplicate characters
# from a given string s.
# Example:
# Input: "mississippi"
# Output: "misp”



# def Remove_duplicates(s):
#     r = ""
#     for char in s:
#         if char not in r:
#             r = r + char
#     return r

# print(Remove_duplicates(input()))


#-----------------------------------------------------------------------------


# 5. Find the Longest Word:
# ○ Write a function longest_word(s) that takes a sentence s and returns the
# longest word in the sentence.
# Example:
# Input: "I love programming in Python"
# Output: "programming”


# def Longest_word(s):
#     s = s.split(" ")
#     l = ""
#     for word in s:
#         if len(word) > len(l):
#             l = word 
#     return l
# print(Longest_word(input()))


#---------------------------------------------------------------------------



# 6. Count Substring Occurrences:
# ○ Write a function count_substring(s, sub) that takes a string s and a
# substring sub and counts how many times sub appears in s.
# Example:
# Input: "banana", "ana"
# Output: 1



# def count_substring(s, sub):
#     count = 0
#     sub_len = len(sub)
#     for i in range(len(s) - sub_len + 1):
#         if s[i:i + sub_len] == sub:
#             count+=1
#     return count
# print(count_substring(input(), input()))


#-------------------------------------------------------------------------------

# 7. Capitalize Every Word:
# ○ Write a function capitalize_words(s) that takes a sentence s and
# capitalizes the first letter of each word.
# Example:
# Input: "hello world"
# Output: "Hello World"



# def Captitalize_word(s):
#     s = s.split(" ")
#     str = ""
#     for i in s:
#         str += i[0].upper() + i[1:] + " "
#     return str.strip()
# print(Captitalize_word(input()))


#----------------------------------------------------------------


# 8. Find the First Non-Repeating Character:
# ○ Write a function first_non_repeating(s) that returns the first non-repeating
# character in a string s. If all characters are repeated, return None.
# Example:
# Input: "swiss"
# Output: "w”


# def first_nonRepeating(s):
#     for char in s:
#         if s.count(char)==1:
#             return char
#     return None
# print(first_nonRepeating(input()))



#------------------------------------------------------------------------------



# 9. Count Words in a Sentence:
# ○ Write a function count_words(s) that takes a sentence s and counts the
# number of words in it. A word is defined as a sequence of characters separated
# by spaces.
# Example:
# Input: "The quick brown fox"
# Output: 4



# def count_words(s):
#     s = s.split(" ")
#     count = 0
#     for char in s:
#         if char in s:
#             count += 1
#     return count
# print(count_words(input()))




#--------------------------------------------------------------
# n=input()

# def fun(n):
#     s=""
#     for i in n:
#         if i not in s:
#             s=s+i
#     return s
# print(fun(n))
        

# n = int(input())
# sum = 0
# for i in range(0,n+1,2):
#     sum += i
# print(sum)



# def fun(s):
#     if s.isnumeric():
#         return True
#     return False
# print(fun(input()))


# def fun(s, c):
#     o = ""
#     for i in s:
#         if i != c:
#             o = o+i
#     return o
# print(fun(input(), input()))



# def fun(s):
#     w = s.split()
#     res=""
#     for i in w:
#         x = i.capitalize()
#         res+=x
#         res+=" "
#     return res.strip()
# print(fun(input()))


