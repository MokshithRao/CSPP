# 15. Fibonacci Series up to N
# ○ Description: Generate the Fibonacci series up to N numbers.
# ○ Explanation: Use a loop to calculate each Fibonacci number based on the
# previous two.
# ○ Sample Test Cases:
# ■ Input: 5
# Output: [0, 1, 1, 2, 3]




# def generate_fibonacci(n):
#     l = []

#     if n <= 0:
#         return l
#     elif n == 1:
#         l.append(0)
#     else:
#         l.append(0)
#         l.append(1)
    
#         for i in range(2, n):
#             next_number = l[i-1] + l[i-2]
#             l.append(next_number)
    
#     return l

# # Test the function with an example
# input_n = 5
# print(generate_fibonacci(input_n))




#------------------------------------------------------------------------

# 16. Capitalize First Letter of Each Word
# ○ Description: Given a string, capitalize the first letter of each word.
# ○ Explanation: Use the title() function or split and capitalize each word.
# ○ Sample Test Cases:
# ■ Input: "hello world"
# Output: "Hello World"
# ■ Input: "python programming"
# Output: "Python Programming"



# s = "hello words"
# s=s.split()
# # print(s)

# def fun(s):
#     l = []
#     for i in s:
#         if i[0].islower():
#             s = i[0].upper() + i[1:] + " "
#             l.append(s)
#     return ''.join(l).strip()

# print(fun(s))


#-------------------------------------------------------------------------------------

# 18. Find Substring Occurrences
# ○ Description: Count occurrences of a substring in a string.
# ○ Explanation: Use count() to count the substring in the string.
# ○ Sample Test Cases:
# ■ Input: "hello hello", "lo"
# Output: 2
# ■ Input: "mississippi", "iss"
# Output: 2


# s1 = "aaaaa"
# s2 = 'aa'

# def sub(s1, s2):
#     count = 0
#     i = 0

#     while i<len(s1):
#         s = s1[i:i+len(s2)]
#         if s == s2:
#             count += 1
#         #     i += len(s2)
#         # else:
#         i += 1
#     return count
# print(sub(s1, s2))


#-----------------------------------------------------------------------------------


# 20. Find Shortest Word in Sentence
# ○ Description: Find the shortest word in a given sentence.
# ○ Explanation: Split the sentence and find the minimum length word.
# ○ Sample Test Cases:
# ■ Input: "I love Python programming"
# Output: "I"
# ■ Input: "This is a test"
# Output: "a"


# s = "This is a test"
# s = s.split()
# min = s[0]
# for i in s:
#     if len(i) < len(min):
#         min = i
# print(min)


#----------------------------------------------------------------------------------

# 27. Merge Two Dictionaries
# ○ Description: Merge two dictionaries. If a key exists in both, sum the values.
# ○ Explanation: Use update() and a loop to add values for duplicate keys.
# ○ Sample Test Cases:
# ■ Input: {'a': 1, 'b': 2}, {'b': 3, 'c': 4}
# Output: {'a': 1, 'b': 5, 'c': 4}
# ■ Input: {'x': 10}, {'x': 20, 'y': 30}
# Output: {'x': 30, 'y': 30}

# # d1 = {'a': 1, 'b': 2}
# # d2 = {'b': 3, 'c': 4}

# d1 = {'x': 10}
# d2 = {'x': 20, 'y': 30}

# for key, value in d2.is():
#     if key in d1:
#         d1[key] += value
#     else:
#         d1[key] = value
# print(d1)

#--------------------------------------------------------------------------------------------


# 31. Find Prime Numbers up to N
# ○ Description: Write a function to print all prime numbers up to a given number N.
# ○ Explanation: Use nested loops to check if a number is only divisible by 1 and
# itself.
# ○ Sample Test Cases:
# ■ Input: 10
# Output: [2, 3, 5, 7]
# ■ Input: 20
# Output: [2, 3, 5, 7, 11, 13, 17, 19]


# n = 10
# l = []
# for i in range(2,n+1):
#     is_prime = True
#     for j in range(2, i):
#         if i%j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         l.append(i)
# print(l)


#-----------------------------------------------------------------------------


# 41. Concatenate Two Lists Alternately
# ○ Description: Merge two lists alternately, picking elements from each list.
# ○ Explanation: Use a loop to alternate between elements of the two lists.
# ○ Sample Test Cases:
# ■ Input: [1, 2, 3], [a, b, c]
# Output: [1, 'a', 2, 'b', 3, 'c']
# ■ Input: [5, 6], [7, 8, 9]
# Output: [5, 7, 6, 8, 9]

# l1 = [5, 6]
# l2 = [7, 8, 9]

# length = min(len(l1), len(l2))
# l = []

# for i in range(length):
#     l.append(l1[i])
#     l.append(l2[i])

# l.extend(l1[length:])
# l.extend(l2[length:])

# print(l)





#----------------------------------------------------------------------------

