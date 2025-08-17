# def digit_frequency(s):
#     l = [0] * 10
#     for i in s:
#         l[int(i)] += 1
#     return l

# print(digit_frequency(input()))





# def fun_non_zero(s):
#     l = [0] * 10
#     for i in s:
#         l[int(i)] += 1
#     # return [(i, l[i]) for i in range(10) if l[i] > 0]
#     a = []
#     for i in range(10):
#         if l[i]>0:
#             a.append([(i,l[i])])
#     return a

# # Input the number
# print(fun_non_zero(input()))



# def fun_ignore_negative(s):
#     l = [0] * 10
#     for i in s:
#         if i.isdigit():
#             l[int(i)] += 1
#     return l

# # Input the number (can include negative signs)
# print(fun_ignore_negative(input()))




# def fun_list_of_strings(numbers):
#     results = []
#     for s in numbers:
#         l = [0] * 10
#         for i in s:
#             l[int(i)] += 1
#         results.append(l)
#     return results

# # Input the list of numbers as strings
# numbers = input().split()
# print(fun_list_of_strings(numbers))



# def fun_cumulative_frequency(numbers):
#     l = [0] * 10
#     for s in numbers:
#         for i in s:
#             l[int(i)] += 1
#     return l

# # Input the list of numbers as strings
# numbers = input().split(",")
# print(fun_cumulative_frequency(numbers))



# def fun_dict(s):
#     l = {}
#     for i in range(10):
#         l[i] = 0  # Initialize the count for each digit

#     for char in s:
#         if char.isdigit():  # Check if the character is a digit
#             l[int(char)] += 1  # Increment the count for the digit

#     return l

# # Input the number
# print(fun_dict(input()))





# --------------------------------------------------------


# def count_freq_char(s):
#     d = {}
#     for char in s:
#         if char in d:
#             d[char] += 1
#         else:
#             d[char] = 1
#     return d

# print(count_freq_char(input()))


# Input: "apple"
# Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}


# ------------------------------------------------------------


# def remove_duplicates(s):
#     st = ""
#     for i in s:
#         if i not in st:
#             st = st + i
#     return st

# print(remove_duplicates(input()))


# Input: "programming"
# Output: "progamin"



# ----------------------------------------------------------------------


# def check_anagram(s1,s2):
#     if len(s1) != len(s2):
#         return False
#     if sorted(s1) == sorted(s2):
#         return True
#     else:
#         return False
    
# print(check_anagram(input(), input()))


# Input: "listen", "silent"
# Output: True

# Input: "hello", "world"
# Output: False


# -----------------------------------------------------------------------------------------


# def longest_word(s):
#     s = s.split(" ")
#     # print(s)
#     s1 = ""
#     for word in s:
#         if len(word) > len(s1):
#             s1 = word
#     return s1

# print(longest_word(input()))


# Input: "I love Python programming"
# Output: "programming"




# ---------------------------------------------------------------------------


# def most_frequent(s):
#     s = s.split(" ")
#     d = {}

#     for word in s:
#         if word  in d:
#             d[word] += 1
#         else:
#             d[word] = 1
#     max = 0
#     most = None
#     for key,value in d.items():
#         if value > max:
#             max = value
#             most = key
#     return most

# print(most_frequent(input()))


# Input: "apple banana apple apple orange banana"
# Output: "apple"


# ------------------------------------------------------------------------------



# def reverse_each_word(s):
#     s = s.split(" ")
#     print(s)
#     s1 = []
#     for i in s:
#         a = i[::-1]
#         # print(a)
#         s1.append(a)
#         s2 =""
#     for i in s1:
#         s2+=" "+i
#     return s2.strip()


#     # return s1
        
# print(reverse_each_word(input()))


# Input: "hello world"
# Output: "olleh dlrow"


#------------------------------------------------------------------------------------



# def find_all_substrings(s):
#     l= []

#     for i in range(len(s)):
#         for j in range(i+1, len(s)+1):
#             l.append(s[i:j])
#     return l

# print(find_all_substrings(input()))


# Input: "abc"
# Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']


# --------------------------------------------------------------------------------



# def sort_by_length(strings):
#     n = len(strings)
    
#     # Bubble sort algorithm
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             # Compare lengths of adjacent strings
#             if len(strings[j]) > len(strings[j + 1]):
#                 # Swap if they are in the wrong order
#                 strings[j], strings[j + 1] = strings[j + 1], strings[j]
    
#     return strings

# # Example usage
# input_list = ["apple", "dog", "banana", "a", "cat"]
# output = sort_by_length(input_list)
# print(output)  # Output: ['a', 'dog', 'cat', 'apple', 'banana']



# ----------------------------------------------------------------------------------


k = eval(input())

def anagrams(k):
    l =[]
    for i in range(len(k)):
        p = []
        for j in range(len(k)):
            if sorted(k[i])==sorted(k[j]):
                p.append(k[j])
        l.append(p)
    n =[]
    for i in l:
        if i not in n:
            n.append(i)
    return n
print(anagrams(k))