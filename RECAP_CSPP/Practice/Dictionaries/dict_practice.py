# Problem 1: Basic Dictionary Creation

# def d_creation(k,v):
#     d = {}
#     for i in range(len(k)):
#         d[k[i]] = v[i]
#     return d

# return (d_creation(eval(input()), eval(input())))




# ----------------------------------------------------------------------------------------


# Problem 2: Access Dictionary Values


# def access_d_values(d, key):
#     values = d[key]
#     return values
# d = {"name": "Bob", "age": 25}
# key = "name"

# return (access_d_values(d, key))



# ---------------------------------------------------------------------------------------


# Problem 3: Update Dictionary Value

# def update_value(data, key):
#     data[key] = 31
#     return data

# data = {"name": "Alice", "age": 30}
# key = "age"

# return (update_value(data, key))


# -----------------------------------------------------------------------------------------



# Problem 4: Check Key Existence

# data = {"name": "Alice", "age": 30}
# key = "name"
# def check_key_existence(data, key):
#     if key in data:
#         return True
#     return False

# return (check_key_existence(data, key))




# -----------------------------------------------------------------------------------------------


# Problem 5: Remove a Key from Dictionary


# data = {"name": "Alice", "age": 30, "city": "New York"}
# key = "age"

# def remove_key_from_dictionary(data, key):
#     if key in data:
#         data.pop(key)
#     return data
# return (remove_key_from_dictionary(data, key))




# -------------------------------------------------------------------------------------------




# Problem 6: Count Occurrences in List using Dictionary



# def count_occurences(nums):
#     d = {}
#     for i in nums:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1

#     return d

# nums = [1, 2, 2, 3, 1, 1, 4]
# return (count_occurences(nums))



# --------------------------------------------------------------------------------------------------



# Problem 7: Sum of Dictionary Values


# data = {"a": 100, "b": 200, "c": 300}
# def sum_of_dictionary_values(data):
#     sum = 0
#     for key, values in data.items():
#         sum += data[key]
#     return sum

# return (sum_of_dictionary_values(data))




#---------------------------------------------------------------------------------------------------------------



# Problem 8: Merge Two Dictionaries


# def merge_2_dictionaries(d1, d2):
#     d = d1.copy()
#     d.update(d2)
#     return d

# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}
# return (merge_2_dictionaries(d1, d2))



# ----------------------------------------------------------------------------------------------



# Problem 9: Nested Dictionary Lookup


# data = {"info": {"name": "Alice", "age": 30}}
# key1 = "info"
# key2 = "age"
# def Nested_Dictionary_Lookup(data, key1, key2):
#     if key1 in data:
#         d = data[key1]
#         if key2 in d:
#             a = d[key2]
#     return a

# return (Nested_Dictionary_Lookup(data, key1, key2))


# -----------------------------------------------------------------------------------------



# Problem 10: Create Dictionary from Two Lists


# keys = ["a", "b", "c"]
# values = [1, 2, 3]

# def create_dic_from_2dlist(keys, values):
#     d = {}
#     for i in range(len(keys)):
#         d[keys[i]] = values[i]

#     return d
        
# return (create_dic_from_2dlist(keys, values))



# -----------------------------------------------------------------------------------------------------


# Problem 11: Reverse Dictionary


# def reverse_dictionary(data):
#     d = {}

#     for key, value in data.items():
#         d[value] = key
#     return d

# data = {"a": 1, "b": 2, "c": 3}
# return (reverse_dictionary(data))


# ----------------------------------------------------------------------------------------------



# Problem 12: Filter Dictionary by Value


# def filter_dic_value(data, n):
#     d = {}

#     for key,values in data.items():
#         if data[key] > n:
#             d[key] = values

#     return d

# data = {"apple": 5, "banana": 3, "cherry": 8}
# n = 4
# return (filter_dic_value(data, n))



#-----------------------------------------------------------------------------------------------



# Problem 13: Frequency Count of Characters


# def frequency_count(s):
#     d = {}
#     for i in s:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1

#     return d

# return (frequency_count(input()))



# -----------------------------------------------------------------------------------------------------



# Problem 14: Find Maximum Value in Dictionary