# 42. Flatten Nested List
# ○ Description: Convert a nested list into a flat list.
# ○ Explanation: Use recursion or nested loops to flatten.
# ○ Sample Test Cases:
# ■ Input: [[1, 2], [3, 4], [5]]
# Output: [1, 2, 3, 4, 5]
# ■ Input: [1, [2, [3]]]
# Output: [1, 2, 3]


# def flatten(l):
#     l1 = [] 
#     for i in l:
#         if isinstance(i, list):
#             l1.extend(flatten(i))  
#         else:
#             l1.append(i)  
#     return l1

# # Test cases
# print(flatten([[1, 2], [3, 4], [5]]))  # Output: [1, 2, 3, 4, 5]
# print(flatten([1, [2, [3]]]))          # Output: [1, 2, 3]



#-------------------------------------------------------------------------------------

# Find Missing Number in List
# ○ Description: Given a list of consecutive numbers with one missing, find the
# missing number.
# ○ Explanation: Use the sum formula to calculate the expected total and find the
# missing number.
# ○ Sample Test Cases:
# ■ Input: [1, 2, 4, 5]
# Output: 3
# ■ Input: [10, 11, 12, 14]
# Output: 13
# 44. Find Intersection of Two Lists


# def find_missing_number(lst):

#     n = len(lst) + 1  
#     expected_sum = (min(lst) + max(lst)) * n // 2
    
#     actual_sum = sum(lst)

#     return expected_sum - actual_sum

# # Test cases
# print(find_missing_number([1, 2, 4, 5]))  # Output: 3
# print(find_missing_number([10, 12, 13, 14]))  # Output: 11


#------------------------------------------------------------------------------


# 82. Find Missing Elements in Consecutive List
# ○ Description: Given a list of consecutive numbers with some missing, return the
# missing numbers.
# ○ Explanation: Use a range and set difference to find missing elements.
# ○ Sample Test Cases:
# ■ Input: [1, 2, 4, 5]
# Output: [3]
# ■ Input: [10, 12, 13]
# Output: [11]


# l = [10, 12, 13]
# min_len = min(l)
# max_len = max(l)

# l1 = []

# for i in range(min_len, max_len+1):
#     if i not in l:
#         l1.append(i)

# print(l1)


#------------------------------------------------------------------------------------------


# 84. Sort List of Tuples by Second Element
# ○ Description: Sort a list of tuples based on the second element of each tuple.
# ○ Explanation: Use sorted() with a lambda function.
# ○ Sample Test Cases:
# ■ Input: [(1, 3), (2, 1), (3, 2)]
# Output: [(2, 1), (3, 2), (1, 3)]
# ■ Input: [(4, 5), (2, 6), (1, 4)]
# Output: [(1, 4), (4, 5), (2, 6)]


# def sort_by_second_element(lst):
#     return sorted(lst, key=lambda x: x[1])

# print(sort_by_second_element([(1, 3), (2, 1), (3, 2)]))  
# print(sort_by_second_element([(4, 5), (2, 6), (1, 4)]))  



# def sort_by_second_element(lst):
#     n = len(lst)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if lst[j][1] > lst[j+1][1]:  
#                 lst[j], lst[j+1] = lst[j+1], lst[j]  
#     return lst


# print(sort_by_second_element([(1, 3), (2, 1), (3, 2)]))  
# print(sort_by_second_element([(4, 5), (2, 6), (1, 4)]))  

#----------------------------------------------------------------------------------


# 86. Convert Two Lists into Dictionary
# ○ Description: Given two lists, one of keys and one of values, combine them into a
# dictionary.
# ○ Explanation: Use zip() to create key-value pairs.
# ○ Sample Test Cases:
# ■ Input: ['a', 'b', 'c'], [1, 2, 3]
# Output: {'a': 1, 'b': 2, 'c': 3}
# ■ Input: ['x', 'y'], [10, 20]
# Output: {'x': 10, 'y': 20}


# l1 = ['a', 'b']
# l2 = [1, 2, 3]
# d = {}

# length = min(len(l1), len(l2))

# for i in range(length):
#     d[l1[i]] = l2[i]

# if len(l1) > len(l2):
#     for i in range(len(l2), len(l1)):
#         d[l1[i]] = None

# elif len(l2) > len(l1):
#     for i in range(len(l1), len(l2)):
#         d[None] = l2[i]
# print(d)


#-----------------------------------------------------------------------------


# 95. Find GCD of Two Numbers
# ○ Description: Find the Greatest Common Divisor (GCD) of two numbers.
# ○ Explanation: Use the Euclidean algorithm.
# ○ Sample Test Cases:
# ■ Input: 24, 36
# Output: 12
# ■ Input: 20, 15
# Output: 5


# def find_gcd(a, b):
#     while b != 0:  
#         a, b = b, a % b  
#     return a  


# print(find_gcd(24, 36))  
# print(find_gcd(20, 15))  


#--------------------------------------------------------------------------------


