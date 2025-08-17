# def count_occurrences(s1, n):
#     count = 0
#     i = 0
#     while i<len(s1):
#         if s1[i:i+len(n)] == n:
#             count += 1
#         i+=1

#     return count
    
# print(count_occurrences(input(), input()))



# Input: main_string = "abababa", substring = "aba"
# Output: 3 (the substring "aba" appears 3 times in overlapping positions)





#-------------------------------------------------------------------------------------------------------------



# def extract_substring(s1, n):
#     l = []
#     i = 0
#     while i<len(s1):
#         if s1[i:i+len(n)] == n:
#             l.append(i)
#         i+=1
#     return l
# print(extract_substring(input(), input()))


# Input: main_string = "abababa", substring = "aba"
# Output: [0, 2, 4] (the substring "aba" is found starting at indices 0, 2, and 4)



#---------------------------------------------------------------------------------------------------------------



# def remove_all_Occurrences(s1, n):
#     s = ""
#     i = 0
#     while i<len(s1):
#         if s1[i:i+len(n)] == n:
#             i += len(n)
#         else:
#             s = s + s1[i]
#             i += 1
#     return s

# print(remove_all_Occurrences(input(), input()))



# Input: main_string = "abababa", substring = "aba"
# Output: "b" (all instances of "aba" are removed, leaving "b")



#----------------------------------------------------------------------------------------------



# def replace_vowels(s):
#     s1 = ""
#     for i in s:
#         if i in "aeiouAEIOU":
#             i = "*"
#         s1 = s1 + i
#     return s1
# print(replace_vowels(input()))


# Input: main_string = "hello world", replacement_char = "*"
# Output: "h*ll* w*rld"



#----------------------------------------------------------------------------------------------


# def reverse_occurrences_substring(s1, n):
#     s = ""
#     i = 0
#     while i<len(s1):
#         if s1[i:i+len(n)] == n:
#             s = s + n[::-1]
#             i += len(n)
#         else:
#             s = s + s1[i]
#             i += 1

#     return s
# print(reverse_occurrences_substring(input(), input()))


# Input: main_string = "abababa", substring = "aba"
# Output: "ababbba" (the substring "aba" is reversed each time, resulting in "ababbba")



#-----------------------------------------------------------------------------------------------------------------



# def count_distinct_substring(s):
#     s1 = []
#     for i in range(len(s)):
#         for j in range(i+1, len(s)+1):
#             a = s[i:j]
#             # if a not in s1:
#             s1.append(a)
#     return len(s1)
    
# print(count_distinct_substring(input()))


# Input: main_string = "abc"
# Output: 6 (distinct substrings are: "a", "b", "c", "ab", "bc", "abc")




#-----------------------------------------------------------------------------------------------




# def longest_substring(s):
#     s1 = ""
#     d = {}
#     for i in range(len(s)):
#         for j in range(i+1, len(s)+1):
#             a = s[i:j]
#             if a in d:
#                 d[a] += 1
#             else:
#                 d[a] = 1

#     for key, value in d.items():
#         if value > 1 and len(key) > len(s1):
#             s1 = key
#     return s1

# print(longest_substring(input()))


# Input: main_string = "banana"
# Output: "ana" (the longest repeated substring is "ana")



#-------------------------------------------------------------------------------------------------


# def capitalize_words(s):
#     s = s.split(" ")
#     s1 = ""
#     for i in s:
#         s1 = s1 + i[0].upper() + i[1:] + ' '

#     return s1.strip()


# print(capitalize_words(input()))


# Input: main_string = "hello world"
# Output: "Hello World"



#------------------------------------------------------------------------------------



# def extract_substring(s1, n):
#     l = []
#     i = 0
#     for i in range(len(s1) - n+1):
#         a = s1[i:i+n]
#         l.append(a)
#     #     i+=1
#     # for i in l:
#     #     if len(i) < n:
#     #         l.remove(i)
#     return l
# print(extract_substring(input(), int(input())))



# Input: main_string = "abcdef", length = 3
# Output: ["abc", "bcd", "cde", "def"]


#----------------------------------------------------------------------------------------------


# def generate_all_permutations(s1,s2):
#     import itertools
#     lt = []
#     # for i in s2:
#     for j in itertools.permutations(s2):
#         converting_tuple_to_string = "".join(j)
#         lt.append(converting_tuple_to_string)
#     print(lt)


 
# generate_all_permutations("abcabc","abc")