# def find_maximum_value(d):
#     max = 0
#     v = None
#     for key,values in d.items():
#         if values > max:
#             max = values
#             v = key
#     return v

# d = {"apple": 5, "banana": 3, "cherry": 8}
# return (find_maximum_value(d))



# ---------------------------------------------------------------------------------------------------


# Problem 15: Dictionary Comprehension for Squares


# n = int(input())
# def dictionary_comprehension(n):
#     d = {}

#     for i in range(1,n+1):
#         d[i] = i**2
#     return d

# return (dictionary_comprehension(n))



# ------------------------------------------------------------------------------------------------------



# Problem 16: Update Nested Dictionary Value

# d = {"info": {"name": "Alice", "age": 30}}
# k1 = "info"
# k2 = "age"
# v = 31

# def update_nested_dictionary(d, k1, k2, v):
#     if k1 in d:
#         if k2 in d[k1]:
#             d[k1][k2] = v
#     return d

# return (update_nested_dictionary(d, k1, k2, v))



# ----------------------------------------------------------------------------------------------------


# Problem 17: Dictionary from List of Tuples

# pairs = ['n'e", "Alice"), 'a'", 25)]

# def dictionary_from_tuples(pairs):
#     d = {}
#     for key, values in pairs:
#         d[key] = values

#     return d

# return (dictionary_from_tuples(pairs))



# ----------------------------------------------------------------------------------------------------------



# Problem 18: Sum of Product of Corresponding Values

# dict1 = {"a": 2, "b": 3, "c": 4}
# dict2 = {"a": 5, "b": 6, "c": 7}

# def sum_of_product_of_values(dict1, dict2):
#     sum = 0

#     for key in dict1:
#         sum += dict1[key] * dict2[key]

#     return sum 

# return (sum_of_product_of_values(dict1, dict2))


# --------------------------------------------------------------------------------------------------


# Problem 19: Count Words in a Sentence

# def count_words(s):
#     s = s.split()
#     d={}

#     for i in s:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#     return d

# s = "hello world hello"
# return (count_words(s))



# ------------------------------------------------------------------------------------------------------



# Problem 20: Identify Common Keys

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}

# def identify_common_keys(dict1, dict2):
#     l = []
#     for key in dict1:
#         if key in dict2:
#             l.append(key)
#     return l

# return (identify_common_keys(dict1, dict2))


# --------------------------------------------------------------------------------------------


# Problem 21: Unique Values in a Dictionary


# data = {"a": 1, "b": 2, "c": 1, "d": 3}

# def unique_values(data):
#     l = []
#     for key,values in data.items():
#         if values not in l:
#             l.append(data[key])
#     return l
# return (unique_values(data))


# -------------------------------------------------------------------------------------------



# Problem 22: Find Keys with Minimum Value


# data = {"a": 2, "b": 1, "c": 3, "d": 1}

# def find_keys_min_values(data):
#     l = []
#     m = min(data.values())
#     for key, value in data.items():
#         if value == m:
#             l.append(key)
#     return l
# return (find_keys_min_values(data))



# -------------------------------------------------------------------------


# Problem 23: Group Elements by Frequency

# l = [1, 2, 2, 3, 1, 1, 4]
# def group_by_freq(l):
#     d = {}
#     for i in l:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1
#     return (d)
#     d1 = {}
#     for k,v in d.items():
#         if v not in d1:
#             d1[v] = [k]
#         else:
#             d1[v].append(k)

#     return d1
# return (group_by_freq(l))


#--------------------------------------------------------------------------


# Problem 24: Flatten a Nested Dictionary

# data = {"a": 1, "b": {"c": 2, "d": 3}}

# def flatten_nested_dicitonary(data):
   
    

# ------------------------------------------------------------------------------

# Problem 25: Create Dictionary from Two Lists with Different Lengths


# keys = ["a", "b", "c"]
# values = [1, 2]

# def fun(key, values):
#     m = max(len(keys), len(values))
#     d = {}
#     for i in range(m):
#         if i < len(keys):
#             key = keys[i]
#         else:
#             key = None
        
#         if i < len(values):
#             value = values[i]
#         else:
#             value = None
        
#         d[key] = value
#     return d

# return (fun(keys, values))


# --------------------------------------------------------------------------

# Problem 26: Remove Items with Specific Value

# data = {"a": 1, "b": 2, "c": 1, "d": 3}
# n = 1

# def remove_items(data):
#     d = data.copy()
#     for k,v in data.items():
#         if v == n:
#             d.pop(k)
#     return d

# return (remove_items(data))


# ----------------------------------------------------------------------------


# Problem 27: Dictionary Intersection

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"a": 1, "b": 4, "c": 3}

# def dict_intersection(dict1, dict2):
#     d = {}
#     for k,v in dict1.items():
#         if k in dict2 and dict2[k] == v:
#             d[k] = v
#     return d

# return (dict_intersection(dict1, dict2))


# ------------------------------------------------------------------------


# Problem 28: Sort Dictionary by Value


# data = {"apple": 5, "banana": 3, "cherry": 8}

# def sort_dictionary(data):
#     d = dict(sorted(data.items(), key=lambda item:item[1], reverse=False))
#     return d
# return (sort_dictionary(data))


# ------------------------------------------------------------------------


# Problem 29: Count Letters in a List of Words

# words = ["apple", "banana"]

# def count_letters(words):
#     d = {}
#     for i in words:
#         for j in i:
#             if j not in d:
#                 d[j] = 1
#             else:
#                 d[j] += 1
#     return d

# return (count_letters(words))


# --------------------------------------------------------------------------


# Problem 30: Map List Items to Positions


# l = [1, 2, 1, 3, 2, 1]

# def list_position(l):
#     d = {}
#     for i in range(len(l)):
#         if l[i] not in d:
#             d[l[i]] = [i]
#         else:
#             d[l[i]] += [i]
#     return d
# return (list_position(l))

# -------------------------------------------------------------------------


# Problem 31: Calculate Average of Dictionary Values


# d = {"Alice": 90, "Bob": 80, "Charlie": 70}

# def cal_average(scores):
#     l = list(d.values())
#     sum = 0
#     for i in l:
#         sum += i
#     avg = sum/len(l)
#     return avg

# return (cal_average(d))
        


# ---------------------------------------------------------------------------


# Problem 32: Group Dictionary Keys by Value

# data = {"a": 1, "b": 2, "c": 1, "d": 3}

# def group_dic(data):
#     d = {}
#     for k,v in data.items():
#         if v not in d:
#             d[v] = [k]
#         else:
#             d[v] += [k]
#     return d
# return (group_dic(data))


# -----------------------------------------------------------------------------


# Problem 33: Dictionary Difference


# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 2, "d": 4}

# def dict_diff(dict1, dict2):
#     l = []

#     for k,v in dict1.items():
#         if k not in dict2:
#             l.append(k)
#     return l
# return (dict_diff(dict1, dict2))


# ---------------------------------------------------------------------------


# Problem 34: Count Vowels in a String

# text = "hello world"

# def count_vowels(text):
#     d = {}
#     v = 'aeiouAEIOU'
#     for i in text:
#         if i in v:
#             if i not in d:
#                 d[i] = 1
#             else:
#                 d[i] += 1
#     return d

# return (count_vowels(text))

# ----------------------------------------------------------------------

# Problem 35: Convert Two Lists into a Dictionary with Sum Values

# list1 = ["a", "b", "a", "c"]
# list2 = ["b", "a", "b", "d"]

# def list_to_dict(list1, list2):
#     l = list1+list2
#     d = {}
#     for i in l:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1
#     return d
# return (list_to_dict(list1, list2))


# ------------------------------------------------------------------------


# Problem 36: Calculate Grades Based on Score Ranges

# scores = {"Alice": 85, "Bob": 92, "Charlie": 67, "David": 73}

# def grades(n):
#     if n >= 90 and n<=100:
#         return 'A'
#     elif n>=80 and n<= 89:
#         return 'B'
#     elif n>=70 and n<=79:
#         return 'C'
#     else:
#         return 'F'
# # cal_grades(int(input()))

# def cal_grades(scores):
#     d = {}
#     for k,v in scores.items():
#         if k not in d:
#             d[k] = grades(v)
#         else:
#             d[k] += grades(v)
#     return d
# print(cal_grades(scores))


# ------------------------------------------------------------------------

# Problem 37: Invert a Dictionary with Lists

# data = {"fruits": ["apple", "banana"], "vegetables": ["carrot", "beet"]}

# def invert_a_dic(data):
#     d = {}

#     for k,v in data.items():
#         for i in range(len(v)):
#             if v[i] not in d:
#                 d[v[i]] = k
#             else:
#                 d[v[i]] += k

#     return d

# print(invert_a_dic(data))


# ---------------------------------------------------------------------------


# Problem 38: Filter Dictionary by Key Length


# data = {"apple": 5, "banana": 3, "pear": 2}
# n = 5

# def filter_dict(data, n):
#     d = {}
#     for k,v in data.items():
#         if len(k) == n:
#             if k not in d:
#                 d[k] = v
#             else:
#                 d[k] += v
#     return d
# print(filter_dict(data, n))


# -------------------------------------------------------------------


# Problem 39: Dictionary with Count of Elements Less than K

# data = {"a": 5, "b": 2, "c": 7, "d": 3}
# n = 4

# def dic_count(data, n):
#     d = {}
#     for k,v in data.items():
#         if v < n:
#             if 'count' not in d:
#                 d['count'] = 1
#             else:
#                 d['count'] += 1
#     return d
# print(dic_count(data, n))


# --------------------------------------------------------------------------


# Problem 40: Create Dictionary of Squares for Odd Numbers

# numbers = [1, 2, 3, 4, 5]

# def fun(numbers):
#     d = {}

#     for i in numbers:
#         if i%2 != 0:
#             if i not in d:
#                 d[i] = i**2
#             else:
#                 d[i] += i**2
#     return d
# print(fun(numbers))


# -------------------------------------------------------------------------

# Problem 41: Create Frequency Dictionary of Word Lengths


# words = ["apple", "banana", "pear", "kiwi", "orange"]

# def fun(words):
#     d = {}

#     for i in words:
#         length = len(i)

#         if length not in d:
#             d[length] = 1
#         else:
#             d[length] += 1
#     return d
# print(fun(words))


# -------------------------------------------------------------------------


# Problem 42: Create a Dictionary of Divisors

# numbers = [10, 15, 20]

# def divisors(n):
#     l = []
#     for i in range(1,n+1):
#         if n%i == 0:
#             l.append(i)
#     return l
# # print(divisors(int(input())))

# def dic_of_divisors(numbers):
#     d = {}

#     for i in numbers:
#         if i not in d:
#             d[i] = divisors(i)
#         else:
#             d[i] += divisors(i)

#     return d
# print(dic_of_divisors(numbers))


# ---------------------------------------------------------------------

# Problem 43: Character Position Mapping


# text = "hello world"
# text = ''.join(text)
# def character_positon(text):
#     d = {}

#     for i in range(len(text)):
#         if text[i] == ' ':
#             continue
#         elif text[i] not in d:
#             d[text[i]] = [i]
#         else:
#             d[text[i]] += [i]
#     return d
# print(character_positon(text)) 


# -----------------------------------------------------------------------------

# Problem 44: Transform Values Based on Function

# data = {"a": 4, "b": 9, "c": 16}

# import math
# def fun(n):
#     a = math.sqrt(n)
#     return a
# # print(fun(int(input())))

# def transform_values(data):
#     d = {}
#     for k,v in data.items():
#         if k not in d:
#             d[k] = fun(v)
#         else:
#             d[k] += fun(v)
#     return d
# print(transform_values(data))


# ----------------------------------------------------------------------


# Problem 45: Count Digits and Letters in String

# s = "hello123"

# def count_digits_letters(s):
#     d = {}
#     count = 0
#     c = 0
#     for i in range(len(s)):
#         if s[i].isalpha():
#             count += 1
#             d['letters'] = count
            
#         else:
#             c += 1
#             d['digits'] = c
#     return d
# print(count_digits_letters(s))
            

# -------------------------------------------------------------------------

